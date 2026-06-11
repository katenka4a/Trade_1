# -*- coding: utf-8 -*-
"""
О проекте — вводная страница электронного приложения к ВКР.
"""
import streamlit as st

st.set_page_config(page_title="О проекте", page_icon=None, layout="wide")

try:
    from utils import setup_i18n, render_lang_switcher, L
    setup_i18n()
except Exception:
    render_lang_switcher = None
    def L(key: str) -> str:
        return key

try:
    from data.locales import install_streamlit_i18n, translate_text as TT
    install_streamlit_i18n(st)
except Exception:
    def TT(value):
        return value

st.markdown("""
<style>
html, body, [class*="css"] { font-family:'Inter',sans-serif; color:#20242A; }
.stApp { background:#FFFFFF; }
h1, h2, h3 { font-family:'Source Sans Pro','Inter',sans-serif; font-weight:700; letter-spacing:-0.02em; color:#121826; }
.hero {
    background: linear-gradient(135deg,#F8FBF8 0%,#FFFFFF 58%,#F8FAFC 100%);
    border:1px solid #E2E8F0; border-radius:18px; padding:1.35rem 1.55rem; margin-bottom:1rem;
    box-shadow:0 8px 22px rgba(15,23,42,0.035);
}
.kicker { font-size:0.75rem; text-transform:uppercase; letter-spacing:0.10em; color:#64748B; font-weight:800; margin-bottom:0.35rem; }
.hero-title { font-size:2.2rem; line-height:1.08; margin:0; color:#121826; }
.hero-subtitle { color:#52606D; margin-top:0.58rem; max-width:1120px; font-size:1rem; line-height:1.58; }
.section-head { margin-top:1.3rem; margin-bottom:0.65rem; }
.section-head h2 { margin:0; font-size:1.32rem; }
.section-head p { margin:0.35rem 0 0 0; color:#64748B; line-height:1.5; }
.card, .source-card, .task-card {
    background:#FFFFFF; border:1px solid #E5EAF0; border-radius:14px; padding:1rem 1.1rem;
    box-shadow:0 6px 18px rgba(15,23,42,0.025); margin-bottom:0.85rem;
}
.passport-card { background:#F8FAFC; border:1px solid #E2E8F0; border-left:5px solid #6A9A7B; border-radius:14px; padding:1rem 1.1rem; min-height:150px; margin-bottom:0.85rem; }
.card-title { color:#121826; font-weight:820; margin-bottom:0.32rem; font-size:1rem; }
.card-text { color:#52606D; font-size:0.91rem; line-height:1.55; }
.passport-label { color:#64748B; font-size:0.74rem; text-transform:uppercase; letter-spacing:0.08em; font-weight:800; margin-bottom:0.34rem; }
.passport-main { color:#121826; font-size:1.05rem; font-weight:820; line-height:1.35; margin-bottom:0.35rem; }
.task-num { color:#6A9A7B; font-weight:850; font-size:0.86rem; margin-bottom:0.2rem; }
.pill { display:inline-block; border:1px solid #E2E8F0; background:#F8FAFC; color:#475569; border-radius:999px; padding:0.17rem 0.52rem; font-size:0.74rem; font-weight:740; margin:0.1rem 0.16rem 0.1rem 0; }
.note-box { background:#F8FAFC; border:1px solid #E2E8F0; border-radius:14px; padding:1rem 1.1rem; color:#52606D; line-height:1.58; margin-bottom:0.9rem; }
.small-muted { color:#7B8794; font-size:0.82rem; line-height:1.48; }
.table-wrap { background:#FFFFFF; border:1px solid #E5EAF0; border-radius:14px; overflow:hidden; margin-bottom:0.9rem; }
.table-row { display:grid; grid-template-columns:220px 1fr; border-bottom:1px solid #EEF2F6; }
.table-row:last-child { border-bottom:none; }
.table-left { background:#F8FAFC; padding:0.78rem 0.95rem; color:#121826; font-weight:780; }
.table-right { padding:0.78rem 0.95rem; color:#52606D; line-height:1.5; }
@media (max-width: 900px) { .hero-title { font-size:1.85rem; } .table-row { grid-template-columns:1fr; } .table-left { border-bottom:1px solid #EEF2F6; } }
</style>
""", unsafe_allow_html=True)

lang_col1, lang_col2 = st.columns([6, 1])
with lang_col2:
    if render_lang_switcher:
        render_lang_switcher()

st.markdown("""
<div class="hero">
  <div class="kicker">Электронное приложение к выпускной квалификационной работе</div>
  <h1 class="hero-title">Статистический анализ и прогнозирование внешней торговли России с Китаем и Индией</h1>
  <div class="hero-subtitle">
    Данная страница содержит общую характеристику исследования: объект, предмет, цель, задачи,
    информационную базу и применяемые методы. Электронное приложение используется для представления
    расчетной и визуальной части выпускной квалификационной работы.
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-head">
  <h2>Паспорт исследования</h2>
  <p>Вводная часть фиксирует основные элементы исследовательской рамки, на которой построены последующие расчетные разделы.</p>
</div>
""", unsafe_allow_html=True)

p1, p2, p3 = st.columns(3)
with p1:
    st.markdown("""
    <div class="passport-card">
      <div class="passport-label">Объект исследования</div>
      <div class="passport-main">Внешняя торговля Российской Федерации</div>
      <div class="card-text">В работе рассматриваются торговые связи России с Китаем и Индией как ключевыми направлениями внешнеэкономического взаимодействия.</div>
    </div>
    """, unsafe_allow_html=True)
