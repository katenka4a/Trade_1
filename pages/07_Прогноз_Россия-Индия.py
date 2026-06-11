"""
Страница прогноза внешнеторгового оборота: Россия—Индия.
Модели:
1) Линейная регрессия — базовая факторная модель;
2) ARIMA — временная модель;
3) Расширенный режим — линейная модель с временным трендом и структурными шоками;
4) Гибрид NN + RSS — расширенный режим + нейросетевая коррекция остатков + RSS/NLP-сигнал.
"""
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler

try:
    from utils import setup_i18n, render_lang_switcher
    setup_i18n()
except Exception:
    render_lang_switcher = None

try:
    from data.locales import install_streamlit_i18n, translate_text as TT
    install_streamlit_i18n(st)
except Exception:
    def TT(value):
        return value

from data.diploma_data import factors_in_df

# =============================================================
# ВШИТЫЕ НАСТРОЙКИ ДЛЯ ЗАЩИТЫ ДИПЛОМА
# =============================================================
PAIR_LABEL = "Россия—Индия"
DEFAULT_FACTORS = ['Курс USD/INR', 'BDI (Балтийский индекс)', 'Инфляция Индия']
FORECAST_END_YEAR = 2030
ARIMA_MAX_ORDER = (2, 2, 2)
RSS_SIGNAL_SCALE = 0.20

MODEL_LR = "Линейная регрессия"
MODEL_ARIMA = "ARIMA"
MODEL_EXT = "Расширенный режим"
MODEL_HYBRID = "Гибрид NN + RSS"
ALL_MODELS = [MODEL_LR, MODEL_ARIMA, MODEL_EXT, MODEL_HYBRID]

st.set_page_config(page_title="Прогноз Россия-Индия", page_icon=None, layout="wide")

st.markdown("""
<style>
html, body, [class*="css"] { font-family: 'Inter', sans-serif; color: #212529; }
h1, h2, h3 { font-family: 'Source Sans Pro', 'Inter', sans-serif; font-weight: 650; letter-spacing: -0.01em; color: #1a1a2e; }
.section-box { background:#FFFFFF; border-radius:10px; padding:1.1rem 1.25rem; border:1px solid #E9ECEF; margin-bottom:1rem; }
.good-box { background:#F3FAF6; border:1px solid #BDE5C8; border-radius:10px; padding:1rem 1.2rem; margin-bottom:1rem; }
.warn-box { background:#FFF8E8; border:1px solid #F1D28A; border-radius:10px; padding:1rem 1.2rem; margin-bottom:1rem; }
.model-card { background:#FFFFFF; border:1px solid #E9ECEF; border-radius:12px; padding:1rem; min-height:158px; }
.best-card { background:#F3FAF6; border:2px solid #58B36E; border-radius:12px; padding:1rem; min-height:158px; }
.small-muted { color:#6C757D; font-size:0.86rem; }
.big-number { font-size:1.45rem; font-weight:700; color:#1a1a2e; }
</style>
""", unsafe_allow_html=True)

header_cols = st.columns([7, 1])
with header_cols[1]:
    if render_lang_switcher:
        render_lang_switcher()

st.markdown(f"""
<div style="margin-bottom:1.2rem;">
    <div style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.08em; color:#6C757D; margin-bottom:0.25rem;">Forecast Engine</div>
    <h1 style="margin:0;">Прогноз Россия-Индия</h1>
    <p style="color:#6C757D; margin-top:0.35rem;">Сравнение четырёх моделей: линейная регрессия, ARIMA, расширенный режим и гибрид NN + RSS.</p>
</div>
""", unsafe_allow_html=True)

# =============================================================
# УТИЛИТЫ
# =============================================================
def fmt_bln(value: float) -> str:
    try:
        return f"{value / 1e9:,.1f} млрд $".replace(",", " ")
    except Exception:
        return "—"

def fmt_pct(value: float) -> str:
    if value is None or not np.isfinite(value):
        return "—"
    return f"{value:.1f}%"

