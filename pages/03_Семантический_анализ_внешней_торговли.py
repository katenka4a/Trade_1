"""
Семантический анализ внешнеэкономических связей — текущий RSS/NLP анализ новостного фона.

Логика страницы:
1. RSS-ленты используются только для текущей краткосрочной картины, так как RSS хранит новости ограниченное время.
2. На странице отображаются около 10 значимых новостей из открытых источников.
3. Для анализа выводятся динамика тональности инфополя, распределение по категориям и «новости недели».
"""

import os
import sys
import re
import html
from datetime import datetime, timedelta
from urllib.parse import quote_plus

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

st.set_page_config(page_title="Семантический анализ внешнеэкономических связей", page_icon=None, layout="wide")

from utils import setup_i18n, render_lang_switcher, L
setup_i18n()

try:
    from data.locales import install_streamlit_i18n, translate_text as TT
    install_streamlit_i18n(st)
except Exception:
    def TT(value):
        return value

st.markdown("""
<style>
html, body, [class*="css"] { font-family: 'Inter', sans-serif; color: #212529; }
h1, h2, h3 { font-family: 'Source Sans Pro', 'Inter', sans-serif; font-weight: 600; letter-spacing: -0.01em; color: #1a1a2e; }
.section-box { background: #FFFFFF; border-radius: 8px; padding: 1.25rem; border: 1px solid #E9ECEF; margin-bottom: 1rem; }
.news-card { background:#FFFFFF; border:1px solid #E9ECEF; border-radius:8px; padding:1rem; margin-bottom:0.75rem; }
.news-title { font-weight:600; color:#1a1a2e; margin-bottom:0.35rem; }
.news-meta { font-size:0.78rem; color:#6C757D; margin-bottom:0.4rem; }
.news-text { font-size:0.88rem; color:#343A40; }
.small-muted { font-size:0.82rem; color:#6C757D; }
.badge { display:inline-block; padding:0.15rem 0.45rem; border-radius:999px; background:#F1F3F5; color:#495057; font-size:0.75rem; margin-left:0.25rem; }
</style>
""", unsafe_allow_html=True)

lang_col1, lang_col2 = st.columns([6, 1])
with lang_col2:
    render_lang_switcher()

st.markdown(f"""
<div style="margin-bottom:1.5rem;">
    <div style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.08em; color:#6C757D; margin-bottom:0.25rem;">{"Methodology" if L("nlp_tab_method")=="Methodology" else "Методология"}</div>
    <h1 style="margin:0;">Семантический анализ внешнеэкономических связей</h1>
    <p style="color:#6C757D; margin-top:0.25rem;">{L("nlp_subtitle")}</p>
</div>
""", unsafe_allow_html=True)

from data.diploma_data import nlp_rss_results, nlp_gdelt_sentiment

# -----------------------------------------------------------------------------
# Настройки текущего RSS-анализа
# -----------------------------------------------------------------------------
PAIR_CONFIG = {
    "Россия-Китай": {
        "label": "Россия—Китай",
        "queries": [
            "Russia China trade",
            "Russia China economic cooperation",
            "Sino Russian trade",
            "Россия Китай торговля",
            "Россия Китай экономическое сотрудничество",
            "Russia China sanctions trade payments logistics",
        ],
        "keywords": [
            "russia", "china", "россия", "китай", "trade", "торговля",
            "economic", "cooperation", "поставки", "экспорт", "импорт", "санкции",
            "energy", "oil", "gas", "юань", "settlement", "payments", "logistics",
        ],
    },
    "Россия-Индия": {
        "label": "Россия—Индия",
        "queries": [
            "Russia India trade",
            "Russia India economic cooperation",
            "Russia India oil trade",
            "Россия Индия торговля",
            "Россия Индия экономическое сотрудничество",
            "Russia India sanctions trade rupee payments logistics",
        ],
        "keywords": [
            "russia", "india", "россия", "индия", "trade", "торговля",
            "economic", "cooperation", "поставки", "экспорт", "импорт", "санкции",
            "oil", "payments", "rupee", "рупия", "settlement", "logistics",
        ],
    },
    "Индия-Китай": {
        "label": "Индия—Китай",
        "queries": [
            "India China trade",
            "China India economic relations",
            "Sino Indian trade",
            "Индия Китай торговля",
            "India China trade tariffs supply chain",
        ],
        "keywords": [
            "india", "china", "индия", "китай", "trade", "торговля",
            "imports", "exports", "economic", "border", "tariffs", "supply chain",
        ],
    },
}