with p2:
    st.markdown("""
    <div class="passport-card">
      <div class="passport-label">Предмет исследования</div>
      <div class="passport-main">Показатели и факторы развития внешней торговли</div>
      <div class="card-text">Анализируются объемы экспорта и импорта, оборот, сальдо, коэффициент покрытия, товарная структура и факторы прогнозной динамики.</div>
    </div>
    """, unsafe_allow_html=True)
with p3:
    st.markdown("""
    <div class="passport-card">
      <div class="passport-label">Период исследования</div>
      <div class="passport-main">2000–2023 годы; прогноз до 2030 года</div>
      <div class="card-text">Ретроспективный анализ строится на доступных сопоставимых статистических рядах, прогнозная часть продолжает расчет до 2030 года.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="section-head">
  <h2>Цель и задачи исследования</h2>
</div>
<div class="note-box">
  <b>Цель исследования</b> — провести комплексный статистический анализ внешней торговли Российской Федерации
  с Китаем и Индией, оценить структурные и динамические изменения торговых потоков и построить прогноз
  внешнеторгового оборота до 2030 года.
</div>
""", unsafe_allow_html=True)

task_cols = st.columns(3)
tasks = [
    ("01", "Раскрыть теоретические основы внешней торговли и особенности ее статистического учета."),
    ("02", "Сформировать информационную базу исследования по России, Китаю и Индии."),
    ("03", "Оценить информационный фон внешнеэкономических отношений с использованием семантического анализа."),
    ("04", "Проанализировать динамику экспорта, импорта, внешнеторгового оборота и сальдо."),
    ("05", "Рассмотреть товарную и географическую структуру торговли, а также структурные сдвиги."),
    ("06", "Построить и сопоставить прогнозные модели внешнеторгового оборота до 2030 года."),
]
for i, (num, text) in enumerate(tasks):
    with task_cols[i % 3]:
        st.markdown(f"""
        <div class="task-card">
          <div class="task-num">{num}</div>
          <div class="card-text">{text}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div class="section-head">
  <h2>Методологическая основа</h2>
  <p>В приложении применяются статистические, структурные и прогнозные методы, соответствующие задачам исследования.</p>
</div>
""", unsafe_allow_html=True)

m1, m2, m3 = st.columns(3)
with m1:
    st.markdown("""
    <div class="card">
      <div class="card-title">Статистический анализ динамики</div>
      <div class="card-text">Используются показатели внешнеторгового оборота, экспорта, импорта, сальдо торгового баланса, коэффициента покрытия и темпов изменения.</div>
      <span class="pill">динамика</span><span class="pill">сальдо</span><span class="pill">коэффициент покрытия</span>
    </div>
    """, unsafe_allow_html=True)
with m2:
    st.markdown("""
    <div class="card">
      <div class="card-title">Структурный анализ</div>
      <div class="card-text">Рассматриваются изменения товарной и географической структуры торговли, а также индексы структурных сдвигов Гатева и Салаи.</div>
      <span class="pill">товарная структура</span><span class="pill">индекс Гатева</span><span class="pill">индекс Салаи</span>
    </div>
    """, unsafe_allow_html=True)
with m3:
    st.markdown("""
    <div class="card">
      <div class="card-title">Прогнозирование и NLP-анализ</div>
      <div class="card-text">В прогнозной части сопоставляются регрессионные и временные модели, а семантический анализ используется для оценки новостного фона.</div>
      <span class="pill">регрессия</span><span class="pill">ARIMA</span><span class="pill">NLP</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="section-head">
  <h2>Состав электронного приложения</h2>
  <p>Разделы приложения соответствуют основным этапам исследования и предназначены для демонстрации расчетных материалов.</p>
</div>
<div class="table-wrap">
  <div class="table-row"><div class="table-left">Теоретический раздел</div><div class="table-right">Понятия внешней торговли, методология статистического учета, правила Incoterms 2020 и особенности информационной базы России, Китая и Индии.</div></div>
  <div class="table-row"><div class="table-left">Семантический анализ</div><div class="table-right">Оценка новостного фона внешнеэкономических связей с применением RSS-источников и NLP-подхода.</div></div>
  <div class="table-row"><div class="table-left">Статистический анализ</div><div class="table-right">Динамика, товарная структура, география торговли, торговое сальдо, коэффициенты покрытия и структурные сдвиги.</div></div>
  <div class="table-row"><div class="table-left">Итоговый и прогнозный раздел</div><div class="table-right">Сводная оценка торговых связей за 2023 год и прогноз внешнеторгового оборота России с Китаем и Индией до 2030 года.</div></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-head">
  <h2>Информационная база</h2>
  <p>Для расчетов используются открытые статистические и информационные источники, позволяющие сопоставлять торговые потоки в динамике и структуре.</p>
</div>
""", unsafe_allow_html=True)

source_cols = st.columns(4)
sources = [
    ("WITS World Bank", "Временные ряды внешней торговли за 2000–2023 годы."),
    ("Trade Map / ITC", "Товарная структура экспорта и импорта по основным группам."),
    ("Atlas of Economic Complexity", "Данные о географической структуре торговли и долях стран-партнеров."),
    ("GDELT и RSS", "Материалы для оценки информационного фона и семантического анализа."),
    ("Росстат", "Российская государственная статистика и макроэкономические показатели."),
    ("ФТС России", "Таможенная статистика и сведения о внешнеторговых потоках."),
    ("Банк России", "Платежный баланс, внешнеэкономические и валютные показатели."),
    ("Официальные ведомства Китая и Индии", "Национальные статистические и торговые источники стран-партнеров."),
]
for i, (title, text) in enumerate(sources):
    with source_cols[i % 4]:
        st.markdown(f"""
        <div class="source-card">
          <div class="card-title">{title}</div>
          <div class="card-text">{text}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"<div class='small-muted'>&copy; 2026 {L('footer_copyright')}</div>", unsafe_allow_html=True)