def clean_numeric_df(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    out = df[["Год", "Y"] + columns].copy()
    for col in ["Год", "Y"] + columns:
        out[col] = pd.to_numeric(out[col], errors="coerce")
    out = out.dropna().sort_values("Год").reset_index(drop=True)
    out["Год"] = out["Год"].astype(int)
    return out

def add_regime_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["trend"] = out["Год"] - out["Год"].min()
    out["post_2022"] = (out["Год"] >= 2022).astype(int)
    out["trend_post_2022"] = np.where(out["Год"] >= 2022, out["Год"] - 2021, 0)
    out["shock_2020"] = (out["Год"] == 2020).astype(int)
    out["shock_2022"] = (out["Год"] == 2022).astype(int)
    return out

def get_hidden_test_years(years: pd.Series) -> int:
    last_year = int(np.max(years))
    return 1 if last_year <= 2023 else 2

def split_train_test(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, int]:
    n_test = get_hidden_test_years(df["Год"])
    if len(df) <= n_test + 5:
        n_test = 1
    return df.iloc[:-n_test].copy(), df.iloc[-n_test:].copy(), n_test

def metrics(y_true, y_pred) -> dict:
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    rmse = float(np.sqrt(mean_squared_error(y_true, y_pred)))
    mae = float(mean_absolute_error(y_true, y_pred))
    with np.errstate(divide="ignore", invalid="ignore"):
        mape = float(np.mean(np.abs((y_true - y_pred) / y_true)) * 100)
    try:
        r2 = float(r2_score(y_true, y_pred)) if len(y_true) > 1 else np.nan
    except Exception:
        r2 = np.nan
    return {"RMSE": rmse, "MAE": mae, "MAPE": mape, "R2_pred": r2}

def add_constant(df_x: pd.DataFrame) -> pd.DataFrame:
    return sm.add_constant(df_x, has_constant="add")

def fit_ols(train_df: pd.DataFrame, feature_cols: list[str]):
    X_train = add_constant(train_df[feature_cols])
    y_train = train_df["Y"]
    return sm.OLS(y_train, X_train).fit()

def predict_ols(model, df_x: pd.DataFrame, feature_cols: list[str]) -> np.ndarray:
    X = add_constant(df_x[feature_cols])
    return np.asarray(model.predict(X), dtype=float)

def prediction_interval_ols(model, df_x: pd.DataFrame, feature_cols: list[str], alpha: float) -> pd.DataFrame:
    X = add_constant(df_x[feature_cols])
    sf = model.get_prediction(X).summary_frame(alpha=alpha)
    return pd.DataFrame({
        "mean": sf["mean"].astype(float),
        "lower": sf["obs_ci_lower"].astype(float),
        "upper": sf["obs_ci_upper"].astype(float),
    })

def select_arima_order(y: pd.Series) -> tuple[int, int, int]:
    best_order = (1, 1, 0)
    best_aic = np.inf
    pmax, dmax, qmax = ARIMA_MAX_ORDER
    for p in range(pmax + 1):
        for d in range(dmax + 1):
            for q in range(qmax + 1):
                if p == 0 and d == 0 and q == 0:
                    continue
                try:
                    res = ARIMA(y, order=(p, d, q), enforce_stationarity=False, enforce_invertibility=False).fit()
                    if np.isfinite(res.aic) and res.aic < best_aic:
                        best_aic = res.aic
                        best_order = (p, d, q)
                except Exception:
                    continue
    return best_order

def fit_arima(y: pd.Series, order: tuple[int, int, int] | None = None):
    if order is None:
        order = select_arima_order(y)
    model = ARIMA(y, order=order, enforce_stationarity=False, enforce_invertibility=False).fit()
    return model, order

def forecast_arima(model, steps: int, alpha: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    fc = model.get_forecast(steps=steps)
    mean = np.asarray(fc.predicted_mean, dtype=float)
    ci = fc.conf_int(alpha=alpha)
    lower = np.asarray(ci.iloc[:, 0], dtype=float)
    upper = np.asarray(ci.iloc[:, 1], dtype=float)
    return mean, lower, upper

def future_factor_frame(df_hist: pd.DataFrame, base_feature_cols: list[str], end_year: int) -> pd.DataFrame:
    last_year = int(df_hist["Год"].max())
    future_years = list(range(last_year + 1, end_year + 1))
    if not future_years:
        return pd.DataFrame(columns=["Год"] + base_feature_cols)

    rows = []
    last_values = df_hist[base_feature_cols].iloc[-1].astype(float).to_dict()
    growth_rates = {}
    for col in base_feature_cols:
        s = df_hist[col].astype(float).replace([np.inf, -np.inf], np.nan).dropna()
        if len(s) >= 5 and abs(float(s.iloc[-5])) > 1e-12 and float(s.iloc[-1]) > 0 and float(s.iloc[-5]) > 0:
            growth_rates[col] = (float(s.iloc[-1]) / float(s.iloc[-5])) ** (1 / 4) - 1
        elif len(s) >= 2 and abs(float(s.iloc[-2])) > 1e-12:
            growth_rates[col] = float(s.iloc[-1] / s.iloc[-2] - 1)
        else:
            growth_rates[col] = 0.0
        growth_rates[col] = float(np.clip(growth_rates[col], -0.25, 0.25))

    current = last_values.copy()
    for year in future_years:
        row = {"Год": year}
        for col in base_feature_cols:
            current[col] = current[col] * (1 + growth_rates[col])
            row[col] = current[col]
        rows.append(row)
    return pd.DataFrame(rows)

def make_regime_future(df_future_base: pd.DataFrame, first_year: int) -> pd.DataFrame:
    out = df_future_base.copy()
    out["trend"] = out["Год"] - first_year
    out["post_2022"] = (out["Год"] >= 2022).astype(int)
    out["trend_post_2022"] = np.where(out["Год"] >= 2022, out["Год"] - 2021, 0)
    out["shock_2020"] = 0
    out["shock_2022"] = 0
    return out

def fit_residual_mlp(train_df: pd.DataFrame, base_model, feature_cols: list[str]):
    base_pred = predict_ols(base_model, train_df, feature_cols)
    residuals = np.asarray(train_df["Y"], dtype=float) - base_pred
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(train_df[feature_cols].astype(float))
    mlp = MLPRegressor(
        hidden_layer_sizes=(4,),
        activation="tanh",
        solver="lbfgs",
        alpha=0.05,
        max_iter=5000,
        random_state=42,
    )
    mlp.fit(X_scaled, residuals)
    fitted_residuals = np.asarray(mlp.predict(X_scaled), dtype=float)
    error_std = float(np.std(residuals - fitted_residuals, ddof=1)) if len(residuals) > 2 else 0.0
    return mlp, scaler, fitted_residuals, error_std

def predict_residual_mlp(mlp, scaler, df_x: pd.DataFrame, feature_cols: list[str]) -> np.ndarray:
    X_scaled = scaler.transform(df_x[feature_cols].astype(float))
    return np.asarray(mlp.predict(X_scaled), dtype=float)

def walk_forward_hybrid_validation(df_regime: pd.DataFrame, feature_cols: list[str], min_train_size: int = 8) -> tuple[dict, pd.DataFrame]:
    y_true, y_pred, pred_years = [], [], []
    min_train_size = min(max(min_train_size, len(feature_cols) + 3), max(len(df_regime) - 1, 1))
    for split_idx in range(min_train_size, len(df_regime)):
        hist = df_regime.iloc[:split_idx].copy()
        target = df_regime.iloc[split_idx:split_idx + 1].copy()
        try:
            base_model = fit_ols(hist, feature_cols)
            base_target_pred = predict_ols(base_model, target, feature_cols)
            mlp, scaler, _, _ = fit_residual_mlp(hist, base_model, feature_cols)
            resid_target_pred = predict_residual_mlp(mlp, scaler, target, feature_cols)
            y_true.append(float(target["Y"].iloc[0]))
            y_pred.append(float(base_target_pred[0] + resid_target_pred[0]))
            pred_years.append(int(target["Год"].iloc[0]))
        except Exception:
            continue
    if len(y_true) == 0:
        return {"RMSE": np.nan, "MAE": np.nan, "MAPE": np.nan, "R2_pred": np.nan}, pd.DataFrame()
    details = pd.DataFrame({"Год": pred_years, "Факт": y_true, "Прогноз": y_pred})
    return metrics(y_true, y_pred), details

def collect_rss_signal(pair_label: str, queries: list[str]) -> dict:
    default = {
        "available": False,
        "avg_sentiment": 0.0,
        "max_sentiment": 0.0,
        "min_sentiment": 0.0,
        "positive_share": 0.0,
        "negative_share": 0.0,
        "neutral_share": 100.0,
        "articles": [],
        "message": "RSS-ленты не вернули достаточное количество новостей для анализа тональности.",
    }
    try:
        import feedparser
        from textblob import TextBlob
        from urllib.parse import quote_plus
        from datetime import datetime, timedelta
    except Exception as exc:
        default["message"] = f"RSS-анализ временно недоступен: {exc}"
        return default

    rss_urls = []
    for q in queries:
        rss_urls.append(f"https://news.google.com/rss/search?q={quote_plus(q)}&hl=ru&gl=RU&ceid=RU:ru")
        rss_urls.append(f"https://news.google.com/rss/search?q={quote_plus(q)}&hl=en&gl=US&ceid=US:en")

    all_articles = []
    seen_titles = set()
    for url in rss_urls[:8]:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:5]:
                title = entry.get("title", "").strip()
                if title and title not in seen_titles:
                    seen_titles.add(title)
                    try:
                        date = datetime(*entry.published_parsed[:6])
                    except Exception:
                        date = datetime.now()
                    all_articles.append({
                        "title": title,
                        "date": date,
                        "link": entry.get("link", ""),
                        "source": entry.get("source", {}).get("title", "Google News") if hasattr(entry, "source") else "Google News",
                    })
        except Exception:
            continue

    if len(all_articles) < 3:
        return default

    week_ago = datetime.now() - timedelta(days=7)
    recent = [a for a in all_articles if a["date"] >= week_ago]
    if len(recent) < 3:
        recent = all_articles[:10]

    sentiments = []
    for article in recent:
        try:
            sentiments.append(float(TextBlob(article["title"]).sentiment.polarity))
        except Exception:
            sentiments.append(0.0)
    sentiments_arr = np.asarray(sentiments, dtype=float)
    positive_share = float(np.sum(sentiments_arr > 0.05)) / len(sentiments_arr) * 100
    negative_share = float(np.sum(sentiments_arr < -0.05)) / len(sentiments_arr) * 100
    return {
        "available": True,
        "avg_sentiment": float(np.mean(sentiments_arr)),
        "max_sentiment": float(np.max(sentiments_arr)),
        "min_sentiment": float(np.min(sentiments_arr)),
        "positive_share": positive_share,
        "negative_share": negative_share,
        "neutral_share": max(0.0, 100 - positive_share - negative_share),
        "articles": recent,
        "message": "ok",
    }

def formula_and_comment(model_name: str, factors: list[str], arima_order: tuple[int, int, int] | None = None) -> tuple[str, str]:
    x_part = " + ".join([f"β{i+1}·{x}" for i, x in enumerate(factors)])
    if model_name == MODEL_LR:
        formula = f"Yₜ = β₀ + {x_part} + εₜ"
        comment = "Базовая линейная регрессия служит точкой отсчёта и показывает связь оборота с отобранными макроэкономическими факторами."
    elif model_name == MODEL_ARIMA:
        order_text = f"{arima_order}" if arima_order else "(p,d,q)"
        formula = f"ARIMA{order_text}: Yₜ = f(Yₜ₋₁, Yₜ₋₂, …, εₜ₋₁, εₜ₋₂)"
        comment = "ARIMA прогнозирует ряд по собственной динамике: тренду, инерции и прошлым ошибкам, без внешних факторов."
    elif model_name == MODEL_EXT:
        formula = f"Yₜ = β₀ + {x_part} + βₜ·t + γ₁·post2022ₜ + γ₂·trend_post2022ₜ + γ₃·shock2020ₜ + γ₄·shock2022ₜ + εₜ"
        comment = "Расширенный режим учитывает макрофакторы, общий временной тренд, структурный перелом после 2022 года и разовые кризисные импульсы."
    else:
        formula = "Ŷᴴₜ = Ŷᴿₜ + NN(Xₜ) + δ_RSSₜ"
        comment = "Гибридная модель использует прогноз расширенного режима как базу, добавляет нейросетевую коррекцию остаточной компоненты и текущий RSS/NLP-сигнал новостного фона."
    return formula, comment

def safe_stat(value, as_money=False, as_percent=False):
    if value is None or not np.isfinite(value):
        return "—"
    if as_money:
        return fmt_bln(value)
    if as_percent:
        return fmt_pct(value)
    return f"{value:.3f}"

def ols_coef_table(model) -> pd.DataFrame:
    return pd.DataFrame({
        "Параметр": model.params.index,
        "Коэффициент": model.params.values,
        "Std. Error": model.bse.values,
        "t-stat": model.tvalues.values,
        "p-value": model.pvalues.values,
    })

def arima_param_table(model) -> pd.DataFrame:
    params = pd.Series(getattr(model, "params", []))
    try:
        names = list(model.param_names)
    except Exception:
        names = [f"param_{i}" for i in range(len(params))]
    try:
        bse = np.asarray(model.bse, dtype=float)
    except Exception:
        bse = np.full(len(params), np.nan)
    try:
        zvalues = np.asarray(model.zvalues, dtype=float)
    except Exception:
        zvalues = np.full(len(params), np.nan)
    try:
        pvalues = np.asarray(model.pvalues, dtype=float)
    except Exception:
        pvalues = np.full(len(params), np.nan)
    return pd.DataFrame({
        "Параметр": names,
        "Коэффициент": np.asarray(params, dtype=float),
        "Std. Error": bse,
        "z-stat": zvalues,
        "p-value": pvalues,
    })

def mlp_weights_table(mlp, feature_cols: list[str]) -> pd.DataFrame:
    rows = []
    if mlp is None:
        return pd.DataFrame(columns=["Слой", "Параметр", "Коэффициент"])
    input_names = list(feature_cols)
    for layer_idx, weights in enumerate(mlp.coefs_):
        weights = np.asarray(weights, dtype=float)
        if layer_idx == 0:
            from_names = input_names
            to_names = [f"нейрон_{j+1}" for j in range(weights.shape[1])]
        else:
            from_names = [f"нейрон_{i+1}" for i in range(weights.shape[0])]
            to_names = ["выход"] if weights.shape[1] == 1 else [f"выход_{j+1}" for j in range(weights.shape[1])]
        for i, from_name in enumerate(from_names):
            for j, to_name in enumerate(to_names):
                rows.append({
                    "Слой": f"W{layer_idx+1}",
                    "Параметр": f"{from_name} → {to_name}",
                    "Коэффициент": float(weights[i, j]),
                })
    for layer_idx, intercepts in enumerate(mlp.intercepts_):
        for j, value in enumerate(np.asarray(intercepts, dtype=float)):
            rows.append({
                "Слой": f"b{layer_idx+1}",
                "Параметр": f"свободный член {j+1}",
                "Коэффициент": float(value),
            })
    return pd.DataFrame(rows)

# =============================================================
# НАСТРОЙКИ СТРАНИЦЫ
# =============================================================
raw_df = factors_in_df.copy()
available_factors = [f for f in DEFAULT_FACTORS if f in raw_df.columns]
missing_factors = [f for f in DEFAULT_FACTORS if f not in raw_df.columns]

if missing_factors:
    st.warning("В данных не найдены некоторые факторы: " + ", ".join(missing_factors))

if len(available_factors) == 0:
    st.error("Нет доступных факторов для построения регрессионных моделей.")
    st.stop()

ci_choice = st.radio(
    "Доверительный интервал прогноза",
    ["80%", "95%", "99%"],
    index=0,
    horizontal=True,
    help="Это единственная настраиваемая статистическая опция. Остальные параметры зафиксированы, чтобы не перегружать страницу."
)
alpha_map = {"80%": 0.20, "95%": 0.05, "99%": 0.01}
alpha = alpha_map[ci_choice]

model_to_explain = st.selectbox(
    "Пояснить модель",
    ALL_MODELS,
    index=2,
    help="Все четыре модели рассчитываются и сравниваются ниже. Этот выбор меняет только формулу и пояснение."
)

# =============================================================
# ПОДГОТОВКА ДАННЫХ
# =============================================================
df_base = clean_numeric_df(raw_df, available_factors)
df_regime = add_regime_features(df_base)
regime_cols = available_factors + ["trend", "post_2022", "trend_post_2022", "shock_2020", "shock_2022"]

train_base, test_base, hidden_test_years = split_train_test(df_base)
train_regime, test_regime, _ = split_train_test(df_regime)
steps_future = FORECAST_END_YEAR - int(df_base["Год"].max())
if steps_future <= 0:
    st.error("Последний год в данных уже не меньше 2030. Горизонт прогноза некорректен.")
    st.stop()

# =============================================================
# RSS-СИГНАЛ ДО ФИНАЛЬНОГО ПРОГНОЗА
# =============================================================
rss_signal = collect_rss_signal(PAIR_LABEL, ['Россия Индия торговля', 'Russia India trade', 'Russia India economic cooperation', 'Россия Индия экономика'])
rss_avg = float(rss_signal.get("avg_sentiment", 0.0))

# =============================================================
# ОБУЧЕНИЕ ДЛЯ СРАВНЕНИЯ НА КОНТРОЛЬНОМ ПЕРИОДЕ
# =============================================================
try:
    lr_train = fit_ols(train_base, available_factors)
    lr_test_pred = predict_ols(lr_train, test_base, available_factors)
    lr_test_metrics = metrics(test_base["Y"], lr_test_pred)
except Exception as exc:
    st.error(f"Не удалось построить базовую линейную регрессию: {exc}")
    st.stop()

try:
    regime_train = fit_ols(train_regime, regime_cols)
    regime_test_pred = predict_ols(regime_train, test_regime, regime_cols)
    regime_test_metrics = metrics(test_regime["Y"], regime_test_pred)
except Exception as exc:
    st.error(f"Не удалось построить модель расширенного режима: {exc}")
    st.stop()

try:
    arima_train, arima_order = fit_arima(train_base["Y"])
    arima_test_pred, _, _ = forecast_arima(arima_train, len(test_base), alpha)
    arima_test_metrics = metrics(test_base["Y"], arima_test_pred)
except Exception:
    arima_order = (1, 1, 0)
    arima_train, arima_order = fit_arima(train_base["Y"], arima_order)
    arima_test_pred, _, _ = forecast_arima(arima_train, len(test_base), alpha)
    arima_test_metrics = metrics(test_base["Y"], arima_test_pred)

try:
    hybrid_test_metrics, hybrid_walk_df = walk_forward_hybrid_validation(df_regime, regime_cols)
    if not np.isfinite(hybrid_test_metrics.get("MAPE", np.nan)):
        mlp_train, scaler_train, _, _ = fit_residual_mlp(train_regime, regime_train, regime_cols)
        hybrid_test_pred = regime_test_pred + predict_residual_mlp(mlp_train, scaler_train, test_regime, regime_cols)
        hybrid_test_metrics = metrics(test_regime["Y"], hybrid_test_pred)
        hybrid_walk_df = pd.DataFrame({"Год": test_regime["Год"], "Факт": test_regime["Y"], "Прогноз": hybrid_test_pred})
except Exception:
    hybrid_test_metrics = {"RMSE": np.nan, "MAE": np.nan, "MAPE": np.nan, "R2_pred": np.nan}
    hybrid_walk_df = pd.DataFrame()

# =============================================================
# ФИНАЛЬНЫЕ МОДЕЛИ НА ВСЕЙ ИСТОРИИ И ПРОГНОЗ ДО 2030
# =============================================================
lr_full = fit_ols(df_base, available_factors)
regime_full = fit_ols(df_regime, regime_cols)
arima_full, arima_full_order = fit_arima(df_base["Y"], arima_order)
mlp_full, scaler_full, fitted_residuals_full, mlp_error_std = fit_residual_mlp(df_regime, regime_full, regime_cols)

future_base = future_factor_frame(df_base, available_factors, FORECAST_END_YEAR)
future_regime = make_regime_future(future_base, int(df_base["Год"].min()))
future_years = future_base["Год"].astype(int).tolist()

lr_fc_frame = prediction_interval_ols(lr_full, future_base, available_factors, alpha)
regime_fc_frame = prediction_interval_ols(regime_full, future_regime, regime_cols, alpha)
arima_mean, arima_lower, arima_upper = forecast_arima(arima_full, steps_future, alpha)

hybrid_residual_future = predict_residual_mlp(mlp_full, scaler_full, future_regime, regime_cols)
regime_pi_width = np.asarray(regime_fc_frame["upper"] - regime_fc_frame["lower"], dtype=float)
rss_adjustment = np.clip(rss_avg, -0.5, 0.5) * regime_pi_width * RSS_SIGNAL_SCALE
hybrid_mean = np.asarray(regime_fc_frame["mean"], dtype=float) + hybrid_residual_future + rss_adjustment
hybrid_lower = np.asarray(regime_fc_frame["lower"], dtype=float) + hybrid_residual_future + rss_adjustment - mlp_error_std
hybrid_upper = np.asarray(regime_fc_frame["upper"], dtype=float) + hybrid_residual_future + rss_adjustment + mlp_error_std
hybrid_lower, hybrid_upper = np.minimum(hybrid_lower, hybrid_upper), np.maximum(hybrid_lower, hybrid_upper)

forecast_2030 = {
    MODEL_LR: float(lr_fc_frame["mean"].iloc[-1]),
    MODEL_ARIMA: float(arima_mean[-1]),
    MODEL_EXT: float(regime_fc_frame["mean"].iloc[-1]),
    MODEL_HYBRID: float(hybrid_mean[-1]),
}
interval_2030 = {
    MODEL_LR: (float(lr_fc_frame["lower"].iloc[-1]), float(lr_fc_frame["upper"].iloc[-1])),
    MODEL_ARIMA: (float(arima_lower[-1]), float(arima_upper[-1])),
    MODEL_EXT: (float(regime_fc_frame["lower"].iloc[-1]), float(regime_fc_frame["upper"].iloc[-1])),
    MODEL_HYBRID: (float(hybrid_lower[-1]), float(hybrid_upper[-1])),
}

comparison_rows = []
for name, m in [
    (MODEL_LR, lr_test_metrics),
    (MODEL_ARIMA, arima_test_metrics),
    (MODEL_EXT, regime_test_metrics),
    (MODEL_HYBRID, hybrid_test_metrics),
]:
    lower, upper = interval_2030[name]
    comparison_rows.append({
        "Модель": name,
        "Ошибка MAPE": m["MAPE"],
        "Ошибка RMSE": m["RMSE"],
        "Ошибка MAE": m["MAE"],
        "Прогноз 2030": forecast_2030[name],
        "Нижняя граница": lower,
        "Верхняя граница": upper,
        "Ширина интервала": upper - lower,
    })
comparison_df = pd.DataFrame(comparison_rows)
lr_mape = comparison_df.loc[comparison_df["Модель"] == MODEL_LR, "Ошибка MAPE"].iloc[0]
comparison_df["Улучшение к LR, %"] = np.where(
    np.isfinite(lr_mape) & (abs(lr_mape) > 1e-12),
    (lr_mape - comparison_df["Ошибка MAPE"]) / lr_mape * 100,
    np.nan,
)
best_row = comparison_df.loc[comparison_df["Ошибка MAPE"].idxmin()]
best_model = str(best_row["Модель"])

# =============================================================
# ПОНЯТНОЕ ПОЯСНЕНИЕ МОДЕЛИ
# =============================================================
formula, comment = formula_and_comment(model_to_explain, available_factors, arima_order if model_to_explain == MODEL_ARIMA else None)
st.markdown("### Формула и смысл выбранной модели")
st.markdown(f"""
<div class="section-box">
    <div style="font-size:1.05rem; font-weight:700; margin-bottom:0.55rem;">{model_to_explain}</div>
    <div style="font-size:1.02rem; padding:0.75rem 0.9rem; background:#F8F9FA; border-radius:8px; margin-bottom:0.7rem;"><code>{formula}</code></div>
    <div class="small-muted">{comment}</div>
</div>
""", unsafe_allow_html=True)

# =============================================================
# БЛОК ЛУЧШЕЙ МОДЕЛИ
# =============================================================
benchmark_mape = float(comparison_df.loc[comparison_df["Модель"] == MODEL_LR, "Ошибка MAPE"].iloc[0])
best_mape = float(best_row["Ошибка MAPE"])
if best_model == MODEL_LR:
    best_comment = "Базовая линейная регрессия оказалась наиболее устойчивой на контрольном периоде. Это значит, что усложнение модели пока не даёт выигрыша по ошибке."
else:
    gain = (benchmark_mape - best_mape) / benchmark_mape * 100 if benchmark_mape else np.nan
    best_comment = f"{best_model} показывает минимальную среднюю процентную ошибку на контрольном периоде и улучшает результат относительно линейной регрессии на {gain:.1f}%."

st.markdown(f"""
<div class="good-box">
    <div style="font-size:0.82rem; text-transform:uppercase; letter-spacing:0.06em; color:#477B55;">Лучшая модель по контрольной ошибке MAPE</div>
    <div style="font-size:1.45rem; font-weight:750; margin:0.15rem 0 0.35rem 0;">{best_model}</div>
    <div>{best_comment}</div>
</div>
""", unsafe_allow_html=True)

# =============================================================
# КАРТОЧКИ МОДЕЛЕЙ
# =============================================================
st.markdown("### Быстрое сравнение четырёх моделей")
card_cols = st.columns(4)
for i, row in comparison_df.iterrows():
    name = row["Модель"]
    card_class = "best-card" if name == best_model else "model-card"
    status = "Лучшая модель" if name == best_model else ("Бенчмарк" if name == MODEL_LR else "Альтернатива")
    with card_cols[i]:
        st.markdown(f"""
        <div class="{card_class}">
            <div style="font-size:0.82rem; color:#6C757D; margin-bottom:0.2rem;">{status}</div>
            <div style="font-size:1.08rem; font-weight:700; margin-bottom:0.55rem;">{name}</div>
            <div class="small-muted">Ошибка на тесте</div>
            <div class="big-number">{fmt_pct(row['Ошибка MAPE'])}</div>
            <div class="small-muted" style="margin-top:0.55rem;">Прогноз на 2030</div>
            <div style="font-size:1.1rem; font-weight:700;">{fmt_bln(row['Прогноз 2030'])}</div>
            <div class="small-muted" style="margin-top:0.35rem;">Интервал {ci_choice}: {fmt_bln(row['Нижняя граница'])} — {fmt_bln(row['Верхняя граница'])}</div>
        </div>
        """, unsafe_allow_html=True)

# =============================================================
# ТАБЛИЦА СРАВНЕНИЯ
# =============================================================
st.markdown("### Таблица сравнения")
st.caption("Главный критерий выбора — MAPE: средняя ошибка прогноза в процентах. Чем меньше, тем лучше.")
view_df = comparison_df.copy()
view_df["Статус"] = view_df["Модель"].apply(lambda x: "Лучшая" if x == best_model else ("Бенчмарк" if x == MODEL_LR else "Альтернатива"))
view_df = view_df[["Статус", "Модель", "Ошибка MAPE", "Ошибка RMSE", "Прогноз 2030", "Нижняя граница", "Верхняя граница", "Улучшение к LR, %"]]
view_df["Ошибка MAPE"] = view_df["Ошибка MAPE"].apply(fmt_pct)
view_df["Ошибка RMSE"] = view_df["Ошибка RMSE"].apply(fmt_bln)
view_df["Прогноз 2030"] = view_df["Прогноз 2030"].apply(fmt_bln)
view_df["Нижняя граница"] = view_df["Нижняя граница"].apply(fmt_bln)
view_df["Верхняя граница"] = view_df["Верхняя граница"].apply(fmt_bln)
view_df["Улучшение к LR, %"] = view_df["Улучшение к LR, %"].apply(lambda x: "—" if not np.isfinite(x) else f"{x:+.1f}%")
st.dataframe(view_df, use_container_width=True, hide_index=True)

# =============================================================
# ГРАФИК
# =============================================================
st.markdown("### График факта и прогнозов")
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df_base["Год"], y=df_base["Y"] / 1e9,
    mode="lines+markers", name="Факт", line=dict(width=3)
))