SIGNAL_WORDS = {
    # Базовые слова релевантности: они не всегда задают знак тональности, но показывают связь с торговлей.
    "санкции", "sanctions", "платеж", "платёж", "payments", "settlement", "расчеты", "расчёты",
    "контракт", "contract", "deal", "agreement", "поставки", "supply", "exports", "export", "imports", "import",
    "oil", "gas", "energy", "логистика", "logistics", "shipping", "tariff", "тариф", "freight",
    "restriction", "restrictions", "ограничения", "ban", "cooperation", "сотрудничество", "growth", "record",
    "corridor", "маршрут", "route", "порт", "port", "railway", "железнодорож", "pipeline", "трубопровод",
    "rupee", "рупия", "yuan", "юань", "national currencies", "нацвалют", "brent", "bdi",
}

# Доменный словарь: усиливает тональность именно в экономико-торговом контексте.
# Это не отдельная модель «торгового сигнала», а более жесткая настройка анализа тональности под тему диплома.
POSITIVE_DOMAIN_WORDS = {
    "growth": 2.0, "increase": 1.7, "increased": 1.7, "expand": 1.6, "expansion": 1.6,
    "surge": 2.0, "boost": 1.8, "record": 2.2, "record high": 2.5, "rise": 1.2,
    "cooperation": 1.4, "partnership": 1.5, "agreement": 1.8, "deal": 1.8, "contract": 1.8,
    "memorandum": 1.3, "signed": 1.6, "launch": 1.5, "new route": 1.7, "corridor": 1.4,
    "capacity": 1.2, "supplies rose": 2.0, "exports rose": 2.0, "imports rose": 1.8,
    "расшир": 1.6, "рост": 1.8, "увелич": 1.7, "вырос": 1.8, "нараст": 1.8,
    "рекорд": 2.3, "соглашение": 1.8, "договор": 1.8, "контракт": 1.8, "подпис": 1.6,
    "сотрудничество": 1.4, "партнерство": 1.4, "партнёрство": 1.4, "запуск": 1.5,
    "новый маршрут": 1.7, "коридор": 1.4, "мтк": 1.4, "север-юг": 1.6,
    "расчеты в нацвалютах": 1.6, "расчёты в нацвалютах": 1.6, "национальных валютах": 1.5,
}

NEGATIVE_DOMAIN_WORDS = {
    "sanctions": 1.5, "secondary sanctions": 2.6, "restrictions": 1.8, "restriction": 1.8,
    "export controls": 2.4, "blacklist": 2.4, "ban": 2.0, "blocked": 2.2, "block": 1.8,
    "payment issues": 2.5, "settlement issues": 2.4, "blocked payments": 2.8,
    "delay": 1.7, "delays": 1.7, "disruption": 2.1, "disruptions": 2.1,
    "congestion": 1.6, "bottleneck": 2.0, "freight rise": 1.8, "shipping costs": 1.5,
    "decline": 2.0, "drop": 2.0, "fall": 1.8, "fell": 1.8, "reduce": 1.6, "reduced": 1.6,
    "slowdown": 1.8, "decrease": 1.8, "tensions": 1.8, "conflict": 2.0, "crisis": 2.1,
    "pressure": 1.4, "risk": 1.3, "uncertainty": 1.5, "tariff hike": 1.7,
    "санкции": 1.5, "вторичные санкции": 2.6, "ограничения": 1.8, "запрет": 2.0,
    "блокиров": 2.2, "зависшие платежи": 2.8, "проблемы с расчетами": 2.5, "проблемы с расчётами": 2.5,
    "неплатеж": 2.2, "неплатёж": 2.2, "задерж": 1.7, "сбой": 2.0, "сбои": 2.0,
    "дефицит контейнеров": 1.8, "рост фрахта": 1.8, "логистические ограничения": 2.0,
    "снижение": 1.9, "падение": 2.0, "сокращ": 1.8, "спад": 1.8, "просад": 1.8,
    "напряженность": 1.8, "напряжённость": 1.8, "конфликт": 2.0, "кризис": 2.1,
    "риск": 1.3, "неопределенность": 1.5, "неопределённость": 1.5,
}

