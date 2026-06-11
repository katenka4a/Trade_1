"""
Теоретические основы внешней торговли и статистического учета.
Страница заменяет прежний NLP-блок: содержит теорию из главы 1,
методологию учета России, Китая и Индии, а также интерактивный справочник Incoterms 2020.
"""

from __future__ import annotations

import math
import html
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Теоретические основы внешней торговли", page_icon=None, layout="wide")

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

st.markdown(
    """
<style>
html, body, [class*="css"] { font-family: 'Inter', sans-serif; color:#25312B; }
h1, h2, h3 { font-family: 'Source Sans Pro', 'Inter', sans-serif; font-weight:650; letter-spacing:-0.01em; color:#1A2A1F; }
.theory-hero { background:linear-gradient(135deg,#F5FAF6 0%,#FFFFFF 58%,#EEF7F0 100%); border:1px solid #D8E8DA; border-radius:18px; padding:1.35rem 1.55rem; margin-bottom:1rem; }
.section-box { background:#FFFFFF; border:1px solid #E3EDE5; border-radius:14px; padding:1.15rem 1.25rem; margin-bottom:1rem; box-shadow:0 1px 2px rgba(26,42,31,0.035); }
.soft-box { background:#F7FBF8; border:1px solid #DDEBDF; border-radius:14px; padding:1rem 1.15rem; margin-bottom:1rem; }
.warn-box { background:#FFF8E8; border:1px solid #EED99B; border-radius:14px; padding:1rem 1.15rem; margin-bottom:1rem; }
.card-grid { display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:0.8rem; margin:0.8rem 0 1rem 0; }
.info-card { background:#FFFFFF; border:1px solid #E3EDE5; border-radius:14px; padding:0.95rem 1rem; min-height:118px; }
.info-card-title { font-size:0.78rem; text-transform:uppercase; letter-spacing:0.07em; color:#6C7C70; margin-bottom:0.35rem; }
.info-card-main { font-size:1.2rem; font-weight:750; color:#1A2A1F; margin-bottom:0.25rem; }
.info-card-text { font-size:0.88rem; color:#526057; line-height:1.45; }
.badge { display:inline-block; border-radius:999px; padding:0.16rem 0.48rem; font-size:0.75rem; background:#EAF5ED; color:#2E6B3D; border:1px solid #CFE6D3; margin:0.08rem 0.18rem 0.08rem 0; }
.badge-warn { background:#FFF4D7; color:#7A5A12; border-color:#E7CF8B; }
.badge-dark { background:#E9ECEF; color:#495057; border-color:#D7DDE1; }
.badge-red { background:#FBEAEA; color:#9B2F2F; border-color:#E7C0C0; }
.small-muted { color:#6C7C70; font-size:0.86rem; line-height:1.5; }
.kpi-number { font-size:1.55rem; font-weight:760; color:#1A2A1F; }
.term-code { font-size:2rem; font-weight:800; letter-spacing:0.02em; color:#1F5B33; }
.term-name { color:#506057; font-size:0.95rem; margin-top:-0.25rem; }
.compact-list li { margin-bottom:0.32rem; }
.resp-seller { color:#2F6B3C; font-weight:650; }
.resp-buyer { color:#8A5A00; font-weight:650; }
.resp-split { color:#495057; font-weight:650; }
.source-card { background:#FFFFFF; border:1px solid #E3EDE5; border-radius:14px; padding:0.95rem 1rem; min-height:168px; box-shadow:0 1px 2px rgba(26,42,31,0.03); }
.source-card-title { font-size:1rem; font-weight:760; color:#183A29; margin-bottom:0.3rem; }
.source-card-desc { font-size:0.88rem; color:#526057; line-height:1.5; margin-bottom:0.6rem; }
.source-card-link a { color:#1E6B45 !important; font-weight:700; text-decoration:none; }
.source-card-link a:hover { text-decoration:underline; }
.legal-box { background:#F8FAFC; border:1px solid #DCE6EE; border-radius:14px; padding:1rem 1.1rem; margin-top:1rem; color:#4F5E68; font-size:0.88rem; line-height:1.55; }
.note-box { background:#F5FAF6; border:1px solid #DDEBDF; border-radius:12px; padding:0.9rem 1rem; margin-bottom:1rem; }
@media (max-width: 1000px) { .card-grid { grid-template-columns:repeat(2,minmax(0,1fr)); } }
@media (max-width: 640px) { .card-grid { grid-template-columns:1fr; } }
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# ДАННЫЕ INCOTERMS 2020
# -----------------------------------------------------------------------------

ROUTE_STEPS = [
    "Упаковка",
    "Погрузка у продавца",
    "Экспортное оформление",
    "Доставка до терминала отправления",
    "Погрузка на основной транспорт",
    "Основная перевозка",
    "Страхование",
    "Разгрузка в пункте назначения",
    "Импортное оформление и пошлины",
    "Финальная доставка",
]

@dataclass(frozen=True)
class Incoterm:
    code: str
    name: str
    ru_name: str
    transport: str
    group: str
    seller_level: int
    seller_pays_main: bool
    insurance_required: str
    export_clearance: str
    import_clearance: str
    risk_point: str
    delivery_point: str
    stat_logic: str
    seller_summary: str
    buyer_summary: str
    responsibility: list[str]

INCOTERMS: list[Incoterm] = [
    Incoterm(
        "EXW", "Ex Works", "Франко-завод", "Любой транспорт", "E", 1, False, "Нет",
        "Покупатель", "Покупатель", "На территории продавца, когда товар предоставлен покупателю.",
        "Склад/завод продавца", "Не является типичным статистическим базисом для внешнеторговой стоимости; транспортные расходы почти полностью вне цены продавца.",
        "Минимальные обязанности: подготовить товар, упаковку и предоставить его покупателю.",
        "Покупатель организует погрузку, экспорт, основную перевозку, импорт и финальную доставку.",
        ["S", "B", "B", "B", "B", "B", "B", "B", "B", "B"],
    ),
    Incoterm(
        "FCA", "Free Carrier", "Франко-перевозчик", "Любой транспорт", "F", 3, False, "Нет",
        "Продавец", "Покупатель", "Когда товар передан перевозчику или иному лицу в названном месте.",
        "Названное место передачи перевозчику", "Используется как базис оценки экспорта при перевозках не морским транспортом: стоимость до пункта передачи перевозчику.",
        "Оформляет экспорт и передает товар перевозчику в согласованном месте.",
        "Оплачивает основную перевозку, страхование при необходимости, импорт и дальнейшую доставку.",
        ["S", "D", "S", "S", "B", "B", "B", "B", "B", "B"],
    ),
    Incoterm(
        "FAS", "Free Alongside Ship", "Свободно вдоль борта судна", "Морской и внутренний водный", "F", 3, False, "Нет",
        "Продавец", "Покупатель", "Когда товар размещен вдоль борта судна в порту отгрузки.",
        "Причал/лихтер вдоль борта судна", "Морской термин; близок к экспортной стоимости до порта отгрузки, но не равен FOB, так как погрузка на судно еще не включена.",
        "Доставляет товар к борту судна и выполняет экспортное оформление.",
        "Организует погрузку на судно, фрахт, страхование, импорт и финальную доставку.",
        ["S", "S", "S", "S", "B", "B", "B", "B", "B", "B"],
    ),
    Incoterm(
        "FOB", "Free On Board", "Свободно на борту", "Морской и внутренний водный", "F", 4, False, "Нет",
        "Продавец", "Покупатель", "Когда товар погружен на борт судна в порту отгрузки.",
        "Борт судна в порту отправления", "Классический базис статистической оценки экспорта при морских перевозках: стоимость товара до момента погрузки на судно.",
        "Оформляет экспорт и обеспечивает доставку/погрузку товара на борт судна.",
        "Оплачивает фрахт, страхование при необходимости, импорт и дальнейшую доставку.",
        ["S", "S", "S", "S", "S", "B", "B", "B", "B", "B"],
    ),
    Incoterm(
        "CFR", "Cost and Freight", "Стоимость и фрахт", "Морской и внутренний водный", "C", 6, True, "Нет",
        "Продавец", "Покупатель", "Риск переходит на борту судна в порту отгрузки, хотя фрахт до порта назначения оплачивает продавец.",
        "Порт назначения, но риск — на судне в порту отправления", "В стоимости присутствует фрахт до порта назначения, поэтому для экспортной статистики требует приведения к FOB при необходимости.",
        "Оформляет экспорт, грузит товар на судно и оплачивает фрахт до порта назначения.",
        "Несет риск после погрузки на судно, организует страхование при необходимости, импорт и доставку после порта назначения.",
        ["S", "S", "S", "S", "S", "S", "B", "B", "B", "B"],
    ),
    Incoterm(
        "CIF", "Cost, Insurance and Freight", "Стоимость, страхование и фрахт", "Морской и внутренний водный", "C", 7, True, "Да, минимальное",
        "Продавец", "Покупатель", "Риск переходит на борту судна в порту отгрузки, несмотря на оплату фрахта и страховки до порта назначения.",
        "Порт назначения, но риск — на судне в порту отправления", "Классический базис статистической оценки импорта при морских перевозках: стоимость товара + страхование + фрахт до порта ввоза.",
        "Оформляет экспорт, грузит товар, оплачивает фрахт и минимальное страхование до порта назначения.",
        "Несет риск после погрузки на судно, оформляет импорт и доставку после порта назначения.",
        ["S", "S", "S", "S", "S", "S", "S", "B", "B", "B"],
    ),
    Incoterm(
        "CPT", "Carriage Paid To", "Перевозка оплачена до", "Любой транспорт", "C", 6, True, "Нет",
        "Продавец", "Покупатель", "Когда товар передан первому перевозчику; расходы до названного места назначения оплачивает продавец.",
        "Названное место назначения, но риск — при передаче перевозчику", "Стоимость включает перевозку до названного места; при статистической оценке может требовать пересчета к FOB/FCA или CIF/CIP в зависимости от потока.",
        "Оформляет экспорт и оплачивает перевозку до согласованного места назначения.",
        "Несет риск после передачи первому перевозчику, страхует при необходимости и оформляет импорт.",
        ["S", "S", "S", "S", "S", "S", "B", "B", "B", "B"],
    ),
    Incoterm(
        "CIP", "Carriage and Insurance Paid To", "Перевозка и страхование оплачены до", "Любой транспорт", "C", 7, True, "Да, расширенное",
        "Продавец", "Покупатель", "Когда товар передан первому перевозчику; перевозка и страхование до места назначения оплачены продавцом.",
        "Названное место назначения, но риск — при передаче перевозчику", "Используется как базис оценки импорта при неморских перевозках: стоимость товара + перевозка + страхование до пункта ввоза.",
        "Оформляет экспорт, оплачивает перевозку и расширенное страхование до названного места назначения.",
        "Несет риск после передачи перевозчику, оформляет импорт и дальнейшую доставку после названного места.",
        ["S", "S", "S", "S", "S", "S", "S", "B", "B", "B"],
    ),
    Incoterm(
        "DAP", "Delivered At Place", "Поставка в месте назначения", "Любой транспорт", "D", 8, True, "Нет",
        "Продавец", "Покупатель", "В названном месте назначения, когда товар готов к разгрузке.",
        "Названное место назначения, без разгрузки", "Стоимость включает существенную часть логистики до места назначения; для статистики требует понимания, какие расходы входят в цену.",
        "Доставляет товар до названного места назначения и несет риск до момента готовности к разгрузке.",
        "Разгружает товар, оформляет импорт, платит пошлины и налоги.",
        ["S", "S", "S", "S", "S", "S", "D", "B", "B", "S"],
    ),
    Incoterm(
        "DPU", "Delivered at Place Unloaded", "Поставка в месте назначения с разгрузкой", "Любой транспорт", "D", 9, True, "Нет",
        "Продавец", "Покупатель", "После разгрузки товара в названном месте назначения.",
        "Названное место назначения после разгрузки", "Включает доставку и разгрузку; важно отделять товарную стоимость от расходов после границы при сопоставлениях.",
        "Доставляет товар и выполняет разгрузку в названном месте назначения.",
        "Оформляет импорт, платит пошлины/налоги и принимает товар после разгрузки.",
        ["S", "S", "S", "S", "S", "S", "D", "S", "B", "S"],
    ),
    Incoterm(
        "DDP", "Delivered Duty Paid", "Поставка с оплатой пошлин", "Любой транспорт", "D", 10, True, "Нет",
        "Продавец", "Продавец", "В названном месте назначения, когда товар готов к разгрузке и импортные формальности выполнены.",
        "Названное место назначения после импортного оформления", "Максимально насыщенная расходами цена; для статистики требует аккуратного выделения таможенной стоимости и логистических компонентов.",
        "Максимальные обязанности: доставка до места назначения, импортное оформление, пошлины и налоги.",
        "Принимает товар в месте назначения и обычно отвечает за разгрузку, если иное не согласовано.",
        ["S", "S", "S", "S", "S", "S", "D", "B", "S", "S"],
    ),
]

TERM_DF = pd.DataFrame([t.__dict__ for t in INCOTERMS])
TERM_BY_CODE = {t.code: t for t in INCOTERMS}

OFFICIAL_SOURCES = {
    "Россия": [
        {
            "name": "Росстат",
            "url": "https://rosstat.gov.ru/",
            "desc": "Официальная государственная статистика: макроэкономика, внешняя торговля, ежегодники и агрегированные показатели.",
        },
        {
            "name": "ФТС России",
            "url": "https://customs.gov.ru/",
            "desc": "Таможенная статистика экспорта и импорта, товарная и страновая структура, методические материалы.",
        },
        {
            "name": "Банк России",
            "url": "https://www.cbr.ru/",
            "desc": "Платежный баланс, внешнеэкономические операции, валютные и финансовые показатели внешнего сектора.",
        },
        {
            "name": "ЕМИСС",
            "url": "https://www.fedstat.ru/",
            "desc": "Единая межведомственная информационно-статистическая система с агрегированными государственными данными.",
        },
    ],
    "Китай": [
        {
            "name": "National Bureau of Statistics of China (NBS)",
            "url": "https://www.stats.gov.cn/english/",
            "desc": "Национальная статистика Китая: годовые, квартальные и ежемесячные макроэкономические данные.",
        },
        {
            "name": "General Administration of Customs of China (GACC)",
            "url": "http://english.customs.gov.cn/",
            "desc": "Таможенная статистика торговли, данные по экспортно-импортным потокам и товарным группам.",
        },
        {
            "name": "Ministry of Commerce of the PRC (MOFCOM)",
            "url": "https://english.mofcom.gov.cn/",
            "desc": "Материалы по внешнеторговой политике, соглашениям, пресс-релизам и официальным обзорам торговли.",
        },
    ],
    "Индия": [
        {
            "name": "Ministry of Commerce & Industry",
            "url": "https://www.commerce.gov.in/",
            "desc": "Торговая политика, официальные документы, обзоры и материалы по внешней торговле Индии.",
        },
        {
            "name": "DGCI&S",
            "url": "https://www.dgciskol.gov.in/",
            "desc": "Статистика внешней торговли, аналитика товарных потоков и официальный портал распространения данных.",
        },
        {
            "name": "DGFT",
            "url": "https://www.dgft.gov.in/CP/",
            "desc": "Регулирование внешней торговли, лицензирование, экспортно-импортные сервисы и регуляторные документы.",
        },
        {
            "name": "Reserve Bank of India (RBI)",
            "url": "https://www.rbi.org.in/",
            "desc": "Платежный баланс, валютные и финансовые показатели внешнего сектора Индии.",
        },
    ],
}

RESP_LABEL = {"S": "Продавец", "B": "Покупатель", "D": "Зависит от места/контракта"}
RESP_SYMBOL = {"S": "●", "B": "●", "D": "◐"}
RESP_COLOR = {"S": "#2F7D45", "B": "#C07A00", "D": "#6C757D"}

# -----------------------------------------------------------------------------
# ФУНКЦИИ РЕНДЕРА
# -----------------------------------------------------------------------------

def render_top_header() -> None:
    col1, col2 = st.columns([7, 1])
    with col2:
        if render_lang_switcher:
            render_lang_switcher()

    st.markdown(
        """
<div class="theory-hero">
  <div style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.08em; color:#6C7C70; margin-bottom:0.35rem;">Теоретическая база проекта</div>
  <h1 style="margin:0;">Теоретические основы внешней торговли</h1>
  <p style="color:#536258; margin:0.45rem 0 0 0; max-width:980px;">
    Страница объединяет ключевые понятия внешней торговли, правила Incoterms 2020,
    систему показателей и методологию организации статистических баз России, Китая и Индии.
    Это методологический справочник для последующего анализа структуры, динамики и прогноза торговых потоков.
  </p>
</div>
""",
        unsafe_allow_html=True,
    )

def render_cards(cards: list[tuple[str, str, str]]) -> None:
    """Безопасный рендер карточек.

    Старый вариант собирал всю сетку одним HTML-блоком. В Streamlit при некоторых
    сочетаниях markdown/HTML это может приводить к тому, что часть <div>
    показывается как обычный текст. Здесь каждая карточка выводится отдельно
    внутри st.columns, поэтому HTML не «разрывается» между элементами страницы.
    """
    if not cards:
        return

    # Разбиваем на строки по 4 карточки, чтобы блок был устойчивым на любых экранах.
    for start in range(0, len(cards), 4):
        row = cards[start:start + 4]
        cols = st.columns(len(row))
        for col, (title, main, text) in zip(cols, row):
            with col:
                st.markdown(
                    f"""
                    <div class="info-card">
                        <div class="info-card-title">{html.escape(str(title))}</div>
                        <div class="info-card-main">{html.escape(str(main))}</div>
                        <div class="info-card-text">{html.escape(str(text))}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

def render_formula_box(title: str, formula: str, comment: str) -> None:
    st.markdown(f"""
    <div class="section-box">
        <div style="font-weight:700; margin-bottom:0.35rem;">{title}</div>
        <div style="background:#F8FAF8; border:1px solid #E3EDE5; border-radius:10px; padding:0.75rem 0.9rem; margin-bottom:0.45rem; font-size:1.05rem;">
            <code>{formula}</code>
        </div>
        <div class="small-muted">{comment}</div>
    </div>
    """, unsafe_allow_html=True)

def render_source_links(country: str) -> None:
    sources = OFFICIAL_SOURCES.get(country, [])
    if not sources:
        return
    cols = st.columns(2)
    for idx, source in enumerate(sources):
        with cols[idx % 2]:
            st.markdown(
                f"""
                <div class="source-card">
                    <div class="source-card-title">{html.escape(source['name'])}</div>
                    <div class="source-card-desc">{html.escape(source['desc'])}</div>
                    <div class="source-card-link"><a href="{html.escape(source['url'])}" target="_blank">Открыть официальный сайт ↗</a></div>
                </div>
                """,
                unsafe_allow_html=True,
            )

def render_legal_notice() -> None:
    st.markdown(
        """
<div class="legal-box">
<b>Важно.</b> Проект подготовлен исключительно в <b>учебных и исследовательских целях</b>.
Все наименования ведомств, статистические базы и иллюстрации используются
для академической демонстрации методологии анализа внешней торговли, а не для коммерческого использования.
При подготовке страницы соблюдаются принципы добросовестного использования материалов, уважения авторских прав
и обязательного указания официальных источников данных. При повторном использовании материалов проекта рекомендуется
дополнительно проверять актуальность ссылок, методологических пояснений и условий использования контента на сайтах ведомств.
</div>
""",
        unsafe_allow_html=True,
    )

def render_trade_basics() -> None:
    st.markdown("### 1. Что изучает статистика внешней торговли")
    st.markdown(
        """
<div class="section-box">
Внешняя торговля — это обмен товарами, услугами и правами интеллектуальной собственности между хозяйствующими субъектами разных стран.
В рамках данного проекта основной акцент сделан на <b>товарной торговле</b>: экспортных и импортных потоках России с Китаем и Индией,
их структуре, динамике, торговом балансе и прогнозировании до 2030 года.
</div>
""",
        unsafe_allow_html=True,
    )
    render_cards([
        ("Поток 1", "Экспорт", "Вывоз товаров из страны. Для России это прежде всего сырьевые, энергетические и отдельные несырьевые поставки."),
        ("Поток 2", "Импорт", "Ввоз товаров в страну: оборудование, электроника, транспорт, фармацевтика, потребительские товары и комплектующие."),
        ("Итог масштаба", "Оборот", "Сумма экспорта и импорта. Показывает общий размер торгового взаимодействия с партнёром."),
        ("Итог баланса", "Сальдо", "Разница между экспортом и импортом. Положительное сальдо означает превышение экспорта над импортом."),
    ])

    st.markdown("### 2. Базовые показатели")
    formulas = pd.DataFrame([
        {"Показатель": "Внешнеторговый оборот", "Формула": "ВТО = Э + И", "Интерпретация": "Общий объём торговли страны с партнёром."},
        {"Показатель": "Сальдо торгового баланса", "Формула": "С = Э − И", "Интерпретация": "Показывает профицит или дефицит торговли."},
        {"Показатель": "Коэффициент покрытия", "Формула": "Кп = Э / И × 100%", "Интерпретация": "Насколько экспортная выручка покрывает импортные закупки."},
        {"Показатель": "Темп роста", "Формула": "Тр = yₜ / yₜ₋₁ × 100%", "Интерпретация": "Скорость изменения показателя во времени."},
        {"Показатель": "Коэффициент опережения", "Формула": "Коп = Тр₁ / Тр₂", "Интерпретация": "Сравнивает скорость роста двух рядов динамики."},
    ])
    st.dataframe(formulas, use_container_width=True, hide_index=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        render_formula_box("Оборот", "ВТО = Э + И", "Используется для сравнения общего масштаба торговли России с Китаем и Индией.")
    with c2:
        render_formula_box("Сальдо", "С = Э − И", "Позволяет увидеть, является ли торговля профицитной или дефицитной.")
    with c3:
        render_formula_box("Покрытие", "Кп = Э / И × 100%", "Если показатель выше 100%, экспорт превышает импорт.")

def render_incoterms_timeline(term: Incoterm) -> None:
    y = [0] * len(ROUTE_STEPS)
    colors = [RESP_COLOR[v] for v in term.responsibility]
    symbols = [RESP_SYMBOL[v] for v in term.responsibility]
    hover = [f"{step}<br>Ответственность: {RESP_LABEL[v]}" for step, v in zip(ROUTE_STEPS, term.responsibility)]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=list(range(len(ROUTE_STEPS))),
        y=y,
        mode="lines",
        line=dict(color="#CBD9CE", width=6),
        hoverinfo="skip",
        showlegend=False,
    ))
    fig.add_trace(go.Scatter(
        x=list(range(len(ROUTE_STEPS))),
        y=y,
        mode="markers+text",
        marker=dict(size=22, color=colors, line=dict(color="#FFFFFF", width=2)),
        text=symbols,
        textfont=dict(color="#FFFFFF", size=10),
        hovertext=hover,
        hoverinfo="text",
        showlegend=False,
    ))
    for i, step in enumerate(ROUTE_STEPS):
        fig.add_annotation(x=i, y=-0.18 if i % 2 == 0 else 0.18, text=step, showarrow=False, font=dict(size=10, color="#3F4E44"), textangle=-25 if i % 2 == 0 else 25)
    fig.update_layout(
        height=260,
        template="plotly_white",
        margin=dict(l=10, r=10, t=10, b=40),
        xaxis=dict(visible=False, range=[-0.5, len(ROUTE_STEPS) - 0.5]),
        yaxis=dict(visible=False, range=[-0.55, 0.55]),
        plot_bgcolor="#FFFFFF",
    )
    st.plotly_chart(fig, use_container_width=True, key=f"timeline_{term.code}")