lr_fit_all = predict_ols(lr_full, df_base, available_factors)
regime_fit_all = predict_ols(regime_full, df_regime, regime_cols)
hybrid_fit_all = regime_fit_all + fitted_residuals_full
try:
    arima_fitted = np.asarray(arima_full.fittedvalues, dtype=float)
    arima_years = df_base["Год"].iloc[-len(arima_fitted):]
except Exception:
    arima_fitted = np.array([])
    arima_years = []

fig.add_trace(go.Scatter(x=df_base["Год"], y=lr_fit_all / 1e9, mode="lines", name="Линейная регрессия история", line=dict(width=1.7, dash="dash")))
if len(arima_fitted):
    fig.add_trace(go.Scatter(x=arima_years, y=arima_fitted / 1e9, mode="lines", name="ARIMA история", line=dict(width=1.7, dash="dot")))
fig.add_trace(go.Scatter(x=df_regime["Год"], y=regime_fit_all / 1e9, mode="lines", name="Расширенный режим история", line=dict(width=2)))
fig.add_trace(go.Scatter(x=df_regime["Год"], y=hybrid_fit_all / 1e9, mode="lines", name="Гибрид NN + RSS история", line=dict(width=2, dash="dashdot")))

fig.add_trace(go.Scatter(x=future_years, y=lr_fc_frame["mean"] / 1e9, mode="lines+markers", name="Линейная регрессия прогноз", line=dict(width=1.7, dash="dash")))
fig.add_trace(go.Scatter(x=future_years, y=arima_mean / 1e9, mode="lines+markers", name="ARIMA прогноз", line=dict(width=1.7, dash="dot")))
fig.add_trace(go.Scatter(x=future_years, y=regime_fc_frame["mean"] / 1e9, mode="lines+markers", name="Расширенный режим прогноз", line=dict(width=2.4)))
fig.add_trace(go.Scatter(x=future_years, y=hybrid_mean / 1e9, mode="lines+markers", name="Гибрид NN + RSS прогноз", line=dict(width=2.4, dash="dashdot")))