HIGH_IMPACT_POSITIVE = {
    "record", "record high", "agreement", "deal", "contract", "signed", "launch", "new route",
    "рекорд", "соглашение", "контракт", "подпис", "запуск", "новый маршрут", "мтк", "север-юг",
}

HIGH_IMPACT_NEGATIVE = {
    "secondary sanctions", "export controls", "blacklist", "ban", "blocked payments", "payment issues",
    "settlement issues", "disruption", "bottleneck", "crisis", "conflict",
    "вторичные санкции", "экспортный контроль", "черный список", "чёрный список", "запрет",
    "зависшие платежи", "проблемы с расчетами", "проблемы с расчётами", "сбой", "кризис", "конфликт",
}

def safe_key(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_]+", "_", str(value)).strip("_")

def clean_html(text: str) -> str:
    text = html.unescape(str(text or ""))
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def parse_entry_date(entry) -> datetime:
    for key in ("published_parsed", "updated_parsed"):
        parsed = entry.get(key)
        if parsed:
            return datetime(*parsed[:6])
    for key in ("published", "updated"):
        value = entry.get(key)
        if value:
            try:
                parsed = pd.to_datetime(value, errors="coerce")
                if pd.notna(parsed):
                    return parsed.to_pydatetime().replace(tzinfo=None)
            except Exception:
                pass
    return datetime.now()

def _textblob_sentiment(text: str) -> float:
    """Базовая языковая тональность. Используется только как часть гибридного индекса."""
    try:
        from textblob import TextBlob
        if len(str(text).strip()) < 10:
            return 0.0
        return float(TextBlob(str(text)).sentiment.polarity)
    except Exception:
        return 0.0

def _weighted_hits(text_l: str, dictionary: dict[str, float]) -> float:
    return float(sum(weight for word, weight in dictionary.items() if word.lower() in text_l))

def domain_sentiment_score(text: str) -> float:
    """Доменная корректировка тональности по словарю экономических и геополитических маркеров."""
    text_l = str(text or "").lower()
    pos = _weighted_hits(text_l, POSITIVE_DOMAIN_WORDS)
    neg = _weighted_hits(text_l, NEGATIVE_DOMAIN_WORDS)
    if pos == 0 and neg == 0:
        return 0.0
    return float(np.clip((pos - neg) / (pos + neg), -1.0, 1.0))

def event_importance_weight(text: str) -> float:
    """Вес новости по важности события: важные контракты/шоки сильнее влияют на значимость материала."""
    text_l = str(text or "").lower()
    pos_impact = sum(1 for word in HIGH_IMPACT_POSITIVE if word.lower() in text_l)
    neg_impact = sum(1 for word in HIGH_IMPACT_NEGATIVE if word.lower() in text_l)
    impact = pos_impact + neg_impact
    if impact >= 3:
        return 2.0
    if impact == 2:
        return 1.7
    if impact == 1:
        return 1.35
    return 1.0

def analyze_sentiment(text: str) -> float:
    """Гибридная тональность: TextBlob + доменный словарь. Границы стали жестче, а слабые сигналы не раздуваются."""
    text = str(text or "")
    if len(text.strip()) < 10:
        return 0.0
    base = _textblob_sentiment(text)
    domain = domain_sentiment_score(text)
    score = 0.4 * base + 0.6 * domain
    return float(np.clip(score, -1.0, 1.0))

def classify_sentiment(value: float) -> str:
    # Более жесткие границы: слабые значения остаются нейтральными, сильные новости выделяются увереннее.
    if value >= 0.35:
        return "Сильно позитивные"
    if value >= 0.15:
        return "Умеренно позитивные"
    if value <= -0.35:
        return "Сильно негативные"
    if value <= -0.15:
        return "Умеренно негативные"
    return "Нейтральные"

def relevance_score(text: str, keywords: list[str]) -> int:
    text_l = str(text).lower()
    keyword_hits = sum(1 for word in keywords if word.lower() in text_l)
    signal_hits = sum(1 for word in SIGNAL_WORDS if word.lower() in text_l)
    domain_hits = sum(1 for word in POSITIVE_DOMAIN_WORDS if word.lower() in text_l) + sum(1 for word in NEGATIVE_DOMAIN_WORDS if word.lower() in text_l)
    return int(keyword_hits + signal_hits * 2 + domain_hits * 2)