def term_badges(term: Incoterm) -> str:
    pay = "продавец оплачивает перевозку" if term.seller_pays_main else "покупатель оплачивает перевозку"
    ins_class = "badge" if "Да" in term.insurance_required else "badge-dark"
    return (
        f"<span class='badge'>Группа {term.group}</span>"
        f"<span class='badge'>{term.transport}</span>"
        f"<span class='badge-warn badge'>{pay}</span>"
        f"<span class='{ins_class}'>{'страхование: ' + term.insurance_required}</span>"
    )

def render_incoterms_interactive() -> None:
    st.markdown("### Incoterms 2020: интерактивный справочник условий поставки")
    st.markdown(
        """
<div class="section-box">
<b>Incoterms</b> — международные правила толкования условий поставки. Они распределяют между продавцом и покупателем обязанности,
расходы и момент перехода риска. Важно: Incoterms не определяют переход права собственности на товар и не заменяют внешнеторговый контракт,
а только стандартизируют логистическую часть сделки.
</div>
""",
        unsafe_allow_html=True,
    )

    render_cards([
        ("Всего правил", "11", "Правила Incoterms 2020 делятся на универсальные и морские."),
        ("Экспортная оценка", "FOB / FCA", "Экспорт обычно приводится к стоимости до пункта вывоза или передачи перевозчику."),
        ("Импортная оценка", "CIF / CIP", "Импорт включает стоимость товара, перевозки и страхования до пункта ввоза."),
        ("Ключевой риск", "FOB ≠ CIF", "Из-за разных базисов оценки данные экспортёра и импортёра могут расходиться."),
    ])

    st.markdown("#### Навигатор по правилам")
    f1, f2, f3, f4 = st.columns([1.2, 1.2, 1, 1])
    with f1:
        mode_filter = st.selectbox("Тип транспорта", ["Все", "Любой транспорт", "Морской и внутренний водный"], key="incoterms_mode")
    with f2:
        group_filter = st.selectbox("Группа", ["Все", "E", "F", "C", "D"], key="incoterms_group")
    with f3:
        main_carriage_filter = st.selectbox("Основная перевозка", ["Все", "Оплачивает продавец", "Оплачивает покупатель"], key="incoterms_main")
    with f4:
        insurance_filter = st.selectbox("Страхование", ["Все", "Требуется", "Не требуется"], key="incoterms_insurance")

    filtered = TERM_DF.copy()
    if mode_filter != "Все":
        filtered = filtered[filtered["transport"] == mode_filter]
    if group_filter != "Все":
        filtered = filtered[filtered["group"] == group_filter]
    if main_carriage_filter != "Все":
        flag = main_carriage_filter == "Оплачивает продавец"
        filtered = filtered[filtered["seller_pays_main"] == flag]
    if insurance_filter != "Все":
        flag = insurance_filter == "Требуется"
        filtered = filtered[filtered["insurance_required"].str.contains("Да") == flag]

    if len(filtered) == 0:
        st.warning("По выбранным фильтрам правила не найдены. Измени условия фильтрации.")
        filtered = TERM_DF.copy()

    options = [f"{row.code} — {row.name} / {row.ru_name}" for row in filtered.itertuples(index=False)]
    selected_label = st.selectbox("Выбери правило Incoterms", options, key="selected_incoterm")
    selected_code = selected_label.split(" — ")[0]
    term = TERM_BY_CODE[selected_code]

    st.markdown("---")
    left, right = st.columns([1, 1.55])
    with left:
        st.markdown(f"""
        <div class="section-box">
            <div class="term-code">{term.code}</div>
            <div class="term-name">{term.name} · {term.ru_name}</div>
            <div style="margin-top:0.7rem;">{term_badges(term)}</div>
            <hr style="border:none; border-top:1px solid #E3EDE5; margin:0.9rem 0;" />
            <div class="small-muted"><b>Пункт поставки:</b><br>{term.delivery_point}</div><br>
            <div class="small-muted"><b>Переход риска:</b><br>{term.risk_point}</div>
        </div>
        """, unsafe_allow_html=True)
        k1, k2 = st.columns(2)
        k1.metric("Уровень обязанностей продавца", f"{term.seller_level}/10")
        k2.metric("Группа", term.group)
    with right:
        st.markdown("##### Карта ответственности по этапам поставки")
        st.caption("Зелёный — зона продавца, оранжевый — зона покупателя, серый — зависит от места поставки и условий контракта.")
        render_incoterms_timeline(term)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
        <div class="soft-box">
            <b>Обязанности продавца</b><br>
            <span class="small-muted">{term.seller_summary}</span>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="soft-box">
            <b>Обязанности покупателя</b><br>
            <span class="small-muted">{term.buyer_summary}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="warn-box">
        <b>Связь со статистикой внешней торговли:</b><br>
        {term.stat_logic}
    </div>
    """, unsafe_allow_html=True)

    resp_df = pd.DataFrame({
        "Этап поставки": ROUTE_STEPS,
        "Ответственная сторона": [RESP_LABEL[x] for x in term.responsibility],
    })
    st.dataframe(resp_df, use_container_width=True, hide_index=True, key=f"resp_df_{term.code}")

    st.markdown("#### Все правила Incoterms 2020")
    compact = TERM_DF[["code", "name", "ru_name", "transport", "group", "seller_pays_main", "insurance_required", "export_clearance", "import_clearance", "delivery_point"]].copy()
    compact.columns = ["Код", "Название", "Русское название", "Транспорт", "Группа", "Продавец оплачивает основную перевозку", "Страхование", "Экспортное оформление", "Импортное оформление", "Пункт поставки"]
    compact["Продавец оплачивает основную перевозку"] = compact["Продавец оплачивает основную перевозку"].map({True: "Да", False: "Нет"})
    st.dataframe(compact, use_container_width=True, hide_index=True, key="all_incoterms_table")

    with st.expander("Подобрать правило под сценарий сделки", expanded=False):
        s1, s2, s3, s4 = st.columns(4)
        with s1:
            scenario_mode = st.radio("Транспорт", ["Любой", "Морской"], horizontal=True, key="scenario_mode")
        with s2:
            seller_can_pay = st.checkbox("Продавец готов оплатить основную перевозку", value=True, key="scenario_pay")
        with s3:
            need_insurance = st.checkbox("Нужно обязательное страхование продавцом", value=False, key="scenario_ins")
        with s4:
            seller_import = st.checkbox("Продавец готов оформить импорт", value=False, key="scenario_import")

        rec = TERM_DF.copy()
        if scenario_mode == "Морской":
            rec = rec[rec["transport"].isin(["Морской и внутренний водный", "Любой транспорт"])]
        if seller_can_pay:
            rec = rec[rec["seller_pays_main"]]
        else:
            rec = rec[~rec["seller_pays_main"]]
        if need_insurance:
            rec = rec[rec["insurance_required"].str.contains("Да")]
        if seller_import:
            rec = rec[rec["import_clearance"] == "Продавец"]
        if len(rec) == 0:
            st.info("По такому набору условий точного правила нет. Обычно нужно ослабить одно из требований или прописать дополнительное условие в контракте.")
        else:
            rec_view = rec[["code", "name", "ru_name", "transport", "group", "delivery_point", "risk_point"]].copy()
            rec_view.columns = ["Код", "Название", "Русское название", "Транспорт", "Группа", "Поставка", "Переход риска"]
            st.dataframe(rec_view, use_container_width=True, hide_index=True, key="incoterms_recommendation")

def render_country_infographic_split() -> None:
    """Показывает три отдельные PNG-инфографики по статистическим базам стран.

    Основные ожидаемые файлы в локальном проекте:
    - Иллюстрации/статистика_внешней_торговли_россии.png
    - Иллюстрации/статистика_внешней_торговли_китая.png
    - Иллюстрации/статистика_внешней_торговли_индии.png
    """
    image_specs = [
        (
            "Россия",
            [
                "статистика_внешней_торговли_россии.png",
                "statistical_databases_for_foreign_trade_in_russia.png",
                "статистические_базы_россия.png",
            ],
        ),
        (
            "Китай",
            [
                "статистика_внешней_торговли_китая.png",
                "статистические_базы_китай.png",
                "statistical_databases_china.png",
            ],
        ),
        (
            "Индия",
            [
                "статистика_внешней_торговли_индии.png",
                "статистические_базы_индия.png",
                "statistical_databases_india.png",
            ],
        ),
    ]

    cols = st.columns(3)
    for col, (country, filenames) in zip(cols, image_specs):
        with col:
            found = None
            for filename in filenames:
                found = find_illustration_path(filename)
                if found is not None:
                    break
            if found is not None:
                st.image(str(found), caption=country, use_container_width=True)
            else:
                st.warning(f"Не найдена инфографика для страны: {country}")
                st.code("Иллюстрации/" + filenames[0], language="text")

def render_statistics_basis() -> None:
    st.markdown("### Организация статистических баз России, Китая и Индии")
    st.markdown(
        """
