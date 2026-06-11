"""
Статистический анализ внешней торговли — пояснительная версия страницы.
"""
import streamlit as st
import html
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

try:
    from data.locales import get_text as _GT
except Exception:
    def _GT(key: str, lang=None) -> str:
        return "Статистический анализ внешней торговли" if key == "stats04_page_title" else key

st.set_page_config(page_title=_GT("stats04_page_title"), page_icon=None, layout="wide")
from utils import setup_i18n, render_lang_switcher, L
setup_i18n()

try:
    from data.locales import install_streamlit_i18n, translate_text as TT, get_text as GT
    install_streamlit_i18n(st)
except Exception:
    def TT(value):
        return value
    def GT(key: str, lang=None):
        return key

from data.diploma_data import (
    df_ru_cn,
    df_ru_in,
    ru_export_to_cn_structure,
    ru_import_from_cn_structure,
    ru_export_to_in_structure,
    ru_import_from_in_structure,
    export_partners_2000,
    export_partners_2023,
    structural_indices,
    coverage_df,
)

st.markdown("""
<style>
html, body, [class*="css"] { font-family:'Inter',sans-serif; color:#20242A; }
.stApp { background:#FFFFFF; }
h1, h2, h3 { font-family:'Source Sans Pro','Inter',sans-serif; font-weight:700; letter-spacing:-0.02em; color:#121826; }
.hero {
    background: radial-gradient(circle at 8% 10%, rgba(74,124,247,0.14), transparent 26%),
                radial-gradient(circle at 94% 8%, rgba(232,168,56,0.16), transparent 28%),
                linear-gradient(135deg,#F8FBFF 0%,#FFFFFF 55%,#F8FAF6 100%);
    border:1px solid #E2E8F0; border-radius:22px; padding:1.35rem 1.55rem; margin-bottom:1.05rem;
    box-shadow:0 12px 30px rgba(15,23,42,0.045);
}
.kicker { font-size:0.75rem; text-transform:uppercase; letter-spacing:0.10em; color:#64748B; font-weight:800; margin-bottom:0.35rem; }
.hero-title { font-size:2.25rem; line-height:1.05; margin:0; color:#121826; }
.hero-subtitle { color:#52606D; margin-top:0.55rem; max-width:1120px; font-size:1rem; line-height:1.58; }
.metric-card, .explain-card, .method-card, .insight-card, .goods-card {
    background:#FFFFFF; border:1px solid #E5EAF0; border-radius:16px; padding:1rem 1.1rem;
    box-shadow:0 8px 22px rgba(15,23,42,0.035); margin-bottom:0.8rem;
}
.metric-label { color:#64748B; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.08em; font-weight:800; margin-bottom:0.42rem; }
.metric-value { color:#121826; font-size:1.62rem; font-weight:850; line-height:1.05; margin-bottom:0.3rem; }
.metric-note { color:#52606D; font-size:0.86rem; line-height:1.4; }
.explain-title { font-weight:820; color:#121826; margin-bottom:0.28rem; font-size:0.98rem; }
.explain-text { color:#52606D; font-size:0.90rem; line-height:1.52; }
.method-card { background:#F8FAFC; border-left:5px solid #4A7CF7; }
.insight-card { background:#F7FBF8; border-left:5px solid #6A9A7B; }
.warn-card { background:#FFF8E8; border:1px solid #EED99B; border-left:5px solid #E8A838; border-radius:16px; padding:1rem 1.1rem; margin-bottom:0.8rem; color:#52606D; line-height:1.52; }
.goods-title { font-weight:820; color:#121826; margin-bottom:0.35rem; }
.goods-text { color:#52606D; font-size:0.88rem; line-height:1.48; }
.pill { display:inline-block; border:1px solid #E2E8F0; background:#F8FAFC; color:#475569; border-radius:999px; padding:0.16rem 0.5rem; font-size:0.74rem; font-weight:750; margin:0.1rem 0.16rem 0.1rem 0; }
.key { color:#121826; font-weight:820; }
.small-muted { color:#7B8794; font-size:0.82rem; line-height:1.48; }
.product-reference-box {
    background:linear-gradient(180deg,#FFFFFF 0%,#FBFCFE 100%); border:1px solid #E5EAF0; border-radius:18px;
    padding:1.05rem 1.1rem; box-shadow:0 10px 26px rgba(15,23,42,0.035); margin:0.7rem 0 1.05rem 0;
}
.product-reference-note { color:#64748B; font-size:0.84rem; line-height:1.48; margin:0.15rem 0 0.85rem 0; max-width:1120px; }
.company-note { background:#F8FAFC; border:1px solid #E5EAF0; border-left:5px solid #94A3B8; border-radius:16px; padding:0.95rem 1.05rem; color:#52606D; font-size:0.88rem; line-height:1.55; margin-bottom:0.9rem; }
.company-section-title { color:#121826; font-size:1.12rem; font-weight:850; margin:1.0rem 0 0.45rem 0; }
.company-section-subtitle { color:#64748B; font-size:0.86rem; line-height:1.48; margin:-0.1rem 0 0.75rem 0; }
.reference-card {
    background:#FFFFFF; border:1px solid #E6ECF2; border-left:5px solid var(--accent); border-radius:15px;
    padding:0.92rem 1rem; margin-bottom:0.72rem; box-shadow:0 5px 16px rgba(15,23,42,0.028);
}
.reference-top { display:flex; justify-content:space-between; gap:1rem; align-items:flex-start; margin-bottom:0.62rem; }
.reference-title { color:#121826; font-weight:850; font-size:1.02rem; line-height:1.24; }
.reference-meta { color:#64748B; font-size:0.84rem; margin-top:0.14rem; }
.reference-tag { flex:0 0 auto; border:1px solid #D8E0EA; background:#F8FAFC; color:#475569; border-radius:999px; padding:0.22rem 0.55rem; font-size:0.70rem; font-weight:850; letter-spacing:0.05em; }
.reference-grid { display:grid; grid-template-columns:1.25fr 1.15fr 1.25fr; gap:0.72rem; }
.reference-field { background:#F8FAFC; border:1px solid #EEF2F6; border-radius:12px; padding:0.72rem 0.78rem; }
.reference-label { color:#7B8794; font-size:0.69rem; text-transform:uppercase; letter-spacing:0.08em; font-weight:850; margin-bottom:0.28rem; }
.reference-text { color:#334155; font-size:0.84rem; line-height:1.43; }
.subsection-title { font-size:1.05rem; font-weight:800; color:#121826; margin:0.25rem 0 0.5rem 0; }
@media (max-width: 1000px) { .reference-grid { grid-template-columns:1fr; } .reference-top { display:block; } .reference-tag { display:inline-block; margin-top:0.4rem; } }
.stTabs [data-baseweb="tab-list"] { gap:0.45rem; border-bottom:1px solid #E5EAF0; }
.stTabs [data-baseweb="tab"] { border:1px solid #E5EAF0; border-bottom:none; border-radius:12px 12px 0 0; padding:0.75rem 1rem; }
.stTabs [aria-selected="true"] { background:#F8FAFC; color:#121826; font-weight:800; }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# -----------------------------------------------------------------------------
PLOT_LAYOUT = dict(
    template="plotly_white",
    height=410,
    margin=dict(l=20, r=20, t=50, b=26),
    font=dict(family="Inter", size=11),
    hoverlabel=dict(bgcolor="white", font_size=12, font_family="Inter"),
)

def money_bln(value: float) -> str:
    try:
        return f"{value:,.1f} млрд $".replace(",", " ").replace(".", ",")
    except Exception:
        return "—"

def pct(value: float) -> str:
    try:
        return f"{value:.1f}%".replace(".", ",")
    except Exception:
        return "—"

def ratio(value: float) -> str:
    try:
        return f"{value:.2f}x".replace(".", ",")
    except Exception:
        return "—"

def times(value: float) -> str:
    try:
        try:
            from data.locales import get_current_lang as _get_current_lang
            if _get_current_lang() == "en":
                return f"{value:,.1f} times"
        except Exception:
            pass
        return f"в {value:,.1f} раза".replace(",", " ").replace(".", ",")
    except Exception:
        return "—"

def metric_card(label: str, value: str, note: str) -> None:
    st.markdown(f"""
    <div class="metric-card">
      <div class="metric-label">{label}</div>
      <div class="metric-value">{value}</div>
      <div class="metric-note">{note}</div>
    </div>
    """, unsafe_allow_html=True)

def explain(title: str, text: str, kind: str = "explain") -> None:
    css = "method-card" if kind == "method" else "insight-card" if kind == "insight" else "explain-card"
    st.markdown(f"""
    <div class="{css}">
      <div class="explain-title">{title}</div>
      <div class="explain-text">{text}</div>
    </div>
    """, unsafe_allow_html=True)

def year_row(df: pd.DataFrame, year: int) -> pd.Series:
    if year in set(df["Год"].astype(int)):
        return df[df["Год"].astype(int) == year].iloc[-1]
    return df.sort_values("Год").iloc[-1]

def get_col(df: pd.DataFrame, candidates: list[str]) -> str:
    for col in candidates:
        if col in df.columns:
            return col
    return candidates[0]

def structure_df(data) -> pd.DataFrame:
    df = pd.DataFrame(data).copy()
    if "Млрд_USD" not in df.columns:
        value_cols = [c for c in df.columns if c != "Товарная группа"]
        df = df.rename(columns={value_cols[0]: "Млрд_USD"})
    df["Млрд_USD"] = pd.to_numeric(df["Млрд_USD"], errors="coerce").fillna(0)
    total = df["Млрд_USD"].sum()
    df["Доля_%"] = np.where(total > 0, df["Млрд_USD"] / total * 100, 0)
    df = df.sort_values("Млрд_USD", ascending=False).reset_index(drop=True)
    return df

GOODS_DETAILS = {
    "минераль": "сырая нефть и нефтепродукты, природный газ, уголь и иные виды минерального топлива",
    "топлив": "сырая нефть и нефтепродукты, природный газ, уголь и иные виды минерального топлива",
    "машин": "станки, промышленное оборудование, насосы, компрессоры, двигатели, комплектующие и механические устройства",
    "электро": "электроника, кабели, аккумуляторы, электрические машины, компоненты связи и бытовая техника",
    "транспорт": "автомобили, грузовой транспорт, автокомпоненты, спецтехника и части транспортных средств",
    "фарма": "лекарственные средства, субстанции, медицинские препараты и фармацевтическая продукция",
    "удобр": "калийные, азотные и смешанные минеральные удобрения",
    "масл": "растительные масла, прежде всего подсолнечное и иные масложировые товары",
    "руды": "железные и цветные руды, концентраты, шлаки и зола",
    "алюмин": "алюминий необработанный, полуфабрикаты и изделия из алюминия",
    "медь": "рафинированная медь, медные сплавы, полуфабрикаты и изделия из меди",
    "древес": "лесоматериалы, пиломатериалы, древесина и продукция первичной обработки",
    "рыб": "рыба, ракообразные, морепродукты и замороженная рыбная продукция",
    "целлю": "целлюлоза, бумажная масса, бумага и картон",
    "кауч": "каучук, резина, шины, изделия из резины и полимерные материалы",
    "пласт": "пластмассы, полимерные материалы, упаковочные материалы и изделия из пластика",
    "хим": "органическая и неорганическая химия, реактивы, химические полуфабрикаты",
    "металл": "изделия из черных и цветных металлов, металлоконструкции и полуфабрикаты",
    "обув": "обувь, элементы обуви и потребительские товары легкой промышленности",
    "одеж": "текстиль, одежда, трикотаж и готовые изделия легкой промышленности",
    "игруш": "игрушки, спортивные товары, инвентарь и отдельные потребительские товары",
    "мебел": "мебель, осветительные приборы, интерьерные товары и бытовые изделия",
    "керами": "керамические изделия, плитка, санитарная керамика и огнеупорные материалы",
    "чай": "чай, пряности, кофе и отдельные продовольственные товары",
    "пряност": "чай, пряности, кофе и отдельные продовольственные товары",
    "драгоц": "драгоценные камни, металлы и отдельные товары ювелирной группы",
}

def describe_goods(group: str) -> str:
    group_l = str(group).lower()
    for key, text in GOODS_DETAILS.items():
        if key in group_l:
            return text
    return "товары соответствующей укрупненной группы внешнеторговой классификации"

PRODUCT_REFERENCES = {
    "минераль": {
        "tag": "ТЭК",
        "examples": "нефть марок Urals и ESPO, нефтепродукты, уголь, природный газ",
        "brands": "Роснефть, Газпром нефть, Сургутнефтегаз, НОВАТЭК — как ориентиры по отрасли",
        "use": "переработка на НПЗ, производство топлива, нефтехимия, энергетика",
    },
    "топлив": {
        "tag": "ТЭК",
        "examples": "нефть марок Urals и ESPO, нефтепродукты, уголь, природный газ",
        "brands": "Роснефть, Газпром нефть, Сургутнефтегаз, НОВАТЭК — как ориентиры по отрасли",
        "use": "переработка на НПЗ, производство топлива, нефтехимия, энергетика",
    },
    "машин": {
        "tag": "ОБОР.",
        "examples": "станки, насосы, компрессоры, строительная и промышленная техника, комплектующие",
        "brands": "SANY, XCMG, Zoomlion, Weichai, Kirloskar, Bharat Forge — примеры компаний по группе",
        "use": "строительство, промышленное производство, добыча, транспортная и складская инфраструктура",
    },
    "электро": {
        "tag": "ЭЛЕКТ.",
        "examples": "кабели, аккумуляторы, бытовая техника, компоненты связи, смартфоны, компьютеры",
        "brands": "Huawei, Xiaomi, Lenovo, Haier, Midea, BHEL — примеры компаний по группе",
        "use": "потребительский рынок, связь, ИТ-инфраструктура, промышленная автоматизация",
    },
    "транспорт": {
        "tag": "ТРАНС.",
        "examples": "легковые автомобили, грузовики, автобусы, спецтехника, автокомпоненты",
        "brands": "Haval, Geely, Chery, FAW, Dongfeng, JAC — примеры брендов по группе",
        "use": "личный транспорт, логистика, строительные работы, перевозки и автосервис",
    },
    "фарма": {
        "tag": "ФАРМА",
        "examples": "дженерики, субстанции, антибиотики, кардиологические и противовирусные препараты",
        "brands": "Dr. Reddy’s, Sun Pharma, Cipla, Glenmark — примеры индийских фармкомпаний",
        "use": "здравоохранение, аптечный рынок, больничные закупки, производство лекарств",
    },
    "удобр": {
        "tag": "АПК",
        "examples": "калийные, азотные, фосфорные и комплексные минеральные удобрения",
        "brands": "ФосАгро, Уралкалий, ЕвроХим, Акрон — примеры российских производителей",
        "use": "сельское хозяйство, повышение урожайности зерновых, масличных и технических культур",
    },
    "масл": {
        "tag": "АПК",
        "examples": "подсолнечное масло, соевое масло, рапсовое масло, масложировое сырье",
        "brands": "ЭФКО, Русагро, Благо — примеры компаний масложирового сектора",
        "use": "пищевая промышленность, производство готовых продуктов, розничный продовольственный рынок",
    },
    "руды": {
        "tag": "СЫРЬЕ",
        "examples": "железорудный концентрат, медные и никелевые руды, шлаки и зола",
        "brands": "Металлоинвест, Норникель, УГМК — примеры компаний сырьевого и металлургического контура",
        "use": "черная и цветная металлургия, производство стали, сплавов и промышленных материалов",
    },
    "алюмин": {
        "tag": "МЕТАЛЛ",
        "examples": "первичный алюминий, алюминиевые сплавы, прокат и полуфабрикаты",
        "brands": "РУСАЛ — основной российский ориентир по алюминиевой продукции",
        "use": "автомобилестроение, строительство, упаковка, энергетика, производство кабелей",
    },
    "медь": {
        "tag": "МЕТАЛЛ",
        "examples": "рафинированная медь, медная катанка, сплавы и полуфабрикаты",
        "brands": "Норникель, УГМК, РМК — примеры компаний медного и цветного металлургического сектора",
        "use": "электротехника, кабельная продукция, электроника, машиностроение",
    },
    "древес": {
        "tag": "ЛЕС",
        "examples": "пиломатериалы, фанера, целлюлозное сырье, продукция первичной обработки древесины",
        "brands": "Segezha Group, Илим, Свеза — примеры российских компаний лесопромышленного комплекса",
        "use": "строительство, мебельное производство, упаковка, бумажная промышленность",
    },
    "рыб": {
        "tag": "АПК",
        "examples": "минтай, краб, лососевые, морепродукты, замороженная рыбная продукция",
        "brands": "Доброфлот, Норебо, Русская рыбопромышленная компания — примеры отраслевых компаний",
        "use": "пищевая промышленность, переработка, розничная торговля, общественное питание",
    },
    "целлю": {
        "tag": "ЛЕС",
        "examples": "целлюлоза, бумажная масса, бумага, картон, упаковочные материалы",
        "brands": "Илим, Архангельский ЦБК, Mondi Syktyvkar — примеры производителей отрасли",
        "use": "бумажная промышленность, упаковка, санитарно-гигиенические изделия",
    },
    "кауч": {
        "tag": "ХИМ.",
        "examples": "синтетический каучук, резинотехнические изделия, шины и полимерные материалы",
        "brands": "Sibur, Sinopec, Linglong Tire, Triangle — примеры компаний и брендов по группе",
        "use": "автопром, шинная промышленность, строительство, промышленная резина",
    },
    "пласт": {
        "tag": "ХИМ.",
        "examples": "полимеры, пленки, упаковка, изделия из пластмасс, комплектующие",
        "brands": "Sinopec, Wanhua Chemical, Hengli Petrochemical — примеры китайских химических компаний",
        "use": "упаковка, бытовые товары, автокомпоненты, строительные материалы",
    },
    "хим": {
        "tag": "ХИМ.",
        "examples": "органическая и неорганическая химия, реактивы, промежуточные продукты, красители",
        "brands": "Wanhua Chemical, Sinopec, Aurobindo, Dr. Reddy’s — примеры компаний по группе",
        "use": "фармацевтика, сельское хозяйство, производство пластмасс, лакокрасочная промышленность",
    },
    "металл": {
        "tag": "МЕТАЛЛ",
        "examples": "металлоконструкции, крепеж, прокат, полуфабрикаты и изделия из черных и цветных металлов",
        "brands": "Baosteel, Ansteel, ММК, Северсталь — примеры компаний металлургического сектора",
        "use": "строительство, машиностроение, инфраструктурные проекты, промышленное оборудование",
    },
    "обув": {
        "tag": "ЛЕГПР.",
        "examples": "спортивная, повседневная и специальная обувь, подошвы, элементы обуви",
        "brands": "Anta, Li-Ning, 361° — примеры китайских брендов потребительского сегмента",
        "use": "розничная торговля, спорт, повседневное потребление, рабочая экипировка",
    },
    "одеж": {
        "tag": "ЛЕГПР.",
        "examples": "трикотаж, верхняя одежда, текстильные изделия, готовая одежда",
        "brands": "Bosideng, Anta, Li-Ning — примеры китайских брендов легкой промышленности",
        "use": "розничная торговля, массовый потребительский рынок, спортивная одежда",
    },
    "игруш": {
        "tag": "ПОТР.",
        "examples": "игрушки, спортивный инвентарь, настольные игры, товары для досуга",
        "brands": "Lego производится глобально, а в китайском сегменте заметны Sembo и Mould King как примеры категории",
        "use": "детские товары, спорт, досуг, розничная торговля",
    },
    "мебел": {
        "tag": "ПОТР.",
        "examples": "корпусная мебель, офисная мебель, светильники, интерьерные изделия",
        "brands": "Kuka Home, Man Wah, Oppein — примеры китайских производителей мебели",
        "use": "домохозяйства, офисы, гостиницы, торговые помещения",
    },
    "керами": {
        "tag": "СТРОЙ",
        "examples": "плитка, санитарная керамика, огнеупорные изделия, техническая керамика",
        "brands": "Kajaria, Somany, Asian Granito — примеры индийских производителей керамики",
        "use": "строительство, ремонт, отделочные работы, промышленная теплоизоляция",
    },
    "чай": {
        "tag": "ПИЩ.",
        "examples": "ассамский чай, дарджилинг, черный чай, пряности, перец, кардамон",
        "brands": "Tata Tea, Taj Mahal Tea, Wagh Bakri — примеры индийских чайных брендов",
        "use": "розничная торговля, общественное питание, пищевая промышленность",
    },
    "пряност": {
        "tag": "ПИЩ.",
        "examples": "перец, кардамон, куркума, кориандр, смеси специй",
        "brands": "MDH, Everest, Tata Sampann — примеры индийских брендов специй",
        "use": "пищевая промышленность, розничная торговля, общественное питание",
    },
    "драгоц": {
        "tag": "ЮВЕЛ.",
        "examples": "алмазы, бриллианты, драгоценные камни, ювелирное сырье",
        "brands": "АЛРОСА — основной российский ориентир по алмазной отрасли",
        "use": "огранка, ювелирное производство, инвестиционные и промышленные применения",
    },
    "проч": {
        "tag": "ПРОЧ.",
        "examples": "разнородные товары, не вошедшие в основные укрупненные группы",
        "brands": "без выделения конкретной компании из-за смешанного состава категории",
        "use": "зависит от конкретных товарных кодов внутри группы",
    },
}

def product_reference(group: str, flow: str = "export", partner: str = "") -> dict[str, str]:
    """Справка по группе с учетом направления потока.

    flow='export' — российский экспорт: показываем профильных российских производителей/экспортеров.
    flow='import' — российский импорт: показываем иностранных производителей и бренды, продукция которых представлена на рынке РФ.
    """
    group_l = str(group).lower()
    ref = None
    for key, value in PRODUCT_REFERENCES.items():
        if key in group_l:
            ref = dict(value)
            break
    if ref is None:
        ref = {
            "tag": "ГРУППА",
            "examples": describe_goods(group),
            "brands": "конкретные компании зависят от детального товарного кода и источника поставки",
            "use": "применение зависит от состава укрупненной товарной группы",
        }

    russian_exporters = {
        "минераль": "Роснефть, Газпром нефть, ЛУКОЙЛ, Сургутнефтегаз, НОВАТЭК, СУЭК — профильные российские производители и экспортеры топливно-энергетического сектора",
        "топлив": "Роснефть, Газпром нефть, ЛУКОЙЛ, Сургутнефтегаз, НОВАТЭК, СУЭК — профильные российские производители и экспортеры топливно-энергетического сектора",
        "удобр": "ФосАгро, Уралкалий, ЕвроХим, Акрон — крупные российские производители и экспортеры минеральных удобрений",
        "масл": "ЭФКО, Русагро, Благо — профильные российские компании масложирового сектора",
        "руды": "Металлоинвест, Норникель, УГМК — крупные российские компании сырьевого и металлургического контура",
        "алюмин": "РУСАЛ — ключевой российский производитель алюминия и алюминиевой продукции",
        "медь": "Норникель, УГМК, РМК — профильные российские компании цветной металлургии",
        "древес": "Segezha Group, Илим, Свеза — крупные российские компании лесопромышленного комплекса",
        "рыб": "Норебо, Русская рыбопромышленная компания, Доброфлот — профильные компании рыбопромышленного сектора",
        "целлю": "Илим, Архангельский ЦБК, Сегежа — профильные российские производители целлюлозно-бумажной продукции",
        "драгоц": "АЛРОСА — ключевой российский ориентир по алмазной отрасли",
        "машин": "Трансмашхолдинг, Силовые машины, Ростсельмаш, КАМАЗ — профильные российские производители машиностроительного контура",
        "электро": "Российские производители электротехнической и кабельной продукции; конкретный состав зависит от товарных кодов",
        "хим": "Сибур, ЕвроХим, Акрон, Уралхим — профильные российские производители химической продукции",
        "металл": "Северсталь, ММК, НЛМК, Металлоинвест — крупные российские компании металлургического сектора",
    }

    foreign_china = {
        "машин": "SANY, XCMG, Zoomlion, Weichai — крупные китайские производители строительной, промышленной и двигательной техники",
        "электро": "Huawei, Xiaomi, Lenovo, Haier, Midea — китайские производители электроники, бытовой техники и компонентов",
        "транспорт": "Haval, Geely, Chery, Changan, FAW, Dongfeng, JAC — китайские автомобильные бренды, активно представленные на российском рынке",
        "пласт": "Sinopec, Wanhua Chemical, Hengli Petrochemical — китайские производители химической и полимерной продукции",
        "хим": "Sinopec, Wanhua Chemical, Sinochem — крупные китайские химические компании",
        "кауч": "Sinopec, Linglong Tire, Triangle — китайские производители каучука, шин и резинотехнической продукции",
        "металл": "Baosteel, Ansteel, HBIS — крупные китайские металлургические компании",
        "обув": "Anta, Li-Ning, 361° — китайские бренды потребительского сегмента",
        "одеж": "Bosideng, Anta, Li-Ning — китайские бренды легкой промышленности",
        "игруш": "Sembo, Mould King и другие производители потребительских товаров; категория неоднородна",
        "мебел": "Kuka Home, Man Wah, Oppein — китайские производители мебели и интерьерных товаров",
    }

    foreign_india = {
        "фарма": "Sun Pharma, Dr. Reddy’s, Cipla, Lupin, Glenmark — крупные индийские фармацевтические производители",
        "машин": "Kirloskar, Bharat Forge, Larsen & Toubro, Mahindra — индийские производители оборудования, компонентов и техники",
        "электро": "BHEL, Havells, Polycab — индийские производители электротехнической продукции и оборудования",
        "хим": "Aurobindo, Dr. Reddy’s, Tata Chemicals, UPL — индийские компании химического и фармацевтического контура",
        "керами": "Kajaria, Somany, Asian Granito — индийские производители керамической продукции",
        "чай": "Tata Tea, Taj Mahal Tea, Wagh Bakri — индийские чайные бренды",
        "пряност": "MDH, Everest, Tata Sampann — индийские бренды специй и продовольственных товаров",
        "металл": "Tata Steel, JSW Steel, Jindal Steel — крупные индийские металлургические компании",
    }

    selected = ""
    if flow == "export":
        for key, value in russian_exporters.items():
            if key in group_l:
                selected = value
                break
        label = "Профильные российские производители и экспортеры"
        if not selected:
            selected = "точное распределение по российским экспортерам требует детализации по компаниям и товарным кодам"
    else:
        partner_l = str(partner).lower()
        source = foreign_india if "инд" in partner_l else foreign_china
        for key, value in source.items():
            if key in group_l:
                selected = value
                break
        label = "Иностранные производители и бренды"
        if not selected:
            selected = "конкретные иностранные производители зависят от детального товарного кода, поставщика и канала ввоза"

    return {
        "tag": ref.get("tag", "ГРУППА"),
        "examples": ref.get("examples", describe_goods(group)),
        "companies_label": label,
        "companies": selected,
        "use": ref.get("use", "применение зависит от состава укрупненной товарной группы"),
    }

def structure_pie(df: pd.DataFrame, title: str, colors: list[str] | None = None) -> go.Figure:
    plot_df = df.copy()
    fig = px.pie(
        plot_df,
        values="Млрд_USD",
        names="Товарная группа",
        hole=0.48,
        color_discrete_sequence=colors or px.colors.qualitative.Set3,
    )
    if len(plot_df):
        top = plot_df.iloc[0]
        fig.add_annotation(
            text=f"<b>{pct(float(top['Доля_%']))}</b><br><span style='font-size:11px'>доля лидера</span>",
            x=0.5, y=0.5, showarrow=False, font=dict(size=14, color="#121826")
        )
    fig.update_traces(
        textposition="inside",
        textinfo="percent",
        hovertemplate="%{label}<br>Стоимость: %{value:.2f} млрд $<br>Доля: %{percent}<extra></extra>",
        sort=False
    )
    fig.update_layout(
        title=title,
        height=410,
        template="plotly_white",
        margin=dict(l=10, r=10, t=55, b=24),
        legend=dict(orientation="h", y=-0.18, font=dict(size=10)),
        font=dict(family="Inter", size=11),
    )
    return fig

def render_product_illustrations(
    title: str,
    df: pd.DataFrame,
    max_items: int = 5,
    accent: str = "#4A7CF7",
    flow: str = "export",
    partner: str = "",
) -> None:
    """Аккуратная справка по ключевым товарным группам.

    Блок вынесен в отдельную вкладку, чтобы не перегружать основной анализ структуры.
    """
    st.markdown(f"<div class='company-section-title'>{html.escape(title)}</div>", unsafe_allow_html=True)
    note = (
        "Для экспортных потоков указаны профильные российские производители и экспортеры соответствующих товарных групп. "
        "Для импортных потоков указаны иностранные производители и бренды, продукция которых представлена в российском импорте. "
        "Перечень компаний используется как отраслевой ориентир; точное распределение оборота по компаниям требует отдельной таможенной микростатистики."
    )
    st.markdown(f"<div class='company-section-subtitle'>{html.escape(note)}</div>", unsafe_allow_html=True)

    for _, row in df.head(max_items).iterrows():
        ref = product_reference(str(row["Товарная группа"]), flow=flow, partner=partner)
        st.markdown(f"""
        <div class="reference-card" style="--accent:{html.escape(accent)};">
          <div class="reference-top">
            <div>
              <div class="reference-title">{html.escape(str(row['Товарная группа']))}</div>
              <div class="reference-meta">{html.escape(money_bln(row['Млрд_USD']))} · {html.escape(pct(row['Доля_%']))} в показанной структуре</div>
            </div>
            <div class="reference-tag">{html.escape(ref['tag'])}</div>
          </div>
          <div class="reference-grid">
            <div class="reference-field">
              <div class="reference-label">Типичная продукция</div>
              <div class="reference-text">{html.escape(ref['examples'])}</div>
            </div>
            <div class="reference-field">
              <div class="reference-label">{html.escape(ref['companies_label'])}</div>
              <div class="reference-text">{html.escape(ref['companies'])}</div>
            </div>
            <div class="reference-field">
              <div class="reference-label">Где используется</div>
              <div class="reference-text">{html.escape(ref['use'])}</div>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

def add_goods_details(df: pd.DataFrame, flow: str = "export", partner: str = "") -> pd.DataFrame:
    out = df.copy()
    out["Что входит в группу"] = out["Товарная группа"].apply(describe_goods)
    out["Стоимость"] = out["Млрд_USD"].apply(money_bln)
    out["Доля"] = out["Доля_%"].apply(pct)
    refs = out["Товарная группа"].apply(lambda x: product_reference(str(x), flow=flow, partner=partner))
    out["Примеры продукции"] = refs.apply(lambda x: x["examples"])
    out["Компании"] = refs.apply(lambda x: x["companies"])
    out["Где используется"] = refs.apply(lambda x: x["use"])
    return out

def structure_bar(df: pd.DataFrame, title: str, main_color: str) -> go.Figure:
    plot_df = df.sort_values("Млрд_USD", ascending=True).copy()
    max_value = plot_df["Млрд_USD"].max() if len(plot_df) else 0
    colors = [main_color if v == max_value else "#DDE6EE" for v in plot_df["Млрд_USD"]]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=plot_df["Млрд_USD"],
        y=plot_df["Товарная группа"],
        orientation="h",
        marker_color=colors,
        text=[money_bln(v) for v in plot_df["Млрд_USD"]],
        textposition="outside",
        customdata=np.stack([plot_df["Доля_%"], plot_df["Товарная группа"].apply(describe_goods)], axis=-1),
        hovertemplate="%{y}<br>Стоимость: %{x:.2f} млрд $<br>Доля: %{customdata[0]:.1f}%<br>%{customdata[1]}<extra></extra>",
    ))
    if len(df):
        top = df.iloc[0]
        fig.add_annotation(
            x=float(top["Млрд_USD"]), y=top["Товарная группа"],
            text=f"ключевая группа: {pct(float(top['Доля_%']))}",
            showarrow=True, arrowhead=2, ax=30, ay=-30,
            font=dict(size=11, color="#121826"), bgcolor="rgba(255,255,255,0.86)", bordercolor="#E2E8F0"
        )
    fig.update_layout(
        title=title,
        height=max(410, 32 * len(plot_df) + 150),
        template="plotly_white",
        margin=dict(l=20, r=90, t=55, b=28),
        font=dict(family="Inter", size=11),
        xaxis=dict(title="млрд долларов США"),
        yaxis=dict(title=""),
        showlegend=False,
    )
    return fig