def build_google_rss_urls(pair_key: str) -> list[str]:
    """Формирует RSS-ссылки Google News для текущей краткосрочной картины."""
    urls = []
    cfg = PAIR_CONFIG[pair_key]
    for query in cfg["queries"]:
        lang = "ru" if any("а" <= ch.lower() <= "я" for ch in query) else "en"
        gl = "RU" if lang == "ru" else "US"
        ceid = "RU:ru" if lang == "ru" else "US:en"
        q = quote_plus(query)
        urls.append(f"https://news.google.com/rss/search?q={q}&hl={lang}&gl={gl}&ceid={ceid}")
    return urls

@st.cache_data(ttl=30 * 60, show_spinner=False)
def fetch_rss_articles(pair_key: str, max_per_feed: int = 30, target_articles: int = 10) -> pd.DataFrame:
    """Собирает текущие RSS-новости по паре. На выходе оставляет около 10 наиболее значимых материалов."""
    try:
        import feedparser
    except Exception:
        return pd.DataFrame(columns=["title", "text", "link", "source", "date", "sentiment", "sentiment_label", "relevance", "significance", "event_weight"])

    cfg = PAIR_CONFIG[pair_key]
    rows = []
    seen = set()

    for url in build_google_rss_urls(pair_key):
        try:
            feed = feedparser.parse(url)
        except Exception:
            continue

        for entry in feed.entries[:max_per_feed]:
            title = clean_html(entry.get("title", ""))
            summary = clean_html(entry.get("summary", ""))
            link = entry.get("link", "")
            date = parse_entry_date(entry)
            text = f"{title} {summary}".strip()
            text_l = text.lower()

            if not any(keyword.lower() in text_l for keyword in cfg["keywords"]):
                continue

            dedup_key = (title[:120].lower(), link[:120])
            if dedup_key in seen:
                continue
            seen.add(dedup_key)

            sentiment = analyze_sentiment(text)
            rel = relevance_score(text, cfg["keywords"])
            event_weight = event_importance_weight(text)
            significance = rel * (1 + abs(sentiment) * 2) * event_weight
            source_raw = entry.get("source", {})
            source_title = clean_html(source_raw.get("title", "Google News")) if isinstance(source_raw, dict) else "Google News"

            rows.append({
                "title": title,
                "text": text[:500],
                "link": link,
                "source": source_title,
                "date": date,
                "sentiment": sentiment,
                "sentiment_label": classify_sentiment(sentiment),
                "relevance": rel,
                "significance": significance,
                "event_weight": event_weight,
            })

    df = pd.DataFrame(rows)
    if len(df) == 0:
        return pd.DataFrame(columns=["title", "text", "link", "source", "date", "sentiment", "sentiment_label", "relevance", "significance", "event_weight"])

    # Сначала берём наиболее значимые материалы, затем выводим их в хронологии для графика.
    df = df.sort_values(["significance", "date"], ascending=[False, False]).head(target_articles).copy()
    return df.sort_values("date").reset_index(drop=True)

def normalize_rss_dataframe(df: pd.DataFrame, pair_key: str) -> pd.DataFrame:
    """Приводит результат дипломного RSSSentimentAnalyzer к единому формату."""
    if df is None or len(df) == 0:
        return pd.DataFrame(columns=["title", "text", "link", "source", "date", "sentiment", "sentiment_label", "relevance", "significance", "event_weight"])

    out = df.copy()
    if "sentiment" not in out.columns and "polarity" in out.columns:
        out["sentiment"] = out["polarity"]
    if "sentiment" not in out.columns:
        out["sentiment"] = 0.0
    if "title" not in out.columns:
        out["title"] = "Без заголовка"
    if "text" not in out.columns:
        out["text"] = out["title"].astype(str)
    if "date" not in out.columns:
        out["date"] = datetime.now()
    out["date"] = pd.to_datetime(out["date"], errors="coerce").fillna(pd.Timestamp.now()).dt.to_pydatetime()
    if "sentiment_label" not in out.columns:
        out["sentiment_label"] = out["sentiment"].astype(float).apply(classify_sentiment)
    if "relevance" not in out.columns:
        out["relevance"] = out["text"].apply(lambda x: relevance_score(x, PAIR_CONFIG[pair_key]["keywords"]))
    if "significance" not in out.columns:
        out["event_weight"] = out["text"].apply(event_importance_weight)
        out["significance"] = out["relevance"] * (1 + out["sentiment"].astype(float).abs() * 2) * out["event_weight"]
    if "source" not in out.columns:
        out["source"] = "RSS"
    if "link" not in out.columns:
        out["link"] = ""

    out = out.sort_values(["significance", "date"], ascending=[False, False]).head(10)
    return out.sort_values("date").reset_index(drop=True)