if best_model == MODEL_LR:
    lower = lr_fc_frame["lower"].values / 1e9
    upper = lr_fc_frame["upper"].values / 1e9
elif best_model == MODEL_ARIMA:
    lower = arima_lower / 1e9
    upper = arima_upper / 1e9
elif best_model == MODEL_EXT:
    lower = regime_fc_frame["lower"].values / 1e9
    upper = regime_fc_frame["upper"].values / 1e9
else:
    lower = hybrid_lower / 1e9
    upper = hybrid_upper / 1e9

fig.add_trace(go.Scatter(x=future_years, y=upper, mode="lines", name=f"Верхняя граница {ci_choice}", line=dict(width=0), showlegend=False))
fig.add_trace(go.Scatter(x=future_years, y=lower, mode="lines", name=f"Интервал лучшей модели {ci_choice}", fill="tonexty", line=dict(width=0)))

fig.update_layout(
    height=540,
    template="plotly_white",
    yaxis=dict(title="млрд $"),
    xaxis=dict(title="Год"),
    hovermode="x unified",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
)
st.plotly_chart(fig, use_container_width=True)

# =============================================================
# ПРОГНОЗНАЯ ТАБЛИЦА ПО ГОДАМ
# =============================================================
st.markdown("### Прогноз по годам")
forecast_table = pd.DataFrame({
    "Год": future_years,
    MODEL_LR: [fmt_bln(v) for v in lr_fc_frame["mean"]],
    MODEL_ARIMA: [fmt_bln(v) for v in arima_mean],
    MODEL_EXT: [fmt_bln(v) for v in regime_fc_frame["mean"]],
    MODEL_HYBRID: [fmt_bln(v) for v in hybrid_mean],
})
st.dataframe(forecast_table, use_container_width=True, hide_index=True)