def top_summary(df: pd.DataFrame, n: int = 3) -> str:
    top = df.head(n)
    parts = [f"<b>{row['Товарная группа']}</b> — {money_bln(row['Млрд_USD'])} ({pct(row['Доля_%'])})" for _, row in top.iterrows()]
    return "; ".join(parts)

def goods_card(title: str, df: pd.DataFrame) -> None:
    top = df.iloc[0]
    st.markdown(f"""
    <div class="goods-card">
      <div class="goods-title">{title}</div>
      <div class="goods-text">
        Крупнейшая группа: <span class="key">{top['Товарная группа']}</span> — <span class="key">{money_bln(top['Млрд_USD'])}</span>,
        или <span class="key">{pct(top['Доля_%'])}</span> от показанного состава. В группу входят: {describe_goods(top['Товарная группа'])}.
      </div>
    </div>
    """, unsafe_allow_html=True)

latest_year = int(min(df_ru_cn["Год"].max(), df_ru_in["Год"].max()))
first_year = int(max(df_ru_cn["Год"].min(), df_ru_in["Год"].min()))
cn_latest = year_row(df_ru_cn, latest_year)
in_latest = year_row(df_ru_in, latest_year)
cn_first = year_row(df_ru_cn, first_year)
in_first = year_row(df_ru_in, first_year)