def summarize_articles(df: pd.DataFrame) -> dict:
    if df is None or len(df) == 0:
        return {
            "total_articles": 0,
            "average_polarity": 0.0,
            "nlp_adjustment": 0.0,
            "top_week": None,
            "category_counts": pd.Series(dtype=float),
        }

    avg = float(df["sentiment"].astype(float).mean())
    adjustment = avg * 20
    week_start = datetime.now() - timedelta(days=7)
    df_week = df[pd.to_datetime(df["date"], errors="coerce") >= week_start]
    top_week_df = df_week.sort_values(["significance", "date"], ascending=[False, False]) if len(df_week) > 0 else df.sort_values(["significance", "date"], ascending=[False, False])

    return {
        "total_articles": int(len(df)),
        "average_polarity": avg,
        "nlp_adjustment": adjustment,
        "top_week": top_week_df.iloc[0].to_dict() if len(top_week_df) > 0 else None,
        "category_counts": df["sentiment_label"].value_counts(),
    }

def render_news_card(news: dict | None, title: str):
    st.markdown(f"<div class='news-card'><div class='news-title'>{title}</div>", unsafe_allow_html=True)
    if not news:
        st.markdown("<div class='small-muted'>Подходящая новость не найдена.</div></div>", unsafe_allow_html=True)
        return

    news_title = clean_html(news.get("title", "Без заголовка"))
    date = news.get("date")
    if not isinstance(date, datetime):
        try:
            date = pd.to_datetime(date, errors="coerce").to_pydatetime()
        except Exception:
            date = None
    date_str = date.strftime("%d.%m.%Y") if isinstance(date, datetime) else "—"
    sentiment = float(news.get("sentiment", 0.0))
    category = classify_sentiment(sentiment)
    source = clean_html(news.get("source", "RSS"))
    link = news.get("link", "")
    text = clean_html(news.get("text", ""))

    link_html = f"<a href='{link}' target='_blank'>Открыть источник</a>" if link else ""
    st.markdown(
        f"<div class='news-title'>{news_title}</div>"
        f"<div class='news-meta'>{date_str} · {source} · тональность: {sentiment:+.3f} "
        f"<span class='badge'>{category}</span> · {link_html}</div>"
        f"<div class='news-text'>{text[:320]}</div></div>",
        unsafe_allow_html=True,
    )

def render_sentiment_dynamics(df: pd.DataFrame, key: str):
    plot_df = df.copy().reset_index(drop=True)
    plot_df["date_label"] = pd.to_datetime(plot_df["date"], errors="coerce").dt.strftime("%d.%m")
    plot_df["x"] = np.arange(1, len(plot_df) + 1)
    y = plot_df["sentiment"].astype(float)
    y_min = min(float(y.min()) - 0.03, -0.2)
    y_max = max(float(y.max()) + 0.03, 0.2)

    fig = go.Figure()
    fig.add_hrect(y0=0, y1=y_max, fillcolor="rgba(106, 154, 123, 0.18)", line_width=0, annotation_text="Позитивная зона", annotation_position="top left")
    fig.add_hrect(y0=y_min, y1=0, fillcolor="rgba(217, 83, 79, 0.18)", line_width=0, annotation_text="Негативная зона", annotation_position="bottom left")
    fig.add_trace(go.Scatter(
        x=plot_df["x"],
        y=y,
        mode="lines+markers+text",
        text=plot_df["date_label"],
        textposition="top center",
        line=dict(width=2.5, color="#2D3A2D"),
        marker=dict(size=9, color="#FFFFFF", line=dict(width=2, color="#2D3A2D")),
        name="Индекс тональности",
        hovertemplate="Дата: %{text}<br>Индекс: %{y:+.3f}<extra></extra>",
    ))
    fig.add_hline(y=0, line_width=1, line_color="gray")
    fig.update_layout(
        title="Динамика тональности инфополя",
        height=380,
        template="plotly_white",
        margin=dict(l=20, r=20, t=45, b=20),
        yaxis=dict(title="Индекс тональности", range=[y_min, y_max]),
        xaxis=dict(title="Значимые новости RSS", showticklabels=False),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    )
    st.plotly_chart(fig, use_container_width=True, key=f"sentiment_dynamics_{key}")