<div class="section-box">
Статистика внешней торговли формируется на основе документов, фиксирующих перемещение товаров через границу,
их стоимость, страну происхождения или назначения, код товарной классификации и условия поставки. Для сопоставимого анализа важно понимать,
какие органы собирают данные, где публикуются официальные показатели и как различается методология по странам.
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="note-box">
<b>Как читать этот раздел:</b> сначала показана визуальная карта основных официальных источников,
а ниже — три отдельные инфографики по странам и пояснения к методологии, зачем каждая база нужна в исследовании.
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown("#### Визуальная карта статистических баз по странам")
    st.markdown(
        """
<div class="soft-box">
Ниже показаны три отдельные инфографики — по России, Китаю и Индии. В каждой карточке под аббревиатурой дана расшифровка названия ведомства и его роль в статистике внешней торговли.
</div>
""",
        unsafe_allow_html=True,
    )
    render_country_infographic_split()

    country_tabs = st.tabs(["Россия", "Китай", "Индия", "Сравнение"])

    with country_tabs[0]:
        render_cards([
            ("Регулирование", "ЕАЭС + РФ", "Методология строится на таможенном регулировании ЕАЭС и российских нормативных актах."),
            ("Основные источники", "ФТС / Росстат", "ФТС ведёт таможенную статистику, Росстат публикует агрегированные показатели."),
            ("Дополнительный контур", "Банк России", "Используется для платежного баланса и досчётов по внешнеторговым операциям."),
            ("Особенность", "после 2022", "Часть детализированных данных по странам и товарным группам ограничена в открытом доступе."),
        ])
        st.markdown(
            """
<div class="section-box">
<b>Россия.</b> Импорт учитывается преимущественно по стране происхождения товара, экспорт — по стране назначения.
Для экспорта применяются базисы FOB/FCA, для импорта — CIF/CIP. При торговле внутри ЕАЭС используется методология,
связанная с учетом взаимной торговли и зеркальной статистикой.
</div>
""",
            unsafe_allow_html=True,
        )
    with country_tabs[1]:
        render_cards([
            ("Статистический орган", "NBS China", "Национальное бюро статистики Китая публикует агрегированные статистические ежегодники."),
            ("Таможенный контур", "GACC", "Главное таможенное управление КНР собирает данные по товарным потокам."),
            ("Валюты публикации", "RMB / USD", "Данные могут публиковаться в юанях и долларах США."),
            ("Особенность", "SAR отдельно", "Гонконг, Макао и Тайвань часто рассматриваются отдельно в статистических публикациях."),
        ])
        st.markdown(
            """
<div class="section-box">
<b>Китай.</b> Методология внешнеторговой статистики опирается на данные таможенного управления и международные классификации товаров
HS и SITC. Экспорт обычно оценивается по FOB, импорт — по CIF. Отдельный учет специальных административных регионов важен при сравнении
статистики Китая с данными торговых партнеров.
</div>
""",
            unsafe_allow_html=True,
        )
    with country_tabs[2]:
        render_cards([
            ("Регулятор торговли", "DGFT", "Генеральный директорат внешней торговли связан с лицензированием и политикой торговли."),
            ("Торговая статистика", "DGCI&S", "Отвечает за статистику торгового баланса и обработку данных о товарных потоках."),
            ("Платежный контур", "RBI", "Резервный банк Индии формирует данные платежного баланса."),
            ("Документы", "Shipping Bill", "Используются Shipping Bill, Bill of Lading, Bill of Entry и таможенные декларации."),
        ])
        st.markdown(
            """
<div class="section-box">
<b>Индия.</b> Статистика внешней торговли формируется через несколько административных контуров: лицензирование,
учет фактического перемещения товаров и учет платежей. В статистике преимущественно отражаются коммерческие операции с товарами;
часть оборонных, транзитных и некоммерческих операций может не включаться в стандартные публикации.
</div>
""",
            unsafe_allow_html=True,
        )
    with country_tabs[3]:
        comparison = pd.DataFrame([
            {"Критерий": "Основные органы", "Россия": "ФТС, Росстат, Банк России", "Китай": "GACC, NBS, MOFCOM", "Индия": "DGCI&S, DGFT, RBI"},
            {"Критерий": "Экспортная оценка", "Россия": "FOB/FCA", "Китай": "FOB", "Индия": "обычно FOB"},
            {"Критерий": "Импортная оценка", "Россия": "CIF/CIP", "Китай": "CIF", "Индия": "обычно CIF"},
            {"Критерий": "Классификации", "Россия": "ТН ВЭД ЕАЭС / HS", "Китай": "HS / SITC", "Индия": "ITC(HS)"},
            {"Критерий": "Особенность", "Россия": "ограничение части данных после 2022", "Китай": "отдельный учет SAR", "Индия": "несколько административных источников"},
            {"Критерий": "Риск сопоставимости", "Россия": "закрытые товарные категории", "Китай": "региональные особенности учета", "Индия": "исключения по некоммерческим и оборонным операциям"},
        ])
        st.dataframe(comparison, use_container_width=True, hide_index=True)

    render_legal_notice()