# =============================================================
# RSS-БЛОК
# =============================================================
st.markdown("### RSS/NLP-сигнал новостного фона")
st.caption("Текущий RSS/NLP-сигнал используется только в финальном прогнозе гибридной модели и не пересчитывает исторические ошибки моделей.")

if rss_signal["available"]:
    avg_sentiment = rss_signal["avg_sentiment"]
    if avg_sentiment > 0.05:
        direction_icon = "📈"
        direction_text = "ПОЗИТИВНАЯ"
        correction_note = "Гибридный прогноз получает положительное RSS/NLP-смещение: текущий новостной фон указывает на повышенную вероятность значения ближе к верхней части прогнозного интервала."
        arrow = "↑"
    elif avg_sentiment < -0.05:
        direction_icon = "📉"
        direction_text = "НЕГАТИВНАЯ"
        correction_note = "Гибридный прогноз получает отрицательное RSS/NLP-смещение: текущий новостной фон указывает на повышенную вероятность значения ближе к нижней части прогнозного интервала."
        arrow = "↓"
    else:
        direction_icon = "↔️"
        direction_text = "НЕЙТРАЛЬНАЯ"
        correction_note = "RSS/NLP-сигнал близок к нейтральному, поэтому финальная поправка гибридной модели минимальна."
        arrow = "→"

    st.markdown(f"""
    <div class="section-box">
        <div style="display:flex; align-items:center; gap:0.75rem; margin-bottom:0.75rem;">
            <span style="font-size:1.8rem;">{direction_icon}</span>
            <div>
                <div style="font-size:0.82rem; text-transform:uppercase; letter-spacing:0.06em; color:#6C757D;">
                    RSS-анализ за последние 7 дней · {len(rss_signal['articles'])} новостей
                </div>
                <div style="font-size:1.25rem; font-weight:700;">
                    Тональность: {avg_sentiment:+.3f} ({direction_text}) {arrow}
                </div>
            </div>
        </div>
        <div style="display:flex; gap:1.5rem; flex-wrap:wrap; margin-bottom:0.75rem;">
            <div><span class="small-muted">Макс.:</span> {rss_signal['max_sentiment']:+.3f}</div>
            <div><span class="small-muted">Мин.:</span> {rss_signal['min_sentiment']:+.3f}</div>
            <div><span class="small-muted">Позитивных:</span> {rss_signal['positive_share']:.0f}%</div>
            <div><span class="small-muted">Негативных:</span> {rss_signal['negative_share']:.0f}%</div>
            <div><span class="small-muted">Нейтральных:</span> {rss_signal['neutral_share']:.0f}%</div>
        </div>
        <div style="padding:0.65rem 0.9rem; background:#F8F9FA; border-radius:8px; font-size:0.92rem;">
            {correction_note}
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("Последние новости RSS", expanded=False):
        for article in rss_signal["articles"][:8]:
            st.markdown(f"- [{article['title']}]({article['link']}) · {article['date'].strftime('%d.%m')}")
else:
    st.info(rss_signal["message"])

# =============================================================
# МЕТОДОЛОГИЯ И СТАТИСТИКА ДЛЯ ЗАЩИТЫ
# =============================================================
with st.expander("Методология расчёта", expanded=False):
    st.markdown(f"""
    **Что сравнивается:**

    1. **Линейная регрессия** — базовый benchmark на макроэкономических факторах: {', '.join(available_factors)}.
    2. **ARIMA** — временная модель, которая прогнозирует ряд по его собственной динамике без внешних факторов.
    3. **Расширенный режим** — факторная модель, дополненная общим временным трендом `trend` и переменными `post_2022`, `trend_post_2022`, `shock_2020`, `shock_2022`.
    4. **Гибрид NN + RSS** — прогноз расширенного режима, дополненный нейросетевой коррекцией остаточной компоненты и текущим RSS/NLP-сигналом.

    **Как выбирается лучшая модель:** по минимальной ошибке MAPE на контрольном периоде.  
    Контрольный период зашит в коде и составляет **{hidden_test_years} последний год/года** для линейной регрессии, ARIMA и расширенного режима. Для гибрида дополнительно используется walk-forward проверка по годам, шагов проверки: **{len(hybrid_walk_df)}**.

    **Как строится финальный прогноз:** после сравнения все модели переобучаются на всей доступной истории и прогнозируют период до 2030 года.

    **RSS/NLP:** текущая тональность новостей входит в финальный прогноз гибридной модели как оперативный индикатор новостного фона. Текущий RSS-сигнал: **{rss_avg:+.3f}**.

    **Доверительный интервал:** выбранный уровень — **{ci_choice}**. Для линейных моделей используется интервал прогноза нового наблюдения, для ARIMA — стандартный интервал прогноза временного ряда, для гибрида — интервал расширенного режима, дополненный ошибкой нейросетевой коррекции остатков.
    """)

with st.expander("Статистика моделей для защиты", expanded=False):
    stat_rows = []
    for label, model in [(MODEL_LR, lr_full), (MODEL_EXT, regime_full)]:
        stat_rows.append({
            "Модель": label,
            "R²": getattr(model, "rsquared", np.nan),
            "Adjusted R²": getattr(model, "rsquared_adj", np.nan),
            "AIC": getattr(model, "aic", np.nan),
            "BIC": getattr(model, "bic", np.nan),
            "F-statistic": getattr(model, "fvalue", np.nan),
            "p-value модели": getattr(model, "f_pvalue", np.nan),
            "MAPE проверки": comparison_df.loc[comparison_df["Модель"] == label, "Ошибка MAPE"].iloc[0],
        })
    stat_rows.append({
        "Модель": f"ARIMA{arima_full_order}",
        "R²": np.nan,
        "Adjusted R²": np.nan,
        "AIC": getattr(arima_full, "aic", np.nan),
        "BIC": getattr(arima_full, "bic", np.nan),
        "F-statistic": np.nan,
        "p-value модели": np.nan,
        "MAPE проверки": comparison_df.loc[comparison_df["Модель"] == MODEL_ARIMA, "Ошибка MAPE"].iloc[0],
    })
    stat_rows.append({
        "Модель": MODEL_HYBRID,
        "R²": np.nan,
        "Adjusted R²": np.nan,
        "AIC": np.nan,
        "BIC": np.nan,
        "F-statistic": np.nan,
        "p-value модели": np.nan,
        "MAPE проверки": comparison_df.loc[comparison_df["Модель"] == MODEL_HYBRID, "Ошибка MAPE"].iloc[0],
    })
    stat_df = pd.DataFrame(stat_rows)
    st.dataframe(stat_df, use_container_width=True, hide_index=True)

    selected_for_coef = st.radio(
        "Показать коэффициенты / параметры",
        ALL_MODELS,
        horizontal=True,
        index=2,
    )

    if selected_for_coef == MODEL_LR:
        st.markdown("**Коэффициенты линейной регрессии**")
        st.dataframe(ols_coef_table(lr_full), use_container_width=True, hide_index=True)
    elif selected_for_coef == MODEL_ARIMA:
        st.markdown("**Параметры ARIMA**")
        st.dataframe(arima_param_table(arima_full), use_container_width=True, hide_index=True)
    elif selected_for_coef == MODEL_EXT:
        st.markdown("**Коэффициенты модели расширенного режима**")
        st.dataframe(ols_coef_table(regime_full), use_container_width=True, hide_index=True)
    else:
        st.markdown("**Базовая часть гибридной модели: коэффициенты расширенного режима**")
        st.dataframe(ols_coef_table(regime_full), use_container_width=True, hide_index=True)
        st.markdown("**Нейросетевая часть: веса MLP-корректора остатков**")
        st.dataframe(mlp_weights_table(mlp_full, regime_cols), use_container_width=True, hide_index=True)
        st.markdown("**RSS/NLP-параметры финальной поправки**")
        rss_params_df = pd.DataFrame([
            {"Параметр": "rss_sentiment", "Значение": rss_avg},
            {"Параметр": "rss_signal_scale", "Значение": RSS_SIGNAL_SCALE},
            {"Параметр": "mlp_error_std", "Значение": mlp_error_std},
            {"Параметр": "walk_forward_steps", "Значение": len(hybrid_walk_df)},
        ])
        st.dataframe(rss_params_df, use_container_width=True, hide_index=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='font-size:0.78rem; color:#ADB5BD;'>© 2026 Forecast Engine · дипломная модель</div>", unsafe_allow_html=True)