def render_sentiment_pie(df: pd.DataFrame, key: str):
    order = ["Сильно позитивные", "Умеренно позитивные", "Нейтральные", "Умеренно негативные", "Сильно негативные"]
    counts = df["sentiment_label"].value_counts()
    labels = [label for label in order if counts.get(label, 0) > 0]
    values = [int(counts.get(label, 0)) for label in labels]

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0,
        textinfo="percent+label",
        sort=False,
    )])
    fig.update_layout(
        title="Распределение по категориям",
        height=380,
        template="plotly_white",
        margin=dict(l=20, r=20, t=45, b=20),
        showlegend=False,
    )
    st.plotly_chart(fig, use_container_width=True, key=f"sentiment_pie_{key}")

def get_current_rss_dataset(pair_key: str) -> pd.DataFrame:
    """Пробует дипломный RSSSentimentAnalyzer, затем добирает новости из Google News RSS до ~10 материалов."""
    base_df = pd.DataFrame()
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
        from modules.rss_nlp import RSSSentimentAnalyzer
        analyzer = RSSSentimentAnalyzer(pair_key)
        df_raw, _summary = analyzer.run()
        base_df = normalize_rss_dataframe(df_raw, pair_key)
    except Exception:
        base_df = pd.DataFrame()

    supplement_df = fetch_rss_articles(pair_key, max_per_feed=35, target_articles=10)

    if len(base_df) == 0:
        return supplement_df

    combined = pd.concat([base_df, supplement_df], ignore_index=True)
    if len(combined) == 0:
        return combined

    combined["dedup"] = combined["title"].astype(str).str.lower().str[:120]
    combined = combined.drop_duplicates("dedup").drop(columns=["dedup"])
    combined = combined.sort_values(["significance", "date"], ascending=[False, False]).head(10)
    return combined.sort_values("date").reset_index(drop=True)

def render_live_pair_block(pair_key: str):
    safe_pair = safe_key(pair_key)
    st.markdown(f"<h3 style='font-size:1.05rem;'>{PAIR_CONFIG[pair_key]['label']}</h3>", unsafe_allow_html=True)
    st.caption("RSS-ленты дают краткосрочную картину, поэтому блок показывает только текущую выгрузку и новости недели.")

    live_df = get_current_rss_dataset(pair_key)
    summary = summarize_articles(live_df)

    c1, c2, c3 = st.columns(3)
    c1.metric("Значимых новостей", summary["total_articles"])
    c2.metric(L("nlp_avg_polarity"), f"{summary['average_polarity']:+.4f}")
    c3.metric(L("nlp_adjust"), f"{summary['nlp_adjustment']:+.2f}%")

    if len(live_df) == 0:
        st.info("RSS-ленты не вернули релевантные новости по этой паре. Модель продолжит работу с нейтральным значением индекса.")
        return

    chart_col1, chart_col2 = st.columns([1.15, 1])
    with chart_col1:
        render_sentiment_dynamics(live_df, safe_pair)
    with chart_col2:
        render_sentiment_pie(live_df, safe_pair)

    render_news_card(summary["top_week"], "Новость недели")

    st.markdown("#### Значимые новости, использованные в RSS-анализе")
    table_df = live_df.sort_values(["significance", "date"], ascending=[False, False]).copy()
    table_df = table_df[["date", "title", "sentiment_label", "sentiment", "relevance", "significance", "source"]].head(10)
    table_df["date"] = pd.to_datetime(table_df["date"], errors="coerce").dt.strftime("%d.%m.%Y")
    table_df["sentiment"] = table_df["sentiment"].astype(float).map(lambda x: f"{x:+.3f}")
    table_df["significance"] = table_df["significance"].astype(float).map(lambda x: f"{x:.2f}")
    table_df.columns = ["Дата", "Заголовок", "Категория", "Тональность", "Релевантность", "Значимость", "Источник"]
    st.dataframe(table_df, use_container_width=True, hide_index=True, key=f"rss_significant_table_{safe_pair}")

tab1, tab2, tab3 = st.tabs([L("nlp_tab_method"), L("nlp_tab_rss"), L("nlp_tab_results")])