def render_methodological_limits() -> None:
    st.markdown("### Методологические ограничения и причины расхождений")
    st.markdown(
        """
<div class="section-box">
Даже если две страны описывают одну и ту же сделку, их статистические данные могут отличаться.
Это нормально для международной торговли: показатели зависят от базиса оценки, момента учета, классификации товара и национальной методологии.
</div>
""",
        unsafe_allow_html=True,
    )
    limits = pd.DataFrame([
        {"Причина": "FOB против CIF", "Смысл": "Импортная стоимость обычно включает перевозку и страхование, экспортная — нет."},
        {"Причина": "Разный момент учета", "Смысл": "Экспорт может быть учтен в одном месяце, импорт партнером — в другом."},
        {"Причина": "Страна происхождения и страна отправления", "Смысл": "При реэкспорте страна отправления может отличаться от страны происхождения товара."},
        {"Причина": "Классификация товаров", "Смысл": "Один и тот же товар может быть классифицирован по-разному на уровне детализации кодов."},
        {"Причина": "Статистические пороги", "Смысл": "Мелкие поставки могут не попадать в учет или агрегироваться."},
        {"Причина": "Конфиденциальность", "Смысл": "Часть чувствительных товарных групп может скрываться или публиковаться в укрупненном виде."},
        {"Причина": "Транзит и реэкспорт", "Смысл": "Товары могут проходить через третьи страны и искажать географическую структуру торговли."},
    ])
    st.dataframe(limits, use_container_width=True, hide_index=True, key="methodological_limits")

    st.markdown(
        """
<div class="soft-box">
<b>Как это связано с проектом:</b> теоретическая база используется при расчете оборота, сальдо и коэффициента покрытия,
при сравнении России с Китаем и Индией, при интерпретации товарной структуры и при построении прогнозных моделей.
</div>
""",
        unsafe_allow_html=True,
    )