cn_exp_col = get_col(df_ru_cn, ["Экспорт_РФ_в_КНР", "Экспорт"])
cn_imp_col = get_col(df_ru_cn, ["Импорт_РФ_из_КНР", "Импорт"])
in_exp_col = get_col(df_ru_in, ["Экспорт_РФ_в_Индию", "Экспорт"])
in_imp_col = get_col(df_ru_in, ["Импорт_РФ_из_Индии", "Импорт"])

cn_turnover = float(cn_latest["Оборот"] / 1e6)
in_turnover = float(in_latest["Оборот"] / 1e6)
cn_balance = float(cn_latest["Сальдо"] / 1e6)
in_balance = float(in_latest["Сальдо"] / 1e6)
cn_growth_times = float(cn_latest["Оборот"] / cn_first["Оборот"]) if float(cn_first["Оборот"]) else np.nan
in_growth_times = float(in_latest["Оборот"] / in_first["Оборот"]) if float(in_first["Оборот"]) else np.nan
cn_growth_pct = (cn_growth_times - 1) * 100 if np.isfinite(cn_growth_times) else np.nan
in_growth_pct = (in_growth_times - 1) * 100 if np.isfinite(in_growth_times) else np.nan

cn_export_latest = float(cn_latest[cn_exp_col] / 1e6)
cn_import_latest = float(cn_latest[cn_imp_col] / 1e6)
in_export_latest = float(in_latest[in_exp_col] / 1e6)
in_import_latest = float(in_latest[in_imp_col] / 1e6)