with tab1:
    st.markdown(f"""
    <div class="section-box">
    <p>{L("nlp_sentiment_desc")}</p>
    <ul>
        <li>{L("nlp_textblob")}</li>
        <li>{L("nlp_deepseek")}</li>
        <li>{L("nlp_rss_agg")}</li>
    </ul>
    <p style="margin-bottom:0;">{L("nlp_adjustment")}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-box">
    <b>Как читается RSS-анализ</b><br>
    RSS-блок отражает текущую краткосрочную новостную картину: ленты часто хранят материалы ограниченное время,
    поэтому помесячная ретроспектива здесь не строится. Страница загружает около 10 значимых новостей из открытых RSS-источников,
    оценивает их тональность по гибридной схеме TextBlob + доменный словарь, показывает динамику инфополя и отдельно выделяет «новость недели» — материал с наибольшей значимостью
    для выбранного торгового направления.
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown(f"<h3>{L('nlp_tab_rss')}</h3>", unsafe_allow_html=True)

    pair_choice = st.selectbox(
        "Направление RSS-анализа",
        list(PAIR_CONFIG.keys()),
        format_func=lambda x: PAIR_CONFIG[x]["label"],
        key="rss_pair_choice_current",
    )

    if st.button(L("nlp_load_btn"), key="load_current_rss"):
        with st.spinner(L("loading_spinner")):
            try:
                render_live_pair_block(pair_choice)
            except Exception as e:
                st.error(f"{L('error_occurred')}: {e}")
    else:
        st.markdown(
            f'<div style="background:#FFFFFF; border:1px solid #E9ECEF; border-radius:8px; padding:1rem; color:#6C757D;">{L("nlp_no_data")}</div>',
            unsafe_allow_html=True,
        )

with tab3:
    st.markdown(f"<h3>{L('nlp_distribution_title')}</h3>", unsafe_allow_html=True)
    rss_data = []
    for pair_key, pair_label in [("Россия-Китай", L("ru_cn")), ("Россия-Индия", L("ru_in")), ("Китай-Индия", L("cn_in"))]:
        rss_data.append({
            "Pair": pair_label,
            L("neutral"): nlp_rss_results[(pair_key, "Нейтральные")],
            L("positive"): nlp_rss_results[(pair_key, "Позитивные")],
            L("negative"): nlp_rss_results[(pair_key, "Негативные")],
        })
    rss_df = pd.DataFrame(rss_data)
    st.dataframe(rss_df, use_container_width=True, hide_index=True)

    fig = go.Figure()
    for col_name, color in [(L("positive"), "#6A9A7B"), (L("neutral"), "#B0D4B8"), (L("negative"), "#D9534F")]:
        fig.add_trace(go.Bar(name=col_name, x=rss_df["Pair"], y=rss_df[col_name], marker_color=color))
    fig.update_layout(barmode="group", height=350, template="plotly_white", margin=dict(l=20, r=20, t=30, b=20), yaxis=dict(title="%"))
    st.plotly_chart(fig, use_container_width=True, key="nlp_static_rss_bar")

    st.markdown(f"<h3>{L('nlp_gdelt_title')}</h3>", unsafe_allow_html=True)
    gdelt_data = pd.DataFrame([{"Pair": k, "Index": v} for k, v in nlp_gdelt_sentiment.items()])
    colors = ["#D9534F" if v < 0 else "#6A9A7B" for v in nlp_gdelt_sentiment.values()]
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        x=gdelt_data["Pair"],
        y=gdelt_data["Index"],
        marker_color=colors,
        text=gdelt_data["Index"].apply(lambda x: f"{x:+.3f}"),
        textposition="outside",
    ))
    fig2.add_hline(y=0, line_dash="dash", line_color="gray")
    fig2.update_layout(height=350, template="plotly_white", margin=dict(l=20, r=20, t=20, b=20))
    st.plotly_chart(fig2, use_container_width=True, key="nlp_gdelt_bar")
    st.markdown(f'<div class="section-box" style="font-size:0.88rem;">{L("nlp_ru_cn_comment")}<br>{L("nlp_ru_in_comment")}<br>{L("nlp_cn_in_comment")}</div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"<div style='font-size:0.78rem; color:#ADB5BD;'>&copy; 2026 {L('footer_copyright')}</div>", unsafe_allow_html=True)