def find_illustration_path(filename: str) -> Path | None:
    """Ищет PNG-иллюстрацию в локальной папке проекта.

    Основной ожидаемый путь для локального проекта:
    <корень проекта>/Иллюстрации/<filename>

    Функция также проверяет несколько запасных путей, чтобы страница работала
    и когда файл лежит рядом со страницей, и когда страница находится в папке pages.
    """
    page_dir = Path(__file__).resolve().parent
    candidates = [
        page_dir / "Иллюстрации" / filename,
        page_dir.parent / "Иллюстрации" / filename,
        Path.cwd() / "Иллюстрации" / filename,
        page_dir / "assets" / "Иллюстрации" / filename,
        page_dir.parent / "assets" / "Иллюстрации" / filename,
        page_dir / filename,
        Path.cwd() / filename,
    ]
    for path in candidates:
        if path.exists() and path.is_file():
            return path
    return None

def render_process_scheme() -> None:
    st.markdown("### Как товар превращается в статистическое наблюдение")
    st.markdown(
        """
<div class="section-box">
<b>Логика статистического наблюдения:</b> внешнеторговая операция начинается с контракта и условий Incoterms,
затем товар пересекает границу, проходит таможенное оформление, получает код ТН ВЭД / HS, страну происхождения
или назначения и стоимостную оценку. После этого сведения агрегируются и публикуются в официальной статистике.
</div>
""",
        unsafe_allow_html=True,
    )

    image_filename = "как_товар_превращается_в_статистику.png"
    image_path = find_illustration_path(image_filename)

    if image_path is not None:
        st.image(
            str(image_path),
            caption="Путь внешнеторговой сделки от контракта до публикации официальных данных",
            use_container_width=True,
        )
    else:
        st.warning(
            "PNG-инфографика не найдена. Создайте в корне проекта папку «Иллюстрации» "
            f"и положите туда файл: {image_filename}"
        )
        st.code(f"Иллюстрации/{image_filename}", language="text")

# -----------------------------------------------------------------------------
# ОСНОВНОЙ РЕНДЕР
# -----------------------------------------------------------------------------

render_top_header()

tab_overview, tab_incoterms, tab_stats, tab_limits = st.tabs([
    "Основы внешней торговли",
    "Incoterms 2020",
    "Статистические базы",
    "Сопоставимость данных",
])

with tab_overview:
    render_trade_basics()
    render_process_scheme()

with tab_incoterms:
    render_incoterms_interactive()

with tab_stats:
    render_statistics_basis()

with tab_limits:
    render_methodological_limits()

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='font-size:0.78rem; color:#9AA6A0;'>&copy; 2026 · Теоретическая база статистического анализа внешней торговли России, Китая и Индии · Учебный некоммерческий проект с указанием официальных источников</div>", unsafe_allow_html=True)