coverage_cn_latest = float(coverage_df[coverage_df["Год"] == latest_year]["РФ-Китай"].iloc[-1]) if latest_year in set(coverage_df["Год"]) else float(coverage_df["РФ-Китай"].iloc[-1])
coverage_in_latest = float(coverage_df[coverage_df["Год"] == latest_year]["РФ-Индия"].iloc[-1]) if latest_year in set(coverage_df["Год"]) else float(coverage_df["РФ-Индия"].iloc[-1])

# -----------------------------------------------------------------------------
# ШАПКА
# -----------------------------------------------------------------------------
lang_col1, lang_col2 = st.columns([6, 1])
with lang_col2:
    render_lang_switcher()

st.markdown(f"""
<div class="hero">
  <div class="kicker">Глава 2 · статистическая база исследования</div>
  <h1 class="hero-title">Статистический анализ внешней торговли</h1>
  <div class="hero-subtitle">
    В разделе представлены расчеты по динамике, структуре и сбалансированности торговли России с Китаем и Индией.
    Особое внимание уделяется не только объему торговли, но и ее содержанию: какие товарные группы формируют экспорт и импорт,
    как изменилась география партнеров и насколько экспортная выручка покрывает импортные закупки.
  </div>
</div>
""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
with m1:
    metric_card("РФ—Китай, оборот", money_bln(cn_turnover), f"{latest_year} год; рост к началу периода — {times(cn_growth_times)}.")
with m2:
    metric_card("РФ—Индия, оборот", money_bln(in_turnover), f"{latest_year} год; рост к началу периода — {times(in_growth_times)}.")
with m3:
    metric_card("Сальдо РФ—Китай", money_bln(cn_balance), f"Экспорт: {money_bln(cn_export_latest)}; импорт: {money_bln(cn_import_latest)}.")
with m4:
    metric_card("Сальдо РФ—Индия", money_bln(in_balance), f"Экспорт: {money_bln(in_export_latest)}; импорт: {money_bln(in_import_latest)}.")

explain(
    "Порядок чтения раздела",
    "Сначала рассматривается масштаб торговли во времени, затем — экспортно-импортная структура, далее формально оцениваются структурные сдвиги и коэффициент покрытия. Такой порядок позволяет связать графики с экономической интерпретацией: объем → состав → изменение структуры → устойчивость торгового баланса.",
    kind="method",
)

# -----------------------------------------------------------------------------
# ВКЛАДКИ
# -----------------------------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([L("data_tab_dynamics"), L("data_tab_structure"), L("data_tab_indices"), L("data_tab_raw")])

with tab1:
    explain(
        "Динамический блок",
        "Динамика показывает, что российско-китайская торговля формировалась как долгосрочный крупный контур, тогда как российско-индийское направление резко усилилось в последние годы за счет экспортного потока.",
        kind="method",
    )
    dt1, dt2, dt3 = st.tabs([L("data_subtab_turnover"), L("data_subtab_expimp"), L("data_subtab_balance")])

    with dt1:
        explain(
            "Внешнеторговый оборот",
            "Оборот равен сумме экспорта и импорта. Он показывает масштаб торгового взаимодействия, но сам по себе не отвечает на вопрос о выгоде или качестве структуры. Поэтому далее показатель сопоставляется с сальдо и составом товарных потоков.",
        )
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df_ru_cn["Год"], y=df_ru_cn["Оборот"] / 1e6,
            mode="lines+markers", name="Россия—Китай",
            line=dict(color="#CC2936", width=3), marker=dict(size=6),
            hovertemplate="Год: %{x}<br>Оборот РФ—Китай: %{y:.1f} млрд $<extra></extra>",
        ))
        fig.add_trace(go.Scatter(
            x=df_ru_in["Год"], y=df_ru_in["Оборот"] / 1e6,
            mode="lines+markers", name="Россия—Индия",
            line=dict(color="#E8A838", width=3), marker=dict(size=6), yaxis="y2",
            hovertemplate="Год: %{x}<br>Оборот РФ—Индия: %{y:.1f} млрд $<extra></extra>",
        ))
        fig.add_vrect(x0=2021.5, x1=latest_year + 0.5, fillcolor="rgba(232,168,56,0.10)", line_width=0)
        fig.add_annotation(x=2022, y=1.04, yref="paper", text="перестройка торговых потоков после 2022 года", showarrow=False, font=dict(size=11, color="#64748B"))
        fig.add_annotation(x=latest_year, y=cn_turnover, text=money_bln(cn_turnover), showarrow=True, arrowhead=2, ax=-55, ay=-35, bgcolor="rgba(255,255,255,0.88)", bordercolor="#E2E8F0")
        fig.add_annotation(x=latest_year, y=in_turnover, yref="y2", text=money_bln(in_turnover), showarrow=True, arrowhead=2, ax=-60, ay=35, bgcolor="rgba(255,255,255,0.88)", bordercolor="#E2E8F0")
        fig.update_layout(
            **PLOT_LAYOUT,
            xaxis=dict(dtick=5, title="Год"),
            yaxis=dict(title="Россия—Китай · млрд $"),
            yaxis2=dict(title="Россия—Индия · млрд $", overlaying="y", side="right"),
            legend=dict(orientation="h", y=1.12),
        )
        st.plotly_chart(fig, use_container_width=True)
        c1, c2 = st.columns(2)
        with c1:
            explain("Китайское направление", f"С {first_year} по {latest_year} год оборот увеличился примерно {times(cn_growth_times)}. На графике видно, что Китай стал устойчивым и наиболее масштабным направлением торговли.", kind="insight")
        with c2:
            explain("Индийское направление", f"С {first_year} по {latest_year} год оборот увеличился примерно {times(in_growth_times)}. При этом рост носит более скачкообразный характер и связан с переориентацией российского экспорта.", kind="insight")

    with dt2:
        explain(
            "Экспорт и импорт",
            "Сопоставление экспорта и импорта показывает внутреннюю структуру оборота. Для Китая характерны крупные встречные потоки, а для Индии — резкое превышение российского экспорта над импортом.",
        )
        fig2 = make_subplots(rows=1, cols=2, subplot_titles=("Россия—Китай", "Россия—Индия"))
        for ci, (df, pair, ec, ic) in enumerate([(df_ru_cn, "Китай", cn_exp_col, cn_imp_col), (df_ru_in, "Индия", in_exp_col, in_imp_col)], 1):
            fig2.add_trace(go.Bar(
                x=df["Год"], y=df[ec] / 1e6,
                name=f"Экспорт РФ · {pair}", marker_color="#6A9A7B",
                hovertemplate="Год: %{x}<br>Экспорт: %{y:.1f} млрд $<extra></extra>",
            ), row=1, col=ci)
            fig2.add_trace(go.Bar(
                x=df["Год"], y=df[ic] / 1e6,
                name=f"Импорт РФ · {pair}", marker_color="#B0D4B8",
                hovertemplate="Год: %{x}<br>Импорт: %{y:.1f} млрд $<extra></extra>",
            ), row=1, col=ci)
        fig2.add_annotation(x=latest_year, y=cn_export_latest, text=f"экспорт {money_bln(cn_export_latest)}", showarrow=True, arrowhead=2, ax=-45, ay=-35, row=1, col=1)
        fig2.add_annotation(x=latest_year, y=in_export_latest, text=f"экспорт {money_bln(in_export_latest)}", showarrow=True, arrowhead=2, ax=-50, ay=-35, row=1, col=2)
        fig2.update_layout(
            barmode="group", height=430, template="plotly_white",
            margin=dict(l=20, r=20, t=50, b=26),
            font=dict(family="Inter", size=11),
            legend=dict(orientation="h", y=1.13),
        )
        fig2.update_yaxes(title_text="млрд $")
        st.plotly_chart(fig2, use_container_width=True)
        c1, c2 = st.columns(2)
        with c1:
            explain("Россия—Китай", f"В {latest_year} году экспорт России в Китай составил {money_bln(cn_export_latest)}, импорт из Китая — {money_bln(cn_import_latest)}. Разрыв между потоками есть, но он не является экстремальным.", kind="insight")
        with c2:
            explain("Россия—Индия", f"В {latest_year} году экспорт России в Индию составил {money_bln(in_export_latest)}, импорт из Индии — только {money_bln(in_import_latest)}. Это указывает на сильную асимметрию торговли.", kind="insight")

    with dt3:
        explain(
            "Торговое сальдо",
            "Сальдо рассчитывается как экспорт минус импорт. Положительное значение означает профицит торговли для России. Однако высокий профицит нужно сопоставлять со структурой: он может быть следствием сырьевой концентрации, а не широкой диверсификации.",
        )
        fig3 = go.Figure()
        for df, name, color in [(df_ru_cn, "Россия—Китай", "#CC2936"), (df_ru_in, "Россия—Индия", "#E8A838")]:
            values = df["Сальдо"] / 1e6
            fig3.add_trace(go.Bar(
                x=df["Год"], y=values, name=name,
                marker_color=[color if v >= 0 else "#D9534F" for v in values],
                hovertemplate="Год: %{x}<br>Сальдо: %{y:.1f} млрд $<extra></extra>",
            ))
        fig3.add_hline(y=0, line_dash="dash", line_color="#64748B")
        fig3.add_annotation(x=latest_year, y=cn_balance, text=f"РФ—Китай: {money_bln(cn_balance)}", showarrow=True, arrowhead=2, ax=-35, ay=-30, bgcolor="rgba(255,255,255,0.88)", bordercolor="#E2E8F0")
        fig3.add_annotation(x=latest_year, y=in_balance, text=f"РФ—Индия: {money_bln(in_balance)}", showarrow=True, arrowhead=2, ax=-45, ay=-45, bgcolor="rgba(255,255,255,0.88)", bordercolor="#E2E8F0")
        fig3.update_layout(
            **PLOT_LAYOUT,
            yaxis=dict(title="Сальдо (млрд $)"),
            xaxis=dict(dtick=5, title="Год"),
            barmode="group",
            legend=dict(orientation="h", y=1.12),
        )
        st.plotly_chart(fig3, use_container_width=True)
        c1, c2 = st.columns(2)
        with c1:
            explain("Баланс с Китаем", "В разные годы торговля с Китаем переходила от профицита к дефициту и обратно. Это связано с ростом импорта машин, оборудования и электроники, а затем с увеличением российского экспорта.", kind="insight")
        with c2:
            explain("Баланс с Индией", "Сальдо с Индией в последние годы резко выросло и стало одним из самых заметных результатов анализа. Его природа — экспортная асимметрия, прежде всего по энергетическому сырью.", kind="insight")

with tab2:
    explain(
        "Товарная структура",
        "Структурный анализ показывает, какие именно товары формируют торговые потоки. Важно различать сырьевые позиции, промышленный импорт, технологические компоненты и нишевые товары.",
        kind="method",
    )
    st1, st2, st3, st4 = st.tabs([L("data_subtab_export_rf"), L("data_subtab_import_rf"), L("data_subtab_partners"), GT("stats04_tab_company_ref")] )

    with st1:
        explain(
            "Экспорт России",
            "В экспорте оценивается, какая часть поставок приходится на сырьевые и полуфабрикатные группы. Чем выше доля минерального топлива, тем сильнее зависимость результата от энергетической конъюнктуры.",
        )
        cn_exp_struct = structure_df(ru_export_to_cn_structure)
        in_exp_struct = structure_df(ru_export_to_in_structure)

        st.markdown("<div class='subsection-title'>Россия—Китай</div>", unsafe_allow_html=True)
        c1, c2 = st.columns([1.2, 1])
        with c1:
            st.plotly_chart(structure_bar(cn_exp_struct, "Экспорт России в Китай · столбчатое представление", "#CC2936"), use_container_width=True)
        with c2:
            st.plotly_chart(structure_pie(cn_exp_struct, "Экспорт России в Китай · круговое представление", ["#CC2936", "#E69097", "#F4B8BC", "#F8D7DA", "#E2E8F0", "#CBD5E1", "#94A3B8"]), use_container_width=True)
        goods_card("Что именно экспортируется в Китай", cn_exp_struct)
        explain("Китай: состав экспорта", f"Три крупнейшие группы: {top_summary(cn_exp_struct)}. Структура экспорта в Китай более диверсифицирована, чем в Индию: кроме топлива заметны руды, металлы, древесина, рыба, удобрения и другие сырьевые и полуфабрикатные позиции.", kind="insight")
        with st.expander("Подробная таблица состава экспорта в Китай", expanded=False):
            st.dataframe(add_goods_details(cn_exp_struct, flow="export", partner="Китай")[["Товарная группа", "Стоимость", "Доля", "Примеры продукции", "Где используется"]], use_container_width=True, hide_index=True)

        st.markdown("<div class='subsection-title' style='margin-top:1rem;'>Россия—Индия</div>", unsafe_allow_html=True)
        c1, c2 = st.columns([1.2, 1])
        with c1:
            st.plotly_chart(structure_bar(in_exp_struct, "Экспорт России в Индию · столбчатое представление", "#E8A838"), use_container_width=True)
        with c2:
            st.plotly_chart(structure_pie(in_exp_struct, "Экспорт России в Индию · круговое представление", ["#E8A838", "#F2C66D", "#F7DFA7", "#FDF1D0", "#E2E8F0", "#CBD5E1", "#94A3B8"]), use_container_width=True)
        goods_card("Что именно экспортируется в Индию", in_exp_struct)
        explain("Индия: состав экспорта", f"Три крупнейшие группы: {top_summary(in_exp_struct)}. Экспортное направление в Индию заметно более концентрировано: ключевой вклад в него вносят минеральное топливо, растительные масла и удобрения.", kind="insight")
        with st.expander("Подробная таблица состава экспорта в Индию", expanded=False):
            st.dataframe(add_goods_details(in_exp_struct, flow="export", partner="Индия")[["Товарная группа", "Стоимость", "Доля", "Примеры продукции", "Где используется"]], use_container_width=True, hide_index=True)

    with st2:
        explain(
            "Импорт России",
            "В импорте важно отделить широкую промышленную зависимость от нишевых поставок. Китай поставляет большой набор машин, электроники и транспортных средств, а Индия заметна прежде всего по фармацевтике, химии и отдельным промышленным товарам.",
        )
        cn_imp_struct = structure_df(ru_import_from_cn_structure)
        in_imp_struct = structure_df(ru_import_from_in_structure)

        st.markdown("<div class='subsection-title'>Россия—Китай</div>", unsafe_allow_html=True)
        c1, c2 = st.columns([1.2, 1])
        with c1:
            st.plotly_chart(structure_bar(cn_imp_struct, "Импорт России из Китая · столбчатое представление", "#4A7CF7"), use_container_width=True)
        with c2:
            st.plotly_chart(structure_pie(cn_imp_struct, "Импорт России из Китая · круговое представление", ["#4A7CF7", "#7CA3FF", "#A9C1FF", "#D6E3FF", "#E2E8F0", "#CBD5E1", "#94A3B8"]), use_container_width=True)
        goods_card("Что именно импортируется из Китая", cn_imp_struct)
        explain("Китай: состав импорта", f"Три крупнейшие группы: {top_summary(cn_imp_struct)}. По содержанию это прежде всего машины и оборудование, транспортные средства, электроника, пластмассы, химическая продукция и различные потребительские товары.", kind="insight")
        with st.expander("Подробная таблица состава импорта из Китая", expanded=False):
            st.dataframe(add_goods_details(cn_imp_struct, flow="import", partner="Китай")[["Товарная группа", "Стоимость", "Доля", "Примеры продукции", "Где используется"]], use_container_width=True, hide_index=True)

        st.markdown("<div class='subsection-title' style='margin-top:1rem;'>Россия—Индия</div>", unsafe_allow_html=True)
        c1, c2 = st.columns([1.2, 1])
        with c1:
            st.plotly_chart(structure_bar(in_imp_struct, "Импорт России из Индии · столбчатое представление", "#6A9A7B"), use_container_width=True)
        with c2:
            st.plotly_chart(structure_pie(in_imp_struct, "Импорт России из Индии · круговое представление", ["#6A9A7B", "#93B89F", "#B8D2C0", "#DCEBE3", "#E2E8F0", "#CBD5E1", "#94A3B8"]), use_container_width=True)
        goods_card("Что именно импортируется из Индии", in_imp_struct)
        explain("Индия: состав импорта", f"Три крупнейшие группы: {top_summary(in_imp_struct)}. Индийские поставки меньше по объему, но важны по отдельным нишам: фармацевтика, химия, машины и оборудование, электрооборудование, а также чай и пряности.", kind="insight")
        with st.expander("Подробная таблица состава импорта из Индии", expanded=False):
            st.dataframe(add_goods_details(in_imp_struct, flow="import", partner="Индия")[["Товарная группа", "Стоимость", "Доля", "Примеры продукции", "Где используется"]], use_container_width=True, hide_index=True)

    with st3:
        explain(
            "География экспортных партнеров",
            "Сравнение структуры 2000 и 2023 годов показывает перестройку направления российского экспорта. Главный сдвиг заключается в снижении роли западных рынков и усилении азиатского направления.",
        )
        c1, c2 = st.columns(2)
        for col, data, year in [(c1, export_partners_2000, 2000), (c2, export_partners_2023, 2023)]:
            with col:
                dfp = pd.DataFrame(data).sort_values("Доля_%", ascending=True)
                colors = ["#CC2936" if str(country).lower() in ["china", "китай"] else "#E8A838" if str(country).lower() in ["india", "индия"] else "#DDE6EE" for country in dfp["Страна"]]
                fig = go.Figure(go.Bar(
                    x=dfp["Доля_%"], y=dfp["Страна"], orientation="h",
                    marker_color=colors,
                    text=[pct(v) for v in dfp["Доля_%"]], textposition="outside",
                    hovertemplate="%{y}<br>Доля: %{x:.1f}%<extra></extra>",
                ))
                fig.update_layout(
                    title=f"Структура экспорта России · {year}",
                    height=430, template="plotly_white", margin=dict(l=20, r=80, t=50, b=26),
                    font=dict(family="Inter", size=11), xaxis=dict(title="доля, %"), yaxis=dict(title=""), showlegend=False,
                )
                st.plotly_chart(fig, use_container_width=True)
        explain("Ключевой структурный сдвиг", "В 2000 году среди значимых направлений российского экспорта заметную роль играли европейские страны и США. К 2023 году центр тяжести сместился к Китаю и Индии, что подтверждается как графически, так и расчетом индексов структурных сдвигов.", kind="insight")

    with st4:
        st.markdown("""
        <div class="company-note">
          <b>Методологическое уточнение.</b> В данном блоке компании не используются как источник распределения товарооборота.
          Они приведены для ориентира: в экспорте — как профильные российские производители и экспортеры соответствующих групп,
          в импорте — как иностранные производители и бренды, продукция которых может быть представлена в российских поставках.
          Для строгого ранжирования по компаниям необходима отдельная таможенная микростатистика по участникам ВЭД.
        </div>
        """, unsafe_allow_html=True)

        explain(
            "Зачем блок вынесен отдельно",
            "На защите основное внимание можно оставить на динамике, структуре и коэффициентах. Справка по компаниям открывается при необходимости, если возникает вопрос о том, какие реальные производители стоят за укрупненными товарными группами.",
            kind="method",
        )

        cn_exp_struct = structure_df(ru_export_to_cn_structure)
        in_exp_struct = structure_df(ru_export_to_in_structure)
        cn_imp_struct = structure_df(ru_import_from_cn_structure)
        in_imp_struct = structure_df(ru_import_from_in_structure)

        ref_export, ref_import = st.tabs(["Российский экспорт", "Российский импорт"])
        with ref_export:
            render_product_illustrations("Экспорт России в Китай: профильные российские экспортеры", cn_exp_struct, accent="#CC2936", flow="export", partner="Китай")
            render_product_illustrations("Экспорт России в Индию: профильные российские экспортеры", in_exp_struct, accent="#E8A838", flow="export", partner="Индия")
            with st.expander("Таблица-справка по экспортным группам", expanded=False):
                export_ref = pd.concat([
                    add_goods_details(cn_exp_struct, flow="export", partner="Китай").assign(Направление="Россия—Китай"),
                    add_goods_details(in_exp_struct, flow="export", partner="Индия").assign(Направление="Россия—Индия"),
                ], ignore_index=True)
                st.dataframe(export_ref[["Направление", "Товарная группа", "Стоимость", "Доля", "Примеры продукции", "Компании", "Где используется"]], use_container_width=True, hide_index=True)

        with ref_import:
            render_product_illustrations("Импорт России из Китая: иностранные производители и бренды", cn_imp_struct, accent="#4A7CF7", flow="import", partner="Китай")
            render_product_illustrations("Импорт России из Индии: иностранные производители и бренды", in_imp_struct, accent="#6A9A7B", flow="import", partner="Индия")
            with st.expander("Таблица-справка по импортным группам", expanded=False):
                import_ref = pd.concat([
                    add_goods_details(cn_imp_struct, flow="import", partner="Китай").assign(Направление="Китай—Россия"),
                    add_goods_details(in_imp_struct, flow="import", partner="Индия").assign(Направление="Индия—Россия"),
                ], ignore_index=True)
                st.dataframe(import_ref[["Направление", "Товарная группа", "Стоимость", "Доля", "Примеры продукции", "Компании", "Где используется"]], use_container_width=True, hide_index=True)

with tab3:
    explain(
        "Индексы и коэффициенты",
        "Этот блок переводит наблюдаемые изменения в формальные статистические показатели. Индексы Гатева и Салаи измеряют силу структурного сдвига, а коэффициент покрытия отражает соотношение экспорта и импорта.",
        kind="method",
    )
    i1, i2 = st.tabs([L("data_subtab_shifts"), L("data_subtab_coverage")])

    with i1:
        st.markdown("""
        <div class="warn-card">
          <b>Интерпретация:</b> чем ближе индекс к 1, тем сильнее структурный сдвиг. Значения, полученные для внешней торговли,
          подтверждают, что изменение географии торговли было существенным, а не только визуально заметным.
        </div>
        """, unsafe_allow_html=True)
        shift_rows = []
        for key, ind in structural_indices.items():
            shift_rows.append({"Направление": key, "Индекс Гатева": ind["Гатева"], "Индекс Салаи": ind["Салаи"]})
        shift_df = pd.DataFrame(shift_rows)
        fig_shift = go.Figure()
        fig_shift.add_trace(go.Bar(x=shift_df["Направление"], y=shift_df["Индекс Гатева"], name="Гатева", marker_color="#4A7CF7", text=[f"{v:.3f}" for v in shift_df["Индекс Гатева"]], textposition="outside"))
        fig_shift.add_trace(go.Bar(x=shift_df["Направление"], y=shift_df["Индекс Салаи"], name="Салаи", marker_color="#6A9A7B", text=[f"{v:.3f}" for v in shift_df["Индекс Салаи"]], textposition="outside"))
        fig_shift.update_layout(
            barmode="group", template="plotly_white", height=390, margin=dict(l=20, r=20, t=45, b=26),
            yaxis=dict(title="значение индекса", range=[0, max(1, float(shift_df[["Индекс Гатева", "Индекс Салаи"]].max().max()) + 0.12)]),
            font=dict(family="Inter", size=11), legend=dict(orientation="h", y=1.12),
        )
        st.plotly_chart(fig_shift, use_container_width=True)
        explain("Что фиксируют индексы", "Высокие значения индексов показывают сильную перестройку географии торговли. В экспорте это связано с ростом роли Китая и Индии, а в импорте — прежде всего с усилением китайского направления как основного источника поставок.", kind="insight")
        st.dataframe(shift_df.style.format({"Индекс Гатева": "{:.3f}", "Индекс Салаи": "{:.3f}"}), use_container_width=True, hide_index=True)

    with i2:
        explain(
            "Коэффициент покрытия",
            "Коэффициент покрытия равен отношению экспорта к импорту. Значение выше 1 означает, что экспорт превышает импорт; значение ниже 1 — импорт превышает экспорт. Для удобства на графике проведена линия равновесия.",
        )
        fig4 = go.Figure()
        fig4.add_trace(go.Scatter(
            x=coverage_df["Год"], y=coverage_df["РФ-Китай"], mode="lines+markers", name="Россия—Китай",
            line=dict(color="#CC2936", width=3), marker=dict(size=6),
            hovertemplate="Год: %{x}<br>Коэффициент: %{y:.2f}x<extra></extra>",
        ))
        fig4.add_trace(go.Scatter(
            x=coverage_df["Год"], y=coverage_df["РФ-Индия"], mode="lines+markers", name="Россия—Индия",
            line=dict(color="#E8A838", width=3), marker=dict(size=6),
            hovertemplate="Год: %{x}<br>Коэффициент: %{y:.2f}x<extra></extra>",
        ))
        fig4.add_hline(y=1, line_dash="dash", line_color="#64748B", annotation_text="экспорт = импорт")
        fig4.add_annotation(x=latest_year, y=coverage_cn_latest, text=f"РФ—Китай: {ratio(coverage_cn_latest)}", showarrow=True, arrowhead=2, ax=-45, ay=-35, bgcolor="rgba(255,255,255,0.88)", bordercolor="#E2E8F0")
        fig4.add_annotation(x=latest_year, y=coverage_in_latest, text=f"РФ—Индия: {ratio(coverage_in_latest)}", showarrow=True, arrowhead=2, ax=-55, ay=-45, bgcolor="rgba(255,255,255,0.88)", bordercolor="#E2E8F0")
        fig4.update_layout(
            **PLOT_LAYOUT,
            yaxis=dict(title="коэффициент покрытия, раз"),
            xaxis=dict(dtick=5, title="Год"),
            legend=dict(orientation="h", y=1.12),
        )
        st.plotly_chart(fig4, use_container_width=True)
        c1, c2 = st.columns(2)
        with c1:
            explain("Россия—Китай", f"В {latest_year} году коэффициент покрытия составил {ratio(coverage_cn_latest)}. Экспорт превышал импорт, но соотношение оставалось относительно близким к равновесию.", kind="insight")
        with c2:
            explain("Россия—Индия", f"В {latest_year} году коэффициент покрытия составил {ratio(coverage_in_latest)}. Значение отражает экстремальное превышение российского экспорта над импортом из Индии.", kind="insight")

with tab4:
    explain(
        "Исходные таблицы",
        "Этот раздел оставлен для проверки числовой базы графиков. Здесь можно посмотреть ряды, из которых построены визуализации: оборот, экспорт, импорт, сальдо и коэффициент покрытия.",
        kind="method",
    )
    raw_options = {
        GT("stats04_raw_ru_cn_turnover"): "ru_cn",
        GT("stats04_raw_ru_in_turnover"): "ru_in",
        GT("stats04_raw_cn_in_turnover"): "cn_in",
        L("data_subtab_coverage"): "coverage",
    }
    raw_label = st.radio("", list(raw_options.keys()), horizontal=True, label_visibility="collapsed")
    raw = raw_options.get(raw_label, "ru_cn")
    fmt = lambda v: "{:,.0f}".format(v)
    cols_cn = [c for c in df_ru_cn.columns if c != "Год"]
    cols_in = [c for c in df_ru_in.columns if c != "Год"]
    if raw == "ru_cn":
        st.markdown("<span class='pill'>Россия—Китай</span><span class='pill'>экспорт</span><span class='pill'>импорт</span><span class='pill'>сальдо</span>", unsafe_allow_html=True)
        s = {c: fmt for c in cols_cn} | {"Коэф_покрытия": "{:.2f}"}
        st.dataframe(df_ru_cn.style.format(s), use_container_width=True)
    elif raw == "ru_in":
        st.markdown("<span class='pill'>Россия—Индия</span><span class='pill'>экспорт</span><span class='pill'>импорт</span><span class='pill'>сальдо</span>", unsafe_allow_html=True)
        s = {c: fmt for c in cols_in} | {"Коэф_покрытия": "{:.2f}"}
        st.dataframe(df_ru_in.style.format(s), use_container_width=True)
    elif raw == "cn_in":
        from data.diploma_data import df_cn_in
        st.markdown("<span class='pill'>Китай—Индия</span><span class='pill'>дополнительная ось торгового треугольника</span>", unsafe_allow_html=True)
        st.dataframe(df_cn_in.style.format({c: fmt for c in df_cn_in.columns if c != "Год"}), use_container_width=True)
    else:
        st.markdown("<span class='pill'>коэффициент покрытия</span><span class='pill'>экспорт / импорт</span><span class='pill'>граница баланса = 1</span>", unsafe_allow_html=True)
        st.dataframe(coverage_df.style.format({"РФ-Китай": "{:.2f}", "РФ-Индия": "{:.2f}"}), use_container_width=True)
    explain("Единицы измерения", "В исходных рядах денежные показатели хранятся в базовых единицах датасета, а на графиках приводятся к млрд долларов США для удобства чтения. Коэффициент покрытия является безразмерным отношением.")

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"<div class='small-muted'>&copy; 2026 {L('footer_copyright')}</div>", unsafe_allow_html=True)
