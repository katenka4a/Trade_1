"""
Локализация: RU / EN словари для всего интерфейса.
Использование: from data.locales import L
L["key"]["ru"] или L.get_text("key", lang)
"""
from typing import Dict

# ── Единый словарь ──
LOCALES: Dict[str, Dict[str, str]] = {
    # === Главная (app.py) ===
    "project_subtitle": {"ru": "Дипломный проект · 2026", "en": "Graduation project · 2026"},
    "title_main": {"ru": "Внешняя торговля России с Китаем и Индией", "en": "Russia's Foreign Trade with China and India"},
    "subtitle_main": {"ru": "Анализ, визуализация и NLP-прогнозирование торговых потоков", "en": "Analysis, Visualization & NLP-based Trade Flow Forecasting"},
    "project_desc": {"ru": "Проект посвящён анализу внешней торговли России с Китаем и Индией после кардинальной переориентации торговых потоков в 2022 году. Содержит теоретический обзор, интерактивные визуализации статистики, географию торговли, NLP-анализ тональности новостей и прогностические метрики.", "en": "This project analyzes Russia's foreign trade with China and India after the radical reorientation of trade flows in 2022. It includes a theoretical overview, interactive data visualizations, trade geography, NLP sentiment analysis, and forecast metrics."},
    "forecast_status_title": {"ru": "Состояние прогноза", "en": "Forecast Status"},
    "forecast_not_loaded": {"ru": "Прогноз не загружен. Откройте страницу <strong>Live Прогноз</strong> и нажмите кнопку обновления.", "en": "Forecast not loaded. Open the <strong>Live Forecast</strong> page and click the update button."},
    "last_update": {"ru": "Последнее обновление", "en": "Last update"},
    "nav_teoriya": {"ru": "Теория и методология", "en": "Theory & Methodology"},
    "nav_nlp": {"ru": "Анализ тональности", "en": "Sentiment Analysis"},
    "nav_data": {"ru": "Статистика", "en": "Statistics"},
    "nav_forecast": {"ru": "Live Прогноз", "en": "Live Forecast"},
    "nav_forecast_ru_cn": {"ru": "Прогноз РФ-Китай", "en": "Forecast RU-China"},
    "nav_forecast_ru_in": {"ru": "Прогноз РФ-Индия", "en": "Forecast RU-India"},
    "nav_geo": {"ru": "География торговли", "en": "Trade Geography"},
    "nav_overview": {"ru": "Обзор исследования", "en": "Research Overview"},
    "nav_about": {"ru": "О проекте", "en": "About"},
    "nav_teoriya_desc": {"ru": "Определения, законы, Инкотермс, формулы", "en": "Definitions, laws, Incoterms, formulas"},
    "nav_nlp_desc": {"ru": "RSS-агрегатор, TextBlob, DeepSeek, текущая тональность", "en": "RSS aggregator, TextBlob, DeepSeek, current sentiment"},
    "nav_data_desc": {"ru": "Динамика, структура, индексы сдвигов", "en": "Dynamics, structure, shift indices"},
    "nav_forecast_desc": {"ru": "RSS + DeepSeek + TextBlob, обновления", "en": "RSS + DeepSeek + TextBlob updates"},
    "nav_geo_desc": {"ru": "Карта потоков, маршруты, доли", "en": "Flow map, routes, shares"},
    "nav_overview_desc": {"ru": "Резюме, выводы и рекомендации", "en": "Summary, findings, recommendations"},
    "nav_about_desc": {"ru": "Стек, структура, источники, запуск", "en": "Stack, structure, sources, launch"},

    # === 01_Теория.py ===
    "theory_title": {"ru": "Теория и методология", "en": "Theory & Methodology"},
    "theory_subtitle": {"ru": "Основы ВЭД, законы, Инкотермс, показатели, методология учёта", "en": "Fundamentals of foreign trade, laws, Incoterms, indicators, accounting methodology"},
    "theory_tab1": {"ru": "Основы и законы", "en": "Fundamentals & Laws"},
    "theory_tab2": {"ru": "Показатели", "en": "Indicators"},
    "theory_tab3": {"ru": "Методология учёта", "en": "Accounting Methodology"},
    "theory_tab4": {"ru": "Источники", "en": "Sources"},
    "theory_def_foreign_trade": {"ru": "<b>Внешняя торговля</b> — обмен товарами, услугами или правами интеллектуальной собственности между хозяйствующими субъектами различных стран.", "en": "<b>Foreign trade</b> is the exchange of goods, services, or intellectual property rights between economic entities of different countries."},
    "theory_def_fed": {"ru": "<b>Внешнеэкономическая деятельность (ВЭД)</b> — предпринимательская деятельность, связанная с перемещением товаров и капитала через таможенную границу.", "en": "<b>Foreign Economic Activity (FEA)</b> — entrepreneurial activity related to the movement of goods and capital across the customs border."},
    "theory_laws_title": {"ru": "Ключевые законы РФ", "en": "Key Russian Laws"},
    "theory_incoterms_title": {"ru": "Инкотермс 2020", "en": "Incoterms 2020"},
    "theory_incoterms_desc": {"ru": "Свод правил Международной торговой палаты, определяющий распределение расходов и рисков. <b>Не регулирует</b> переход права собственности.", "en": "A set of ICC rules defining the distribution of costs and risks. <b>Does not regulate</b> transfer of ownership."},
    "theory_turnover_def": {"ru": "<b>Внешнеторговый оборот (ВТО)</b>: ВТО = Э + И", "en": "<b>Foreign trade turnover (FTO)</b>: FTO = E + I"},
    "theory_balance_def": {"ru": "<b>Сальдо торгового баланса</b>: С = Э − И", "en": "<b>Trade balance</b>: B = E − I"},
    "theory_structural_indices": {"ru": "Индексы структурных сдвигов (Гатева и Салаи)", "en": "Structural Shift Indices (Gatev & Salai)"},
    "theory_gatev_formula": {"ru": "<b>Индекс Гатева</b>: Kг = √[∑(d²-d¹)²] / √[∑(d²)² + ∑(d¹)²]", "en": "<b>Gatev Index</b>: Kг = √[∑(d²-d¹)²] / √[∑(d²)² + ∑(d¹)²]"},
    "theory_salai_formula": {"ru": "<b>Индекс Салаи</b>: Ks = √[∑((d²-d¹)/(d²+d¹))²] / √n", "en": "<b>Salai Index</b>: Ks = √[∑((d²-d¹)/(d²+d¹))²] / √n"},
    "theory_shift_note": {"ru": "Значения > 0,3 — значительные структурные сдвиги.", "en": "Values > 0.3 indicate significant structural shifts."},
    "theory_method_diff": {"ru": "Различия в методологии учёта приводят к <b>несопоставимости статистики</b> между странами.", "en": "Differences in accounting methodology lead to <b>incomparable statistics</b> between countries."},
    "theory_export_fob": {"ru": "Оценка экспорта на FOB, импорта на CIF", "en": "Export valued at FOB, import at CIF"},
    "theory_timing_diff": {"ru": "Разный момент учёта (отгрузка vs граница)", "en": "Different recording time (shipment vs border)"},
    "theory_classifier_diff": {"ru": "Разные классификаторы и пороги учёта", "en": "Different classifiers and thresholds"},

    # === 02_NLP_подход.py ===
    "nlp_title": {"ru": "Анализ тональности", "en": "Sentiment Analysis"},
    "nlp_subtitle": {"ru": "Текущая тональность новостей по торговым парам на основе RSS", "en": "Current news sentiment for trade pairs based on RSS"},
    "nlp_tab_method": {"ru": "Методология", "en": "Methodology"},
    "nlp_tab_rss": {"ru": "Динамический RSS", "en": "Dynamic RSS"},
    "nlp_tab_results": {"ru": "Результаты диплома", "en": "Thesis Results"},
    "nlp_sentiment_desc": {"ru": "<b>Sentiment Analysis</b> — метод NLP для определения эмоциональной окраски текста.", "en": "<b>Sentiment Analysis</b> is an NLP method for detecting the emotional tone of text."},
    "nlp_textblob": {"ru": "<b>TextBlob</b>: полярность от −1 до +1", "en": "<b>TextBlob</b>: polarity from −1 to +1"},
    "nlp_deepseek": {"ru": "<b>DeepSeek API</b>: экспертная LLM-оценка заголовков", "en": "<b>DeepSeek API</b>: expert LLM assessment of headlines"},
    "nlp_rss_agg": {"ru": "<b>RSS-агрегатор</b>: сбор заголовков Google News", "en": "<b>RSS aggregator</b>: collecting Google News headlines"},
    "nlp_adjustment": {"ru": "<b>Поправка к прогнозу</b> = Полярность × 20%", "en": "<b>Forecast adjustment</b> = Polarity × 20%"},
    "nlp_load_btn": {"ru": "Загрузить свежие новости", "en": "Load fresh news"},
    "nlp_no_data": {"ru": "Нажмите кнопку для загрузки свежих новостей.", "en": "Click the button to load fresh news."},
    "nlp_articles": {"ru": "Заголовков", "en": "Articles"},
    "nlp_avg_polarity": {"ru": "Средняя полярность", "en": "Avg Polarity"},
    "nlp_adjust": {"ru": "Поправка", "en": "Adjustment"},
    "nlp_distribution_title": {"ru": "Распределение тональности (январь 2026)", "en": "Sentiment Distribution (Jan 2026)"},
    "nlp_gdelt_title": {"ru": "Индексы тональности GDELT (12 мес.)", "en": "GDELT Sentiment Indices (12 months)"},
    "nlp_ru_cn_comment": {"ru": "<b>Россия-Китай</b> (−0,009): стабильно нейтральный фон. Большинство публикаций фактологические.", "en": "<b>Russia-China</b> (−0.009): stable neutral tone. Most publications are factual."},
    "nlp_ru_in_comment": {"ru": "<b>Россия-Индия</b> (+0,011): едва положительный. Доминируют сообщения о нефтяных поставках.", "en": "<b>Russia-India</b> (+0.011): slightly positive. Dominated by oil supply reports."},
    "nlp_cn_in_comment": {"ru": "<b>Китай-Индия</b> (−0,046): устойчивое напряжение с негативным уклоном.", "en": "<b>China-India</b> (−0.046): persistent tension with negative bias."},

    # === 03_Данные.py ===
    "data_title": {"ru": "Статистика и визуализация", "en": "Statistics & Visualization"},
    "data_subtitle": {"ru": "Динамика, структура, индексы — на основе WITS, Trade Map, ФТС", "en": "Dynamics, structure, indices — based on WITS, Trade Map, FCS"},
    "data_tab_dynamics": {"ru": "Динамика", "en": "Dynamics"},
    "data_tab_structure": {"ru": "Структура", "en": "Structure"},
    "data_tab_indices": {"ru": "Индексы", "en": "Indices"},
    "data_tab_raw": {"ru": "Сырые данные", "en": "Raw Data"},
    "data_subtab_turnover": {"ru": "Оборот", "en": "Turnover"},
    "data_subtab_expimp": {"ru": "Экспорт/Импорт", "en": "Exports/Imports"},
    "data_subtab_balance": {"ru": "Сальдо", "en": "Balance"},
    "data_subtab_export_rf": {"ru": "Экспорт РФ (2023)", "en": "Russia's Exports (2023)"},
    "data_subtab_import_rf": {"ru": "Импорт РФ (2023)", "en": "Russia's Imports (2023)"},
    "data_subtab_partners": {"ru": "Доли партнёров", "en": "Partner Shares"},
    "data_subtab_shifts": {"ru": "Структурные сдвиги", "en": "Structural Shifts"},
    "data_subtab_coverage": {"ru": "Коэффициент покрытия", "en": "Coverage Ratio"},
    "data_to_china": {"ru": "В Китай", "en": "To China"},
    "data_to_india": {"ru": "В Индию", "en": "To India"},
    "data_from_china": {"ru": "Из Китая", "en": "From China"},
    "data_from_india": {"ru": "Из Индии", "en": "From India"},
    "data_export_ru": {"ru": "Экспорт", "en": "Export"},
    "data_import_ru": {"ru": "Импорт", "en": "Import"},
    "data_year": {"ru": "Год", "en": "Year"},

    # === 04_Прогноз.py (Live) ===
    "forecast_title": {"ru": "Live Прогноз", "en": "Live Forecast"},
    "forecast_subtitle": {"ru": "NLP-скорректированный прогноз внешней торговли с Китаем и Индией", "en": "NLP-adjusted forecast of foreign trade with China and India"},
    "forecast_update_btn": {"ru": "Обновить прогноз", "en": "Update Forecast"},
    "forecast_pair": {"ru": "Пара", "en": "Pair"},
    "forecast_base": {"ru": "Базовый темп роста", "en": "Base Growth Rate"},
    "forecast_nlp_adjust": {"ru": "NLP-поправка", "en": "NLP Adjustment"},
    "forecast_adjusted": {"ru": "Скорректированный прогноз", "en": "Adjusted Forecast"},
    "forecast_mid": {"ru": "Прогноз на середину", "en": "Mid-Year Forecast"},
    "forecast_high": {"ru": "Прогноз на конец", "en": "Year-End Forecast"},

    # === 06_О_проекте.py ===
    "about_title": {"ru": "О проекте", "en": "About"},
    "about_stack_title": {"ru": "Стек технологий", "en": "Tech Stack"},
    "about_structure_title": {"ru": "Структура проекта", "en": "Project Structure"},
    "about_sources_title": {"ru": "Источники данных", "en": "Data Sources"},
    "about_launch_title": {"ru": "Локальный запуск", "en": "Local Launch"},

    # === 07_География_торговли.py ===
    "geo_title": {"ru": "География торговли", "en": "Trade Geography"},
    "geo_subtitle": {"ru": "Переориентация экспортных потоков России на Восток", "en": "Reorientation of Russia's export flows to the East"},
    "geo_export_cn": {"ru": "Экспорт РФ→Китай (2023)", "en": "Russia's Exports→China (2023)"},
    "geo_export_in": {"ru": "Экспорт РФ→Индия (2023)", "en": "Russia's Exports→India (2023)"},
    "geo_import_cn": {"ru": "Импорт РФ←Китай (2023)", "en": "Russia's Imports←China (2023)"},
    "geo_import_in": {"ru": "Импорт РФ←Индия (2023)", "en": "Russia's Imports←India (2023)"},
    "geo_map_title": {"ru": "Карта торговых потоков", "en": "Trade Flow Map"},
    "geo_dynamics_title": {"ru": "Динамика долей в экспорте РФ", "en": "Share Dynamics in Russia's Exports"},
    "geo_routes_title": {"ru": "Логистические маршруты", "en": "Logistics Routes"},
    "geo_yearly_title": {"ru": "Объёмы по годам", "en": "Yearly Volumes"},
    # Гео — ключевые логистические точки
    "geo_poi_khorgos": {"ru": "Хоргос", "en": "Khorgos"},
    "geo_poi_khorgos_desc": {"ru": "Крупнейший сухопутный погранпереход Китай-Казахстан. Через него идёт до 30% ж/д грузов РФ→Китай по Транссибу.", "en": "Largest land border crossing China-Kazakhstan. Up to 30% of RU→CN rail freight passes here via Trans-Siberian."},
    "geo_poi_zabaikalsk": {"ru": "Забайкальск", "en": "Zabaikalsk"},
    "geo_poi_zabaikalsk_desc": {"ru": "Главный ж/д погранпереход РФ-Китай (83% грузов по Ж/Д). Через него проходит почти вся нефть, лес и руда в Китай.", "en": "Main railway border crossing Russia-China (83% of rail freight). Almost all oil, timber and ore to China passes through."},
    "geo_poi_vostochny": {"ru": "Порт Восточный", "en": "Port Vostochny"},
    "geo_poi_vostochny_desc": {"ru": "Крупнейший порт Дальнего Востока. Глубоководный, принимает контейнеровозы, уголь, зерно. 90% контейнерного экспорта РФ в Азию.", "en": "Largest Far East port. Deep-water, handles container ships, coal, grain. 90% of RU container exports to Asia."},
    "geo_poi_chennai": {"ru": "Ченнаи", "en": "Chennai"},
    "geo_poi_chennai_desc": {"ru": "Порт на восточном побережье Индии. Ключевой для поставок российских удобрений и нефти в южную Индию.", "en": "Port on India's east coast. Key for Russian fertilizer and oil supplies to southern India."},
    "geo_poi_bandar_abbas": {"ru": "Бендер-Аббас", "en": "Bandar Abbas"},
    "geo_poi_bandar_abbas_desc": {"ru": "Иранский порт на МТК Север-Юг. Товары из РФ ж/д через Каспий→Бендер-Аббас→Индия.", "en": "Iranian port on North-South ITC. Goods from RU by rail via Caspian→Bandar Abbas→India."},
    "geo_poi_novorossiysk": {"ru": "Новороссийск", "en": "Novorossiysk"},
    "geo_poi_novorossiysk_desc": {"ru": "Крупнейший порт Чёрного моря. Основные грузы: зерно, удобрения, нефтепродукты в Индию и Китай.", "en": "Largest Black Sea port. Main cargo: grain, fertilizers, oil products to India and China."},
    "geo_poi_alashankou": {"ru": "Алашанькоу", "en": "Alashankou"},
    "geo_poi_alashankou_desc": {"ru": "Китайский ж/д КПП на границе с Казахстаном. Часть Транссиба. Объём: 14 млн тонн/год.", "en": "Chinese railway checkpoint at Kazakhstan border. Part of Trans-Siberian route. Volume: 14M tons/year."},

    # === 08_Обзор_исследования.py ===
    "overview_title": {"ru": "Обзор исследования", "en": "Research Overview"},
    "overview_subtitle": {"ru": "Краткое резюме для защиты дипломного проекта", "en": "Brief summary for the thesis defense"},
    "overview_goal": {"ru": "После 2022 года произошла радикальная переориентация торговых потоков России с Запада на Восток. Цель исследования — проанализировать структуру и динамику внешней торговли России с Китаем и Индией, а также разработать NLP-инструмент для мониторинга тональности новостей как предиктора торговых трендов.", "en": "After 2022, Russia's trade flows radically reoriented from West to East. The goal is to analyze the structure and dynamics of Russia's foreign trade with China and India, and to develop an NLP tool for monitoring news sentiment as a predictor of trade trends."},
    "overview_key_numbers": {"ru": "Ключевые цифры", "en": "Key Numbers"},
    "overview_growth_cn": {"ru": "Рост экспорта РФ→Китай", "en": "Export growth Russia→China"},
    "overview_growth_in": {"ru": "Рост экспорта РФ→Индия", "en": "Export growth Russia→India"},
    "overview_share_cn": {"ru": "Доля Китая в экспорте РФ", "en": "China's share in Russia's exports"},
    "overview_share_in": {"ru": "Доля Индии в экспорте РФ", "en": "India's share in Russia's exports"},
    "overview_sentiment_ru_cn": {"ru": "Тональность РФ–Китай", "en": "Sentiment Russia–China"},
    "overview_sentiment_ru_in": {"ru": "Тональность РФ–Индия", "en": "Sentiment Russia–India"},
    "overview_fuel_cn": {"ru": "Топливо в экспорт в Китай", "en": "Fuel in exports to China"},
    "overview_fuel_in": {"ru": "Топливо в экспорт в Индию", "en": "Fuel in exports to India"},
    "overview_structural": {"ru": "Структурные выводы", "en": "Structural Findings"},
    "overview_method": {"ru": "Методологические достижения", "en": "Methodological Achievements"},
    "overview_recommendations": {"ru": "Рекомендации", "en": "Recommendations"},
    "overview_limits": {"ru": "Ограничения и перспективы", "en": "Limitations & Prospects"},
    "overview_limits_content": {"ru": "Нет свежих таможенных данных после 2023 года; не реализована эконометрическая модель; RSS использует только заголовки.", "en": "No fresh customs data after 2023; no econometric model implemented; RSS only uses headlines."},
    "overview_future": {"ru": "Подключение GDELT API; VAR/ARIMA-модели; карты логистики; автообновление.", "en": "GDELT API integration; VAR/ARIMA models; logistics maps; auto-update."},

    # === Footer ===
    "footer_copyright": {"ru": "Дипломный проект", "en": "Graduation Project"},
    "footer_data": {"ru": "Данные: WITS, Trade Map, ФТС, GDELT", "en": "Data: WITS, Trade Map, FCS, GDELT"},

    # === Общие ===
    "open_btn": {"ru": "Открыть", "en": "Open"},
    "loading_spinner": {"ru": "Загрузка...", "en": "Loading..."},
    "error_occurred": {"ru": "Ошибка", "en": "Error"},
    "neutral": {"ru": "Нейтральные", "en": "Neutral"},
    "positive": {"ru": "Позитивные", "en": "Positive"},
    "negative": {"ru": "Негативные", "en": "Negative"},
    "china": {"ru": "Китай", "en": "China"},
    "india": {"ru": "Индия", "en": "India"},
    "russia": {"ru": "Россия", "en": "Russia"},
    "ru_cn": {"ru": "Россия-Китай", "en": "Russia-China"},
    "ru_in": {"ru": "Россия-Индия", "en": "Russia-India"},
    "cn_in": {"ru": "Китай-Индия", "en": "China-India"},

    # === Эконометрическая модель (04_Прогноз.py) ===
    "econometrics_rmse": {"ru": "RMSE (млрд $)", "en": "RMSE (bn $)"},
    "econometrics_mae": {"ru": "MAE (млрд $)", "en": "MAE (bn $)"},
    "econometrics_mape": {"ru": "MAPE (%)", "en": "MAPE (%)"},
    "econometrics_hybrid": {"ru": "Гибрид (LR + MLP + NLP)", "en": "Hybrid (LR + MLP + NLP)"},
    "econometrics_lr": {"ru": "Линейная регрессия", "en": "Linear Regression"},
    "econometrics_forecast_year": {"ru": "Прогноз на {year}", "en": "{year} Forecast"},
    "econometrics_test_mape": {"ru": "MAPE на тесте", "en": "Test MAPE"},
    "econometrics_metrics_diff": {"ru": "Различие метрик", "en": "Metrics Difference"},
    "econometrics_delta_pct": {"ru": "Δ = {delta:+.2f}%", "en": "Δ = {delta:+.2f}%"},
    "econometrics_table_title": {"ru": "Прогноз торгового оборота до 2030 года", "en": "Trade Turnover Forecast Until 2030"},
    "econometrics_year": {"ru": "Год", "en": "Year"},
    "econometrics_forecast": {"ru": "Прогноз", "en": "Forecast"},
    "econometrics_plot_title": {"ru": "Динамика оборота: факт, LR, гибрид", "en": "Turnover: Actual, LR, Hybrid"},
    "econometrics_billions": {"ru": "млрд $", "en": "bn $"},
    "econometrics_actual": {"ru": "Факт", "en": "Actual"},
    "econometrics_train_test_split": {"ru": "Обучение | Тест", "en": "Train | Test"},
    "econometrics_hybrid_forecast": {"ru": "Гибридный (лаговая матрица + NLP)", "en": "Hybrid (lag matrix + NLP)"},
    "econometrics_forecast_to": {"ru": "Прогноз до {year} года", "en": "Forecast until {year}"},
    "econometrics_billions_format": {"ru": "{val:.2f} млрд $", "en": "{val:.2f} bn $"},
}

def t(key: str, lang: str = "ru") -> str:
    """Получить перевод по ключу и языку."""
    entry = LOCALES.get(key)
    if entry is None:
        return f"[{key}]"
    return entry.get(lang, entry.get("ru", f"[{key}:{lang}]"))
# =============================================================================
# app.py — main Streamlit hub page localization additions
# Added without removing existing keys, so old imports remain compatible.
# =============================================================================
LOCALES.update({
    "app_hero_kicker": {
        "ru": "Электронное приложение к выпускной квалификационной работе",
        "en": "Electronic appendix to the graduation thesis",
    },
    "app_hero_title": {
        "ru": "Внешняя торговля РФ с Китаем и Индией",
        "en": "Russia's Foreign Trade with China and India",
    },
    "app_hero_subtitle": {
        "ru": "Статистический анализ, структура товарных потоков и прогноз развития внешнеторговых связей России с ключевыми азиатскими партнерами.",
        "en": "Statistical analysis, commodity flow structure and forecasting of Russia's foreign trade relations with key Asian partners.",
    },
    "app_hero_note": {
        "ru": "Иллюстрация используется как визуальная метафора торгового треугольника Россия—Китай—Индия; основная аналитическая часть проекта сохраняет академический характер.",
        "en": "The illustration is used as a visual metaphor for the Russia-China-India trade triangle; the main analytical part of the project retains an academic character.",
    },
    "app_image_missing": {
        "ru": "Иллюстрация не найдена. Проверьте путь к файлу в папке Иллюстрации.",
        "en": "The illustration was not found. Check the file path in the Illustrations folder.",
    },
    "app_page_missing_short": {
        "ru": "Файл не найден",
        "en": "File not found",
    },
    "app_footer": {
        "ru": "Дипломное исследование",
        "en": "Graduation thesis project",
    },
    "app_nav_about_title": {
        "ru": "О проекте",
        "en": "About the Project",
    },
    "app_nav_about_desc": {
        "ru": "Описание работы, цели, задачи, актуальность",
        "en": "Project description, goal, objectives and relevance",
    },
    "app_nav_theory_title": {
        "ru": "Теоретические основы внешней торговли",
        "en": "Theoretical Foundations of Foreign Trade",
    },
    "app_nav_theory_desc": {
        "ru": "Обзор теории, основные понятия и показатели",
        "en": "Theory overview, key concepts and indicators",
    },
    "app_nav_semantic_title": {
        "ru": "Семантический анализ",
        "en": "Semantic Analysis",
    },
    "app_nav_semantic_desc": {
        "ru": "NLP-анализ тональности медиа по торговой тематике",
        "en": "NLP-based media sentiment analysis on trade topics",
    },
    "app_nav_stats_title": {
        "ru": "Статистический анализ",
        "en": "Statistical Analysis",
    },
    "app_nav_stats_desc": {
        "ru": "Динамика и структура торговли РФ с Китаем и Индией",
        "en": "Dynamics and structure of Russia's trade with China and India",
    },
    "app_nav_results_title": {
        "ru": "Результаты внешней торговли",
        "en": "Foreign Trade Results",
    },
    "app_nav_results_desc": {
        "ru": "Итоги торговли за 2023 год с визуализацией на карте",
        "en": "2023 trade results with map visualization",
    },
    "app_nav_forecast_cn_title": {
        "ru": "Прогноз Россия — Китай",
        "en": "Russia-China Forecast",
    },
    "app_nav_forecast_cn_desc": {
        "ru": "Прогнозирование торговли с КНР до 2030 года",
        "en": "Forecasting trade with China up to 2030",
    },
    "app_nav_forecast_in_title": {
        "ru": "Прогноз Россия — Индия",
        "en": "Russia-India Forecast",
    },
    "app_nav_forecast_in_desc": {
        "ru": "Прогнозирование торговли с Индией до 2030 года",
        "en": "Forecasting trade with India up to 2030",
    },
})


def _normalize_lang(value: str | None) -> str:
    value = str(value or "").strip().lower()
    if value in {"en", "eng", "english", "английский"}:
        return "en"
    return "ru"


def get_current_lang(default: str = "ru") -> str:
    """Return the current UI language from Streamlit session state when available."""
    try:
        import streamlit as st
        for key in ("lang", "language", "selected_lang", "i18n_lang", "app_lang", "ui_lang", "locale"):
            if key in st.session_state:
                return _normalize_lang(st.session_state.get(key))
    except Exception:
        pass
    return _normalize_lang(default)


def get_text(key: str, lang: str | None = None) -> str:
    """Safe key-based translation helper used by app.py and compatible with utils.py wrappers."""
    target = _normalize_lang(lang or get_current_lang())
    entry = LOCALES.get(key)
    if entry is None:
        return str(key)
    return entry.get(target) or entry.get("ru") or str(key)


class _LocaleAccessor(dict):
    """Backward-compatible helper: L['key']['ru'], L.get_text(...), or L('key')."""
    def __call__(self, key: str, lang: str | None = None) -> str:
        return get_text(key, lang)

    def get_text(self, key: str, lang: str | None = None) -> str:
        return get_text(key, lang)


L = _LocaleAccessor(LOCALES)


def translate_text(value, lang: str | None = None):
    """Small text translator for pages that import translate_text from data.locales.

    It intentionally translates only exact UI strings from LOCALES, so dataframe cell
    values and statistical data are not modified.
    """
    if not isinstance(value, str):
        return value
    target = _normalize_lang(lang or get_current_lang())
    if target != "en" or not value:
        return value
    for entry in LOCALES.values():
        ru = entry.get("ru")
        en = entry.get("en")
        if value == ru and en:
            return en
    return value


def install_streamlit_i18n(st_module=None) -> None:
    """Compatibility hook for localized pages.

    The full project may use a broader runtime translation layer. For this patch we
    keep the hook lightweight and safe: it translates common Streamlit labels exactly
    when they match LOCALES and leaves dataframes/calculations untouched.
    """
    try:
        import streamlit as st
    except Exception:
        return
    st = st_module or st
    if getattr(st, "_diploma_i18n_app_patch_installed", False):
        return

    def _wrap_text_fn(name):
        original = getattr(st, name, None)
        if original is None:
            return
        setattr(st, f"_orig_{name}", original)
        def wrapped(body=None, *args, **kwargs):
            return original(translate_text(body), *args, **kwargs)
        setattr(st, name, wrapped)

    for fn in ("info", "warning", "error", "success", "caption", "title", "header", "subheader"):
        _wrap_text_fn(fn)

    if hasattr(st, "button"):
        original_button = st.button
        st._orig_button = original_button
        def button(label, *args, **kwargs):
            if "help" in kwargs:
                kwargs["help"] = translate_text(kwargs["help"])
            return original_button(translate_text(label), *args, **kwargs)
        st.button = button

    if hasattr(st, "tabs"):
        original_tabs = st.tabs
        st._orig_tabs = original_tabs
        def tabs(labels, *args, **kwargs):
            return original_tabs([translate_text(x) for x in labels], *args, **kwargs)
        st.tabs = tabs

    st._diploma_i18n_app_patch_installed = True

# =============================================================================
# 04_Статистический_анализ_внешней_торговли.py — completed RU/EN localization
# Added as an overlay: existing keys stay untouched, calculations/dataframes are not changed.
# =============================================================================
_STATS04_TEXT_TRANSLATIONS = {'Статистический анализ внешней торговли': 'Statistical Analysis of Foreign Trade',
 'Статистический анализ внешней торговли — пояснительная версия страницы.': 'Statistical analysis of foreign trade — '
                                                                            'explanatory page version.',
 'Глава 2 · статистическая база исследования': 'Chapter 2 · statistical base of the study',
 'В разделе представлены расчеты по динамике, структуре и сбалансированности торговли России с Китаем и Индией.': 'This '
                                                                                                                  'section '
                                                                                                                  'presents '
                                                                                                                  'calculations '
                                                                                                                  'on '
                                                                                                                  'the '
                                                                                                                  'dynamics, '
                                                                                                                  'structure '
                                                                                                                  'and '
                                                                                                                  'balance '
                                                                                                                  'of '
                                                                                                                  'Russia’s '
                                                                                                                  'trade '
                                                                                                                  'with '
                                                                                                                  'China '
                                                                                                                  'and '
                                                                                                                  'India.',
 'Особое внимание уделяется не только объему торговли, но и ее содержанию: какие товарные группы формируют экспорт и импорт,': 'Special '
                                                                                                                               'attention '
                                                                                                                               'is '
                                                                                                                               'paid '
                                                                                                                               'not '
                                                                                                                               'only '
                                                                                                                               'to '
                                                                                                                               'trade '
                                                                                                                               'volume, '
                                                                                                                               'but '
                                                                                                                               'also '
                                                                                                                               'to '
                                                                                                                               'its '
                                                                                                                               'composition: '
                                                                                                                               'which '
                                                                                                                               'commodity '
                                                                                                                               'groups '
                                                                                                                               'form '
                                                                                                                               'exports '
                                                                                                                               'and '
                                                                                                                               'imports,',
 'как изменилась география партнеров и насколько экспортная выручка покрывает импортные закупки.': 'how the geography '
                                                                                                   'of partners has '
                                                                                                   'changed and how '
                                                                                                   'far export '
                                                                                                   'revenues cover '
                                                                                                   'import purchases.',
 'Порядок чтения раздела': 'How to Read the Section',
 'Сначала рассматривается масштаб торговли во времени, затем — экспортно-импортная структура, далее формально оцениваются структурные сдвиги и коэффициент покрытия. Такой порядок позволяет связать графики с экономической интерпретацией: объем → состав → изменение структуры → устойчивость торгового баланса.': 'First, '
                                                                                                                                                                                                                                                                                                                      'the '
                                                                                                                                                                                                                                                                                                                      'scale '
                                                                                                                                                                                                                                                                                                                      'of '
                                                                                                                                                                                                                                                                                                                      'trade '
                                                                                                                                                                                                                                                                                                                      'over '
                                                                                                                                                                                                                                                                                                                      'time '
                                                                                                                                                                                                                                                                                                                      'is '
                                                                                                                                                                                                                                                                                                                      'considered; '
                                                                                                                                                                                                                                                                                                                      'then '
                                                                                                                                                                                                                                                                                                                      'the '
                                                                                                                                                                                                                                                                                                                      'export-import '
                                                                                                                                                                                                                                                                                                                      'structure '
                                                                                                                                                                                                                                                                                                                      'is '
                                                                                                                                                                                                                                                                                                                      'examined; '
                                                                                                                                                                                                                                                                                                                      'after '
                                                                                                                                                                                                                                                                                                                      'that, '
                                                                                                                                                                                                                                                                                                                      'structural '
                                                                                                                                                                                                                                                                                                                      'shifts '
                                                                                                                                                                                                                                                                                                                      'and '
                                                                                                                                                                                                                                                                                                                      'the '
                                                                                                                                                                                                                                                                                                                      'coverage '
                                                                                                                                                                                                                                                                                                                      'ratio '
                                                                                                                                                                                                                                                                                                                      'are '
                                                                                                                                                                                                                                                                                                                      'formally '
                                                                                                                                                                                                                                                                                                                      'assessed. '
                                                                                                                                                                                                                                                                                                                      'This '
                                                                                                                                                                                                                                                                                                                      'order '
                                                                                                                                                                                                                                                                                                                      'makes '
                                                                                                                                                                                                                                                                                                                      'it '
                                                                                                                                                                                                                                                                                                                      'possible '
                                                                                                                                                                                                                                                                                                                      'to '
                                                                                                                                                                                                                                                                                                                      'connect '
                                                                                                                                                                                                                                                                                                                      'the '
                                                                                                                                                                                                                                                                                                                      'charts '
                                                                                                                                                                                                                                                                                                                      'with '
                                                                                                                                                                                                                                                                                                                      'economic '
                                                                                                                                                                                                                                                                                                                      'interpretation: '
                                                                                                                                                                                                                                                                                                                      'volume '
                                                                                                                                                                                                                                                                                                                      '→ '
                                                                                                                                                                                                                                                                                                                      'composition '
                                                                                                                                                                                                                                                                                                                      '→ '
                                                                                                                                                                                                                                                                                                                      'structural '
                                                                                                                                                                                                                                                                                                                      'change '
                                                                                                                                                                                                                                                                                                                      '→ '
                                                                                                                                                                                                                                                                                                                      'stability '
                                                                                                                                                                                                                                                                                                                      'of '
                                                                                                                                                                                                                                                                                                                      'the '
                                                                                                                                                                                                                                                                                                                      'trade '
                                                                                                                                                                                                                                                                                                                      'balance.',
 'Динамический блок': 'Dynamics Block',
 'Динамика показывает, что российско-китайская торговля формировалась как долгосрочный крупный контур, тогда как российско-индийское направление резко усилилось в последние годы за счет экспортного потока.': 'The '
                                                                                                                                                                                                                'dynamics '
                                                                                                                                                                                                                'show '
                                                                                                                                                                                                                'that '
                                                                                                                                                                                                                'Russia-China '
                                                                                                                                                                                                                'trade '
                                                                                                                                                                                                                'formed '
                                                                                                                                                                                                                'as '
                                                                                                                                                                                                                'a '
                                                                                                                                                                                                                'long-term '
                                                                                                                                                                                                                'large-scale '
                                                                                                                                                                                                                'track, '
                                                                                                                                                                                                                'while '
                                                                                                                                                                                                                'the '
                                                                                                                                                                                                                'Russia-India '
                                                                                                                                                                                                                'direction '
                                                                                                                                                                                                                'strengthened '
                                                                                                                                                                                                                'sharply '
                                                                                                                                                                                                                'in '
                                                                                                                                                                                                                'recent '
                                                                                                                                                                                                                'years '
                                                                                                                                                                                                                'due '
                                                                                                                                                                                                                'to '
                                                                                                                                                                                                                'export '
                                                                                                                                                                                                                'flows.',
 'Внешнеторговый оборот': 'Foreign Trade Turnover',
 'Оборот равен сумме экспорта и импорта. Он показывает масштаб торгового взаимодействия, но сам по себе не отвечает на вопрос о выгоде или качестве структуры. Поэтому далее показатель сопоставляется с сальдо и составом товарных потоков.': 'Turnover '
                                                                                                                                                                                                                                               'equals '
                                                                                                                                                                                                                                               'the '
                                                                                                                                                                                                                                               'sum '
                                                                                                                                                                                                                                               'of '
                                                                                                                                                                                                                                               'exports '
                                                                                                                                                                                                                                               'and '
                                                                                                                                                                                                                                               'imports. '
                                                                                                                                                                                                                                               'It '
                                                                                                                                                                                                                                               'shows '
                                                                                                                                                                                                                                               'the '
                                                                                                                                                                                                                                               'scale '
                                                                                                                                                                                                                                               'of '
                                                                                                                                                                                                                                               'trade '
                                                                                                                                                                                                                                               'interaction, '
                                                                                                                                                                                                                                               'but '
                                                                                                                                                                                                                                               'by '
                                                                                                                                                                                                                                               'itself '
                                                                                                                                                                                                                                               'does '
                                                                                                                                                                                                                                               'not '
                                                                                                                                                                                                                                               'answer '
                                                                                                                                                                                                                                               'questions '
                                                                                                                                                                                                                                               'about '
                                                                                                                                                                                                                                               'benefit '
                                                                                                                                                                                                                                               'or '
                                                                                                                                                                                                                                               'structural '
                                                                                                                                                                                                                                               'quality. '
                                                                                                                                                                                                                                               'Therefore, '
                                                                                                                                                                                                                                               'the '
                                                                                                                                                                                                                                               'indicator '
                                                                                                                                                                                                                                               'is '
                                                                                                                                                                                                                                               'further '
                                                                                                                                                                                                                                               'compared '
                                                                                                                                                                                                                                               'with '
                                                                                                                                                                                                                                               'the '
                                                                                                                                                                                                                                               'trade '
                                                                                                                                                                                                                                               'balance '
                                                                                                                                                                                                                                               'and '
                                                                                                                                                                                                                                               'the '
                                                                                                                                                                                                                                               'composition '
                                                                                                                                                                                                                                               'of '
                                                                                                                                                                                                                                               'commodity '
                                                                                                                                                                                                                                               'flows.',
 'перестройка торговых потоков после 2022 года': 'restructuring of trade flows after 2022',
 'Китайское направление': 'China Direction',
 'Индийское направление': 'India Direction',
 'Экспорт и импорт': 'Exports and Imports',
 'Сопоставление экспорта и импорта показывает внутреннюю структуру оборота. Для Китая характерны крупные встречные потоки, а для Индии — резкое превышение российского экспорта над импортом.': 'Comparing '
                                                                                                                                                                                                'exports '
                                                                                                                                                                                                'and '
                                                                                                                                                                                                'imports '
                                                                                                                                                                                                'shows '
                                                                                                                                                                                                'the '
                                                                                                                                                                                                'internal '
                                                                                                                                                                                                'structure '
                                                                                                                                                                                                'of '
                                                                                                                                                                                                'turnover. '
                                                                                                                                                                                                'China '
                                                                                                                                                                                                'is '
                                                                                                                                                                                                'characterized '
                                                                                                                                                                                                'by '
                                                                                                                                                                                                'large '
                                                                                                                                                                                                'two-way '
                                                                                                                                                                                                'flows, '
                                                                                                                                                                                                'while '
                                                                                                                                                                                                'India '
                                                                                                                                                                                                'is '
                                                                                                                                                                                                'characterized '
                                                                                                                                                                                                'by '
                                                                                                                                                                                                'a '
                                                                                                                                                                                                'sharp '
                                                                                                                                                                                                'excess '
                                                                                                                                                                                                'of '
                                                                                                                                                                                                'Russian '
                                                                                                                                                                                                'exports '
                                                                                                                                                                                                'over '
                                                                                                                                                                                                'imports.',
 'Торговое сальдо': 'Trade Balance',
 'Сальдо рассчитывается как экспорт минус импорт. Положительное значение означает профицит торговли для России. Однако высокий профицит нужно сопоставлять со структурой: он может быть следствием сырьевой концентрации, а не широкой диверсификации.': 'The '
                                                                                                                                                                                                                                                         'balance '
                                                                                                                                                                                                                                                         'is '
                                                                                                                                                                                                                                                         'calculated '
                                                                                                                                                                                                                                                         'as '
                                                                                                                                                                                                                                                         'exports '
                                                                                                                                                                                                                                                         'minus '
                                                                                                                                                                                                                                                         'imports. '
                                                                                                                                                                                                                                                         'A '
                                                                                                                                                                                                                                                         'positive '
                                                                                                                                                                                                                                                         'value '
                                                                                                                                                                                                                                                         'means '
                                                                                                                                                                                                                                                         'a '
                                                                                                                                                                                                                                                         'trade '
                                                                                                                                                                                                                                                         'surplus '
                                                                                                                                                                                                                                                         'for '
                                                                                                                                                                                                                                                         'Russia. '
                                                                                                                                                                                                                                                         'However, '
                                                                                                                                                                                                                                                         'a '
                                                                                                                                                                                                                                                         'high '
                                                                                                                                                                                                                                                         'surplus '
                                                                                                                                                                                                                                                         'must '
                                                                                                                                                                                                                                                         'be '
                                                                                                                                                                                                                                                         'compared '
                                                                                                                                                                                                                                                         'with '
                                                                                                                                                                                                                                                         'the '
                                                                                                                                                                                                                                                         'structure: '
                                                                                                                                                                                                                                                         'it '
                                                                                                                                                                                                                                                         'may '
                                                                                                                                                                                                                                                         'result '
                                                                                                                                                                                                                                                         'from '
                                                                                                                                                                                                                                                         'raw-material '
                                                                                                                                                                                                                                                         'concentration '
                                                                                                                                                                                                                                                         'rather '
                                                                                                                                                                                                                                                         'than '
                                                                                                                                                                                                                                                         'broad '
                                                                                                                                                                                                                                                         'diversification.',
 'Баланс с Китаем': 'Balance with China',
 'В разные годы торговля с Китаем переходила от профицита к дефициту и обратно. Это связано с ростом импорта машин, оборудования и электроники, а затем с увеличением российского экспорта.': 'In '
                                                                                                                                                                                              'different '
                                                                                                                                                                                              'years, '
                                                                                                                                                                                              'trade '
                                                                                                                                                                                              'with '
                                                                                                                                                                                              'China '
                                                                                                                                                                                              'moved '
                                                                                                                                                                                              'from '
                                                                                                                                                                                              'surplus '
                                                                                                                                                                                              'to '
                                                                                                                                                                                              'deficit '
                                                                                                                                                                                              'and '
                                                                                                                                                                                              'back. '
                                                                                                                                                                                              'This '
                                                                                                                                                                                              'was '
                                                                                                                                                                                              'linked '
                                                                                                                                                                                              'to '
                                                                                                                                                                                              'the '
                                                                                                                                                                                              'growth '
                                                                                                                                                                                              'of '
                                                                                                                                                                                              'imports '
                                                                                                                                                                                              'of '
                                                                                                                                                                                              'machinery, '
                                                                                                                                                                                              'equipment '
                                                                                                                                                                                              'and '
                                                                                                                                                                                              'electronics, '
                                                                                                                                                                                              'and '
                                                                                                                                                                                              'later '
                                                                                                                                                                                              'to '
                                                                                                                                                                                              'an '
                                                                                                                                                                                              'increase '
                                                                                                                                                                                              'in '
                                                                                                                                                                                              'Russian '
                                                                                                                                                                                              'exports.',
 'Баланс с Индией': 'Balance with India',
 'Сальдо с Индией в последние годы резко выросло и стало одним из самых заметных результатов анализа. Его природа — экспортная асимметрия, прежде всего по энергетическому сырью.': 'The '
                                                                                                                                                                                    'balance '
                                                                                                                                                                                    'with '
                                                                                                                                                                                    'India '
                                                                                                                                                                                    'has '
                                                                                                                                                                                    'risen '
                                                                                                                                                                                    'sharply '
                                                                                                                                                                                    'in '
                                                                                                                                                                                    'recent '
                                                                                                                                                                                    'years '
                                                                                                                                                                                    'and '
                                                                                                                                                                                    'became '
                                                                                                                                                                                    'one '
                                                                                                                                                                                    'of '
                                                                                                                                                                                    'the '
                                                                                                                                                                                    'most '
                                                                                                                                                                                    'notable '
                                                                                                                                                                                    'findings '
                                                                                                                                                                                    'of '
                                                                                                                                                                                    'the '
                                                                                                                                                                                    'analysis. '
                                                                                                                                                                                    'Its '
                                                                                                                                                                                    'nature '
                                                                                                                                                                                    'is '
                                                                                                                                                                                    'export '
                                                                                                                                                                                    'asymmetry, '
                                                                                                                                                                                    'primarily '
                                                                                                                                                                                    'in '
                                                                                                                                                                                    'energy '
                                                                                                                                                                                    'commodities.',
 'Товарная структура': 'Commodity Structure',
 'Структурный анализ показывает, какие именно товары формируют торговые потоки. Важно различать сырьевые позиции, промышленный импорт, технологические компоненты и нишевые товары.': 'Structural '
                                                                                                                                                                                      'analysis '
                                                                                                                                                                                      'shows '
                                                                                                                                                                                      'which '
                                                                                                                                                                                      'goods '
                                                                                                                                                                                      'form '
                                                                                                                                                                                      'trade '
                                                                                                                                                                                      'flows. '
                                                                                                                                                                                      'It '
                                                                                                                                                                                      'is '
                                                                                                                                                                                      'important '
                                                                                                                                                                                      'to '
                                                                                                                                                                                      'distinguish '
                                                                                                                                                                                      'raw-material '
                                                                                                                                                                                      'items, '
                                                                                                                                                                                      'industrial '
                                                                                                                                                                                      'imports, '
                                                                                                                                                                                      'technological '
                                                                                                                                                                                      'components '
                                                                                                                                                                                      'and '
                                                                                                                                                                                      'niche '
                                                                                                                                                                                      'goods.',
 'Справка по компаниям': 'Company Reference',
 'Экспорт России': 'Russian Exports',
 'В экспорте оценивается, какая часть поставок приходится на сырьевые и полуфабрикатные группы. Чем выше доля минерального топлива, тем сильнее зависимость результата от энергетической конъюнктуры.': 'The '
                                                                                                                                                                                                        'export '
                                                                                                                                                                                                        'analysis '
                                                                                                                                                                                                        'assesses '
                                                                                                                                                                                                        'what '
                                                                                                                                                                                                        'share '
                                                                                                                                                                                                        'of '
                                                                                                                                                                                                        'supplies '
                                                                                                                                                                                                        'is '
                                                                                                                                                                                                        'accounted '
                                                                                                                                                                                                        'for '
                                                                                                                                                                                                        'by '
                                                                                                                                                                                                        'raw-material '
                                                                                                                                                                                                        'and '
                                                                                                                                                                                                        'semi-finished '
                                                                                                                                                                                                        'groups. '
                                                                                                                                                                                                        'The '
                                                                                                                                                                                                        'higher '
                                                                                                                                                                                                        'the '
                                                                                                                                                                                                        'share '
                                                                                                                                                                                                        'of '
                                                                                                                                                                                                        'mineral '
                                                                                                                                                                                                        'fuels, '
                                                                                                                                                                                                        'the '
                                                                                                                                                                                                        'stronger '
                                                                                                                                                                                                        'the '
                                                                                                                                                                                                        'dependence '
                                                                                                                                                                                                        'of '
                                                                                                                                                                                                        'the '
                                                                                                                                                                                                        'result '
                                                                                                                                                                                                        'on '
                                                                                                                                                                                                        'energy '
                                                                                                                                                                                                        'market '
                                                                                                                                                                                                        'conditions.',
 'Россия—Китай': 'Russia-China',
 'Россия—Индия': 'Russia-India',
 'Китай—Россия': 'China-Russia',
 'Индия—Россия': 'India-Russia',
 'Россия—Китай, оборот': 'Russia-China, turnover',
 'Россия—Индия, оборот': 'Russia-India, turnover',
 'РФ—Китай, оборот': 'Russia-China, turnover',
 'РФ—Индия, оборот': 'Russia-India, turnover',
 'Сальдо РФ—Китай': 'Russia-China balance',
 'Сальдо РФ—Индия': 'Russia-India balance',
 'Что именно экспортируется в Китай': 'What Is Exported to China',
 'Китай: состав экспорта': 'China: Export Composition',
 'Структура экспорта в Китай более диверсифицирована, чем в Индию: кроме топлива заметны руды, металлы, древесина, рыба, удобрения и другие сырьевые и полуфабрикатные позиции.': 'The '
                                                                                                                                                                                  'export '
                                                                                                                                                                                  'structure '
                                                                                                                                                                                  'to '
                                                                                                                                                                                  'China '
                                                                                                                                                                                  'is '
                                                                                                                                                                                  'more '
                                                                                                                                                                                  'diversified '
                                                                                                                                                                                  'than '
                                                                                                                                                                                  'to '
                                                                                                                                                                                  'India: '
                                                                                                                                                                                  'in '
                                                                                                                                                                                  'addition '
                                                                                                                                                                                  'to '
                                                                                                                                                                                  'fuel, '
                                                                                                                                                                                  'ores, '
                                                                                                                                                                                  'metals, '
                                                                                                                                                                                  'timber, '
                                                                                                                                                                                  'fish, '
                                                                                                                                                                                  'fertilizers '
                                                                                                                                                                                  'and '
                                                                                                                                                                                  'other '
                                                                                                                                                                                  'raw-material '
                                                                                                                                                                                  'and '
                                                                                                                                                                                  'semi-finished '
                                                                                                                                                                                  'positions '
                                                                                                                                                                                  'are '
                                                                                                                                                                                  'noticeable.',
 'Подробная таблица состава экспорта в Китай': 'Detailed Table of Export Composition to China',
 'Что именно экспортируется в Индию': 'What Is Exported to India',
 'Индия: состав экспорта': 'India: Export Composition',
 'Экспортное направление в Индию заметно более концентрировано: ключевой вклад в него вносят минеральное топливо, растительные масла и удобрения.': 'The '
                                                                                                                                                    'export '
                                                                                                                                                    'direction '
                                                                                                                                                    'to '
                                                                                                                                                    'India '
                                                                                                                                                    'is '
                                                                                                                                                    'noticeably '
                                                                                                                                                    'more '
                                                                                                                                                    'concentrated: '
                                                                                                                                                    'mineral '
                                                                                                                                                    'fuels, '
                                                                                                                                                    'vegetable '
                                                                                                                                                    'oils '
                                                                                                                                                    'and '
                                                                                                                                                    'fertilizers '
                                                                                                                                                    'make '
                                                                                                                                                    'the '
                                                                                                                                                    'key '
                                                                                                                                                    'contribution.',
 'Подробная таблица состава экспорта в Индию': 'Detailed Table of Export Composition to India',
 'Импорт России': 'Russian Imports',
 'В импорте важно отделить широкую промышленную зависимость от нишевых поставок. Китай поставляет большой набор машин, электроники и транспортных средств, а Индия заметна прежде всего по фармацевтике, химии и отдельным промышленным товарам.': 'In '
                                                                                                                                                                                                                                                   'imports, '
                                                                                                                                                                                                                                                   'it '
                                                                                                                                                                                                                                                   'is '
                                                                                                                                                                                                                                                   'important '
                                                                                                                                                                                                                                                   'to '
                                                                                                                                                                                                                                                   'separate '
                                                                                                                                                                                                                                                   'broad '
                                                                                                                                                                                                                                                   'industrial '
                                                                                                                                                                                                                                                   'dependence '
                                                                                                                                                                                                                                                   'from '
                                                                                                                                                                                                                                                   'niche '
                                                                                                                                                                                                                                                   'supplies. '
                                                                                                                                                                                                                                                   'China '
                                                                                                                                                                                                                                                   'supplies '
                                                                                                                                                                                                                                                   'a '
                                                                                                                                                                                                                                                   'wide '
                                                                                                                                                                                                                                                   'range '
                                                                                                                                                                                                                                                   'of '
                                                                                                                                                                                                                                                   'machinery, '
                                                                                                                                                                                                                                                   'electronics '
                                                                                                                                                                                                                                                   'and '
                                                                                                                                                                                                                                                   'vehicles, '
                                                                                                                                                                                                                                                   'while '
                                                                                                                                                                                                                                                   'India '
                                                                                                                                                                                                                                                   'is '
                                                                                                                                                                                                                                                   'noticeable '
                                                                                                                                                                                                                                                   'primarily '
                                                                                                                                                                                                                                                   'in '
                                                                                                                                                                                                                                                   'pharmaceuticals, '
                                                                                                                                                                                                                                                   'chemicals '
                                                                                                                                                                                                                                                   'and '
                                                                                                                                                                                                                                                   'selected '
                                                                                                                                                                                                                                                   'industrial '
                                                                                                                                                                                                                                                   'goods.',
 'Что именно импортируется из Китая': 'What Is Imported from China',
 'Китай: состав импорта': 'China: Import Composition',
 'По содержанию это прежде всего машины и оборудование, транспортные средства, электроника, пластмассы, химическая продукция и различные потребительские товары.': 'In '
                                                                                                                                                                   'terms '
                                                                                                                                                                   'of '
                                                                                                                                                                   'content, '
                                                                                                                                                                   'these '
                                                                                                                                                                   'are '
                                                                                                                                                                   'primarily '
                                                                                                                                                                   'machinery '
                                                                                                                                                                   'and '
                                                                                                                                                                   'equipment, '
                                                                                                                                                                   'vehicles, '
                                                                                                                                                                   'electronics, '
                                                                                                                                                                   'plastics, '
                                                                                                                                                                   'chemical '
                                                                                                                                                                   'products '
                                                                                                                                                                   'and '
                                                                                                                                                                   'various '
                                                                                                                                                                   'consumer '
                                                                                                                                                                   'goods.',
 'Подробная таблица состава импорта из Китая': 'Detailed Table of Import Composition from China',
 'Что именно импортируется из Индии': 'What Is Imported from India',
 'Индия: состав импорта': 'India: Import Composition',
 'Индийские поставки меньше по объему, но важны по отдельным нишам: фармацевтика, химия, машины и оборудование, электрооборудование, а также чай и пряности.': 'Indian '
                                                                                                                                                               'supplies '
                                                                                                                                                               'are '
                                                                                                                                                               'smaller '
                                                                                                                                                               'in '
                                                                                                                                                               'volume, '
                                                                                                                                                               'but '
                                                                                                                                                               'important '
                                                                                                                                                               'in '
                                                                                                                                                               'specific '
                                                                                                                                                               'niches: '
                                                                                                                                                               'pharmaceuticals, '
                                                                                                                                                               'chemicals, '
                                                                                                                                                               'machinery '
                                                                                                                                                               'and '
                                                                                                                                                               'equipment, '
                                                                                                                                                               'electrical '
                                                                                                                                                               'equipment, '
                                                                                                                                                               'as '
                                                                                                                                                               'well '
                                                                                                                                                               'as '
                                                                                                                                                               'tea '
                                                                                                                                                               'and '
                                                                                                                                                               'spices.',
 'Подробная таблица состава импорта из Индии': 'Detailed Table of Import Composition from India',
 'География экспортных партнеров': 'Geography of Export Partners',
 'Сравнение структуры 2000 и 2023 годов показывает перестройку направления российского экспорта. Главный сдвиг заключается в снижении роли западных рынков и усилении азиатского направления.': 'Comparing '
                                                                                                                                                                                                'the '
                                                                                                                                                                                                'structures '
                                                                                                                                                                                                'of '
                                                                                                                                                                                                '2000 '
                                                                                                                                                                                                'and '
                                                                                                                                                                                                '2023 '
                                                                                                                                                                                                'shows '
                                                                                                                                                                                                'a '
                                                                                                                                                                                                'restructuring '
                                                                                                                                                                                                'of '
                                                                                                                                                                                                'Russian '
                                                                                                                                                                                                'export '
                                                                                                                                                                                                'destinations. '
                                                                                                                                                                                                'The '
                                                                                                                                                                                                'main '
                                                                                                                                                                                                'shift '
                                                                                                                                                                                                'lies '
                                                                                                                                                                                                'in '
                                                                                                                                                                                                'the '
                                                                                                                                                                                                'declining '
                                                                                                                                                                                                'role '
                                                                                                                                                                                                'of '
                                                                                                                                                                                                'Western '
                                                                                                                                                                                                'markets '
                                                                                                                                                                                                'and '
                                                                                                                                                                                                'the '
                                                                                                                                                                                                'strengthening '
                                                                                                                                                                                                'of '
                                                                                                                                                                                                'the '
                                                                                                                                                                                                'Asian '
                                                                                                                                                                                                'direction.',
 'Ключевой структурный сдвиг': 'Key Structural Shift',
 'В 2000 году среди значимых направлений российского экспорта заметную роль играли европейские страны и США. К 2023 году центр тяжести сместился к Китаю и Индии, что подтверждается как графически, так и расчетом индексов структурных сдвигов.': 'In '
                                                                                                                                                                                                                                                    '2000, '
                                                                                                                                                                                                                                                    'European '
                                                                                                                                                                                                                                                    'countries '
                                                                                                                                                                                                                                                    'and '
                                                                                                                                                                                                                                                    'the '
                                                                                                                                                                                                                                                    'United '
                                                                                                                                                                                                                                                    'States '
                                                                                                                                                                                                                                                    'played '
                                                                                                                                                                                                                                                    'a '
                                                                                                                                                                                                                                                    'visible '
                                                                                                                                                                                                                                                    'role '
                                                                                                                                                                                                                                                    'among '
                                                                                                                                                                                                                                                    'major '
                                                                                                                                                                                                                                                    'destinations '
                                                                                                                                                                                                                                                    'of '
                                                                                                                                                                                                                                                    'Russian '
                                                                                                                                                                                                                                                    'exports. '
                                                                                                                                                                                                                                                    'By '
                                                                                                                                                                                                                                                    '2023, '
                                                                                                                                                                                                                                                    'the '
                                                                                                                                                                                                                                                    'center '
                                                                                                                                                                                                                                                    'of '
                                                                                                                                                                                                                                                    'gravity '
                                                                                                                                                                                                                                                    'shifted '
                                                                                                                                                                                                                                                    'to '
                                                                                                                                                                                                                                                    'China '
                                                                                                                                                                                                                                                    'and '
                                                                                                                                                                                                                                                    'India, '
                                                                                                                                                                                                                                                    'which '
                                                                                                                                                                                                                                                    'is '
                                                                                                                                                                                                                                                    'confirmed '
                                                                                                                                                                                                                                                    'both '
                                                                                                                                                                                                                                                    'visually '
                                                                                                                                                                                                                                                    'and '
                                                                                                                                                                                                                                                    'by '
                                                                                                                                                                                                                                                    'structural '
                                                                                                                                                                                                                                                    'shift '
                                                                                                                                                                                                                                                    'indices.',
 'Методологическое уточнение.': 'Methodological note.',
 'В данном блоке компании не используются как источник распределения товарооборота.': 'In this block, companies are '
                                                                                      'not used as a source for '
                                                                                      'allocating trade turnover.',
 'Они приведены для ориентира: в экспорте — как профильные российские производители и экспортеры соответствующих групп,': 'They '
                                                                                                                          'are '
                                                                                                                          'provided '
                                                                                                                          'as '
                                                                                                                          'a '
                                                                                                                          'reference '
                                                                                                                          'point: '
                                                                                                                          'in '
                                                                                                                          'exports, '
                                                                                                                          'as '
                                                                                                                          'relevant '
                                                                                                                          'Russian '
                                                                                                                          'producers '
                                                                                                                          'and '
                                                                                                                          'exporters '
                                                                                                                          'of '
                                                                                                                          'the '
                                                                                                                          'corresponding '
                                                                                                                          'groups,',
 'в импорте — как иностранные производители и бренды, продукция которых может быть представлена в российских поставках.': 'and '
                                                                                                                          'in '
                                                                                                                          'imports, '
                                                                                                                          'as '
                                                                                                                          'foreign '
                                                                                                                          'producers '
                                                                                                                          'and '
                                                                                                                          'brands '
                                                                                                                          'whose '
                                                                                                                          'products '
                                                                                                                          'may '
                                                                                                                          'be '
                                                                                                                          'represented '
                                                                                                                          'in '
                                                                                                                          'Russian '
                                                                                                                          'supplies.',
 'Для строгого ранжирования по компаниям необходима отдельная таможенная микростатистика по участникам ВЭД.': 'Strict '
                                                                                                              'ranking '
                                                                                                              'by '
                                                                                                              'company '
                                                                                                              'would '
                                                                                                              'require '
                                                                                                              'separate '
                                                                                                              'customs '
                                                                                                              'microstatistics '
                                                                                                              'on '
                                                                                                              'foreign '
                                                                                                              'trade '
                                                                                                              'participants.',
 'Зачем блок вынесен отдельно': 'Why This Block Is Separate',
 'На защите основное внимание можно оставить на динамике, структуре и коэффициентах. Справка по компаниям открывается при необходимости, если возникает вопрос о том, какие реальные производители стоят за укрупненными товарными группами.': 'At '
                                                                                                                                                                                                                                               'the '
                                                                                                                                                                                                                                               'defense, '
                                                                                                                                                                                                                                               'the '
                                                                                                                                                                                                                                               'main '
                                                                                                                                                                                                                                               'focus '
                                                                                                                                                                                                                                               'can '
                                                                                                                                                                                                                                               'remain '
                                                                                                                                                                                                                                               'on '
                                                                                                                                                                                                                                               'dynamics, '
                                                                                                                                                                                                                                               'structure '
                                                                                                                                                                                                                                               'and '
                                                                                                                                                                                                                                               'ratios. '
                                                                                                                                                                                                                                               'The '
                                                                                                                                                                                                                                               'company '
                                                                                                                                                                                                                                               'reference '
                                                                                                                                                                                                                                               'can '
                                                                                                                                                                                                                                               'be '
                                                                                                                                                                                                                                               'opened '
                                                                                                                                                                                                                                               'if '
                                                                                                                                                                                                                                               'a '
                                                                                                                                                                                                                                               'question '
                                                                                                                                                                                                                                               'arises '
                                                                                                                                                                                                                                               'about '
                                                                                                                                                                                                                                               'which '
                                                                                                                                                                                                                                               'real '
                                                                                                                                                                                                                                               'producers '
                                                                                                                                                                                                                                               'stand '
                                                                                                                                                                                                                                               'behind '
                                                                                                                                                                                                                                               'the '
                                                                                                                                                                                                                                               'aggregated '
                                                                                                                                                                                                                                               'commodity '
                                                                                                                                                                                                                                               'groups.',
 'Российский экспорт': 'Russian Exports',
 'Российский импорт': 'Russian Imports',
 'Экспорт России в Китай: профильные российские экспортеры': 'Russian Exports to China: Relevant Russian Exporters',
 'Экспорт России в Индию: профильные российские экспортеры': 'Russian Exports to India: Relevant Russian Exporters',
 'Импорт России из Китая: иностранные производители и бренды': 'Russian Imports from China: Foreign Producers and '
                                                               'Brands',
 'Импорт России из Индии: иностранные производители и бренды': 'Russian Imports from India: Foreign Producers and '
                                                               'Brands',
 'Таблица-справка по экспортным группам': 'Reference Table for Export Groups',
 'Таблица-справка по импортным группам': 'Reference Table for Import Groups',
 'Индексы и коэффициенты': 'Indices and Ratios',
 'Этот блок переводит наблюдаемые изменения в формальные статистические показатели. Индексы Гатева и Салаи измеряют силу структурного сдвига, а коэффициент покрытия отражает соотношение экспорта и импорта.': 'This '
                                                                                                                                                                                                                'block '
                                                                                                                                                                                                                'converts '
                                                                                                                                                                                                                'observed '
                                                                                                                                                                                                                'changes '
                                                                                                                                                                                                                'into '
                                                                                                                                                                                                                'formal '
                                                                                                                                                                                                                'statistical '
                                                                                                                                                                                                                'indicators. '
                                                                                                                                                                                                                'The '
                                                                                                                                                                                                                'Gatev '
                                                                                                                                                                                                                'and '
                                                                                                                                                                                                                'Salai '
                                                                                                                                                                                                                'indices '
                                                                                                                                                                                                                'measure '
                                                                                                                                                                                                                'the '
                                                                                                                                                                                                                'strength '
                                                                                                                                                                                                                'of '
                                                                                                                                                                                                                'structural '
                                                                                                                                                                                                                'shifts, '
                                                                                                                                                                                                                'while '
                                                                                                                                                                                                                'the '
                                                                                                                                                                                                                'coverage '
                                                                                                                                                                                                                'ratio '
                                                                                                                                                                                                                'reflects '
                                                                                                                                                                                                                'the '
                                                                                                                                                                                                                'ratio '
                                                                                                                                                                                                                'of '
                                                                                                                                                                                                                'exports '
                                                                                                                                                                                                                'to '
                                                                                                                                                                                                                'imports.',
 'Интерпретация:': 'Interpretation:',
 'чем ближе индекс к 1, тем сильнее структурный сдвиг. Значения, полученные для внешней торговли,': 'the closer the '
                                                                                                    'index is to 1, '
                                                                                                    'the stronger the '
                                                                                                    'structural shift. '
                                                                                                    'The values '
                                                                                                    'obtained for '
                                                                                                    'foreign trade',
 'подтверждают, что изменение географии торговли было существенным, а не только визуально заметным.': 'confirm that '
                                                                                                      'the change in '
                                                                                                      'trade geography '
                                                                                                      'was '
                                                                                                      'substantial, '
                                                                                                      'not merely '
                                                                                                      'visually '
                                                                                                      'noticeable.',
 'Что фиксируют индексы': 'What the Indices Capture',
 'Высокие значения индексов показывают сильную перестройку географии торговли. В экспорте это связано с ростом роли Китая и Индии, а в импорте — прежде всего с усилением китайского направления как основного источника поставок.': 'High '
                                                                                                                                                                                                                                     'index '
                                                                                                                                                                                                                                     'values '
                                                                                                                                                                                                                                     'indicate '
                                                                                                                                                                                                                                     'a '
                                                                                                                                                                                                                                     'strong '
                                                                                                                                                                                                                                     'restructuring '
                                                                                                                                                                                                                                     'of '
                                                                                                                                                                                                                                     'trade '
                                                                                                                                                                                                                                     'geography. '
                                                                                                                                                                                                                                     'In '
                                                                                                                                                                                                                                     'exports, '
                                                                                                                                                                                                                                     'this '
                                                                                                                                                                                                                                     'is '
                                                                                                                                                                                                                                     'associated '
                                                                                                                                                                                                                                     'with '
                                                                                                                                                                                                                                     'the '
                                                                                                                                                                                                                                     'growing '
                                                                                                                                                                                                                                     'role '
                                                                                                                                                                                                                                     'of '
                                                                                                                                                                                                                                     'China '
                                                                                                                                                                                                                                     'and '
                                                                                                                                                                                                                                     'India; '
                                                                                                                                                                                                                                     'in '
                                                                                                                                                                                                                                     'imports, '
                                                                                                                                                                                                                                     'primarily '
                                                                                                                                                                                                                                     'with '
                                                                                                                                                                                                                                     'the '
                                                                                                                                                                                                                                     'strengthening '
                                                                                                                                                                                                                                     'of '
                                                                                                                                                                                                                                     'the '
                                                                                                                                                                                                                                     'China '
                                                                                                                                                                                                                                     'direction '
                                                                                                                                                                                                                                     'as '
                                                                                                                                                                                                                                     'the '
                                                                                                                                                                                                                                     'main '
                                                                                                                                                                                                                                     'source '
                                                                                                                                                                                                                                     'of '
                                                                                                                                                                                                                                     'supplies.',
 'Коэффициент покрытия': 'Coverage Ratio',
 'Коэффициент покрытия равен отношению экспорта к импорту. Значение выше 1 означает, что экспорт превышает импорт; значение ниже 1 — импорт превышает экспорт. Для удобства на графике проведена линия равновесия.': 'The '
                                                                                                                                                                                                                     'coverage '
                                                                                                                                                                                                                     'ratio '
                                                                                                                                                                                                                     'equals '
                                                                                                                                                                                                                     'exports '
                                                                                                                                                                                                                     'divided '
                                                                                                                                                                                                                     'by '
                                                                                                                                                                                                                     'imports. '
                                                                                                                                                                                                                     'A '
                                                                                                                                                                                                                     'value '
                                                                                                                                                                                                                     'above '
                                                                                                                                                                                                                     '1 '
                                                                                                                                                                                                                     'means '
                                                                                                                                                                                                                     'exports '
                                                                                                                                                                                                                     'exceed '
                                                                                                                                                                                                                     'imports; '
                                                                                                                                                                                                                     'a '
                                                                                                                                                                                                                     'value '
                                                                                                                                                                                                                     'below '
                                                                                                                                                                                                                     '1 '
                                                                                                                                                                                                                     'means '
                                                                                                                                                                                                                     'imports '
                                                                                                                                                                                                                     'exceed '
                                                                                                                                                                                                                     'exports. '
                                                                                                                                                                                                                     'For '
                                                                                                                                                                                                                     'clarity, '
                                                                                                                                                                                                                     'an '
                                                                                                                                                                                                                     'equilibrium '
                                                                                                                                                                                                                     'line '
                                                                                                                                                                                                                     'is '
                                                                                                                                                                                                                     'shown '
                                                                                                                                                                                                                     'on '
                                                                                                                                                                                                                     'the '
                                                                                                                                                                                                                     'chart.',
 'В 2023 году коэффициент покрытия составил': 'In 2023, the coverage ratio was',
 'Экспорт превышал импорт, но соотношение оставалось относительно близким к равновесию.': 'Exports exceeded imports, '
                                                                                          'but the ratio remained '
                                                                                          'relatively close to '
                                                                                          'equilibrium.',
 'Значение отражает экстремальное превышение российского экспорта над импортом из Индии.': 'The value reflects an '
                                                                                           'extreme excess of Russian '
                                                                                           'exports over imports from '
                                                                                           'India.',
 'Исходные таблицы': 'Source Tables',
 'Этот раздел оставлен для проверки числовой базы графиков. Здесь можно посмотреть ряды, из которых построены визуализации: оборот, экспорт, импорт, сальдо и коэффициент покрытия.': 'This '
                                                                                                                                                                                      'section '
                                                                                                                                                                                      'is '
                                                                                                                                                                                      'left '
                                                                                                                                                                                      'for '
                                                                                                                                                                                      'checking '
                                                                                                                                                                                      'the '
                                                                                                                                                                                      'numerical '
                                                                                                                                                                                      'base '
                                                                                                                                                                                      'of '
                                                                                                                                                                                      'the '
                                                                                                                                                                                      'charts. '
                                                                                                                                                                                      'Here '
                                                                                                                                                                                      'one '
                                                                                                                                                                                      'can '
                                                                                                                                                                                      'view '
                                                                                                                                                                                      'the '
                                                                                                                                                                                      'series '
                                                                                                                                                                                      'used '
                                                                                                                                                                                      'to '
                                                                                                                                                                                      'build '
                                                                                                                                                                                      'the '
                                                                                                                                                                                      'visualizations: '
                                                                                                                                                                                      'turnover, '
                                                                                                                                                                                      'exports, '
                                                                                                                                                                                      'imports, '
                                                                                                                                                                                      'balance '
                                                                                                                                                                                      'and '
                                                                                                                                                                                      'coverage '
                                                                                                                                                                                      'ratio.',
 'Единицы измерения': 'Units of Measurement',
 'В исходных рядах денежные показатели хранятся в базовых единицах датасета, а на графиках приводятся к млрд долларов США для удобства чтения. Коэффициент покрытия является безразмерным отношением.': 'In '
                                                                                                                                                                                                        'the '
                                                                                                                                                                                                        'source '
                                                                                                                                                                                                        'series, '
                                                                                                                                                                                                        'monetary '
                                                                                                                                                                                                        'indicators '
                                                                                                                                                                                                        'are '
                                                                                                                                                                                                        'stored '
                                                                                                                                                                                                        'in '
                                                                                                                                                                                                        'the '
                                                                                                                                                                                                        'base '
                                                                                                                                                                                                        'units '
                                                                                                                                                                                                        'of '
                                                                                                                                                                                                        'the '
                                                                                                                                                                                                        'dataset, '
                                                                                                                                                                                                        'while '
                                                                                                                                                                                                        'charts '
                                                                                                                                                                                                        'present '
                                                                                                                                                                                                        'them '
                                                                                                                                                                                                        'in '
                                                                                                                                                                                                        'USD '
                                                                                                                                                                                                        'billions '
                                                                                                                                                                                                        'for '
                                                                                                                                                                                                        'easier '
                                                                                                                                                                                                        'reading. '
                                                                                                                                                                                                        'The '
                                                                                                                                                                                                        'coverage '
                                                                                                                                                                                                        'ratio '
                                                                                                                                                                                                        'is '
                                                                                                                                                                                                        'a '
                                                                                                                                                                                                        'dimensionless '
                                                                                                                                                                                                        'ratio.',
 'Год': 'Year',
 'Оборот': 'Turnover',
 'Экспорт': 'Export',
 'Импорт': 'Import',
 'Сальдо': 'Balance',
 'Стоимость': 'Value',
 'Доля': 'Share',
 'Товарная группа': 'Commodity group',
 'Что входит в группу': 'What the group includes',
 'Примеры продукции': 'Product examples',
 'Компании': 'Companies',
 'Где используется': 'Where it is used',
 'Типичная продукция': 'Typical products',
 'Профильные российские производители и экспортеры': 'Relevant Russian producers and exporters',
 'Иностранные производители и бренды': 'Foreign producers and brands',
 'Направление': 'Direction',
 'Страна': 'Country',
 'Индекс Гатева': 'Gatev Index',
 'Индекс Салаи': 'Salai Index',
 'значение индекса': 'index value',
 'доля, %': 'share, %',
 'доля лидера': 'leader share',
 'ключевая группа': 'key group',
 'экспорт = импорт': 'exports = imports',
 'коэффициент покрытия, раз': 'coverage ratio, times',
 'коэффициент покрытия': 'coverage ratio',
 'экспорт / импорт': 'exports / imports',
 'граница баланса = 1': 'balance threshold = 1',
 'дополнительная ось торгового треугольника': 'additional axis of the trade triangle',
 'экспорт': 'export',
 'импорт': 'import',
 'сальдо': 'balance',
 'оборот': 'turnover',
 'год; рост к началу периода —': 'year; growth since the beginning of the period —',
 'рост к началу периода': 'growth since the beginning of the period',
 'Экспорт:': 'Export:',
 '; импорт:': '; import:',
 'экспорт ': 'export ',
 'или': 'or',
 'от показанного состава': 'of the displayed structure',
 'в показанной структуре': 'in the displayed structure',
 'В группу входят:': 'The group includes:',
 'Три крупнейшие группы:': 'The three largest groups:',
 'млрд долларов США': 'USD billion',
 'млрд $': 'USD bn',
 'млрд': 'bn',
 'раза': 'times',
 'в ': 'x',
 'сырая нефть и нефтепродукты, природный газ, уголь и иные виды минерального топлива': 'crude oil and petroleum '
                                                                                       'products, natural gas, coal '
                                                                                       'and other mineral fuels',
 'нефть марок Urals и ESPO, нефтепродукты, уголь, природный газ': 'Urals and ESPO crude oil, petroleum products, coal '
                                                                  'and natural gas',
 'станки, промышленное оборудование, насосы, компрессоры, двигатели, комплектующие и механические устройства': 'machine '
                                                                                                               'tools, '
                                                                                                               'industrial '
                                                                                                               'equipment, '
                                                                                                               'pumps, '
                                                                                                               'compressors, '
                                                                                                               'engines, '
                                                                                                               'components '
                                                                                                               'and '
                                                                                                               'mechanical '
                                                                                                               'devices',
 'станки, насосы, компрессоры, строительная и промышленная техника, комплектующие': 'machine tools, pumps, '
                                                                                    'compressors, construction and '
                                                                                    'industrial machinery, components',
 'электроника, кабели, аккумуляторы, электрические машины, компоненты связи и бытовая техника': 'electronics, cables, '
                                                                                                'batteries, electrical '
                                                                                                'machinery, '
                                                                                                'communication '
                                                                                                'components and '
                                                                                                'household appliances',
 'кабели, аккумуляторы, бытовая техника, компоненты связи, смартфоны, компьютеры': 'cables, batteries, household '
                                                                                   'appliances, communication '
                                                                                   'components, smartphones and '
                                                                                   'computers',
 'автомобили, грузовой транспорт, автокомпоненты, спецтехника и части транспортных средств': 'cars, freight vehicles, '
                                                                                             'auto components, '
                                                                                             'special-purpose '
                                                                                             'machinery and vehicle '
                                                                                             'parts',
 'легковые автомобили, грузовики, автобусы, спецтехника, автокомпоненты': 'passenger cars, trucks, buses, '
                                                                          'special-purpose vehicles and auto '
                                                                          'components',
 'лекарственные средства, субстанции, медицинские препараты и фармацевтическая продукция': 'medicines, active '
                                                                                           'substances, medical '
                                                                                           'preparations and '
                                                                                           'pharmaceutical products',
 'дженерики, субстанции, антибиотики, кардиологические и противовирусные препараты': 'generics, active substances, '
                                                                                     'antibiotics, cardiovascular and '
                                                                                     'antiviral medicines',
 'калийные, азотные и смешанные минеральные удобрения': 'potash, nitrogen and mixed mineral fertilizers',
 'калийные, азотные, фосфорные и комплексные минеральные удобрения': 'potash, nitrogen, phosphate and compound mineral '
                                                                     'fertilizers',
 'растительные масла, прежде всего подсолнечное и иные масложировые товары': 'vegetable oils, primarily sunflower oil, '
                                                                             'and other oil-and-fat products',
 'подсолнечное масло, соевое масло, рапсовое масло, масложировое сырье': 'sunflower oil, soybean oil, rapeseed oil and '
                                                                         'oil-and-fat raw materials',
 'железные и цветные руды, концентраты, шлаки и зола': 'ferrous and non-ferrous ores, concentrates, slag and ash',
 'железорудный концентрат, медные и никелевые руды, шлаки и зола': 'iron ore concentrate, copper and nickel ores, slag '
                                                                   'and ash',
 'алюминий необработанный, полуфабрикаты и изделия из алюминия': 'unwrought aluminum, semi-finished products and '
                                                                 'aluminum goods',
 'первичный алюминий, алюминиевые сплавы, прокат и полуфабрикаты': 'primary aluminum, aluminum alloys, rolled products '
                                                                   'and semi-finished products',
 'рафинированная медь, медные сплавы, полуфабрикаты и изделия из меди': 'refined copper, copper alloys, semi-finished '
                                                                        'products and copper goods',
 'рафинированная медь, медная катанка, сплавы и полуфабрикаты': 'refined copper, copper rod, alloys and semi-finished '
                                                                'products',
 'лесоматериалы, пиломатериалы, древесина и продукция первичной обработки': 'timber, sawn wood, wood and primary '
                                                                            'processed products',
 'пиломатериалы, фанера, целлюлозное сырье, продукция первичной обработки древесины': 'sawn wood, plywood, pulp raw '
                                                                                      'materials and primary processed '
                                                                                      'wood products',
 'рыба, ракообразные, морепродукты и замороженная рыбная продукция': 'fish, crustaceans, seafood and frozen fish '
                                                                     'products',
 'минтай, краб, лососевые, морепродукты, замороженная рыбная продукция': 'pollock, crab, salmonids, seafood and frozen '
                                                                         'fish products',
 'целлюлоза, бумажная масса, бумага и картон': 'pulp, paper pulp, paper and cardboard',
 'целлюлоза, бумажная масса, бумага, картон, упаковочные материалы': 'pulp, paper pulp, paper, cardboard and packaging '
                                                                     'materials',
 'каучук, резина, шины, изделия из резины и полимерные материалы': 'rubber, tires, rubber goods and polymer materials',
 'синтетический каучук, резинотехнические изделия, шины и полимерные материалы': 'synthetic rubber, rubber technical '
                                                                                 'goods, tires and polymer materials',
 'пластмассы, полимерные материалы, упаковочные материалы и изделия из пластика': 'plastics, polymer materials, '
                                                                                  'packaging materials and plastic '
                                                                                  'goods',
 'полимеры, пленки, упаковка, изделия из пластмасс, комплектующие': 'polymers, films, packaging, plastic goods and '
                                                                    'components',
 'органическая и неорганическая химия, реактивы, химические полуфабрикаты': 'organic and inorganic chemicals, reagents '
                                                                            'and chemical semi-finished products',
 'органическая и неорганическая химия, реактивы, промежуточные продукты, красители': 'organic and inorganic chemicals, '
                                                                                     'reagents, intermediates and dyes',
 'изделия из черных и цветных металлов, металлоконструкции и полуфабрикаты': 'ferrous and non-ferrous metal products, '
                                                                             'metal structures and semi-finished '
                                                                             'products',
 'металлоконструкции, крепеж, прокат, полуфабрикаты и изделия из черных и цветных металлов': 'metal structures, '
                                                                                             'fasteners, rolled '
                                                                                             'products, semi-finished '
                                                                                             'products and ferrous and '
                                                                                             'non-ferrous metal goods',
 'обувь, элементы обуви и потребительские товары легкой промышленности': 'footwear, footwear components and '
                                                                         'light-industry consumer goods',
 'спортивная, повседневная и специальная обувь, подошвы, элементы обуви': 'sports, casual and special-purpose '
                                                                          'footwear, soles and footwear components',
 'текстиль, одежда, трикотаж и готовые изделия легкой промышленности': 'textiles, clothing, knitwear and finished '
                                                                       'light-industry goods',
 'трикотаж, верхняя одежда, текстильные изделия, готовая одежда': 'knitwear, outerwear, textile products and '
                                                                  'ready-made clothing',
 'игрушки, спортивные товары, инвентарь и отдельные потребительские товары': 'toys, sporting goods, equipment and '
                                                                             'selected consumer goods',
 'игрушки, спортивный инвентарь, настольные игры, товары для досуга': 'toys, sports equipment, board games and leisure '
                                                                      'goods',
 'мебель, осветительные приборы, интерьерные товары и бытовые изделия': 'furniture, lighting fixtures, interior goods '
                                                                        'and household items',
 'корпусная мебель, офисная мебель, светильники, интерьерные изделия': 'cabinet furniture, office furniture, lighting '
                                                                       'fixtures and interior goods',
 'керамические изделия, плитка, санитарная керамика и огнеупорные материалы': 'ceramic products, tiles, sanitary '
                                                                              'ceramics and refractory materials',
 'плитка, санитарная керамика, огнеупорные изделия, техническая керамика': 'tiles, sanitary ceramics, refractory goods '
                                                                           'and technical ceramics',
 'чай, пряности, кофе и отдельные продовольственные товары': 'tea, spices, coffee and selected food products',
 'ассамский чай, дарджилинг, черный чай, пряности, перец, кардамон': 'Assam tea, Darjeeling, black tea, spices, pepper '
                                                                     'and cardamom',
 'перец, кардамон, куркума, кориандр, смеси специй': 'pepper, cardamom, turmeric, coriander and spice blends',
 'драгоценные камни, металлы и отдельные товары ювелирной группы': 'precious stones, metals and selected jewelry-group '
                                                                   'goods',
 'алмазы, бриллианты, драгоценные камни, ювелирное сырье': 'diamonds, polished diamonds, precious stones and jewelry '
                                                           'raw materials',
 'товары соответствующей укрупненной группы внешнеторговой классификации': 'goods of the corresponding aggregated '
                                                                           'foreign trade classification group',
 'разнородные товары, не вошедшие в основные укрупненные группы': 'heterogeneous goods not included in the main '
                                                                  'aggregated groups',
 'без выделения конкретной компании из-за смешанного состава категории': 'without identifying a specific company due '
                                                                         'to the mixed composition of the category',
 'зависит от конкретных товарных кодов внутри группы': 'depends on the specific commodity codes within the group',
 'конкретные компании зависят от детального товарного кода и источника поставки': 'specific companies depend on the '
                                                                                  'detailed commodity code and source '
                                                                                  'of supply',
 'применение зависит от состава укрупненной товарной группы': 'the use depends on the composition of the aggregated '
                                                              'commodity group',
 'точное распределение по российским экспортерам требует детализации по компаниям и товарным кодам': 'precise '
                                                                                                     'allocation by '
                                                                                                     'Russian '
                                                                                                     'exporters '
                                                                                                     'requires '
                                                                                                     'company-level '
                                                                                                     'and '
                                                                                                     'commodity-code '
                                                                                                     'detail',
 'конкретные иностранные производители зависят от детального товарного кода, поставщика и канала ввоза': 'specific '
                                                                                                         'foreign '
                                                                                                         'producers '
                                                                                                         'depend on '
                                                                                                         'the detailed '
                                                                                                         'commodity '
                                                                                                         'code, '
                                                                                                         'supplier and '
                                                                                                         'import '
                                                                                                         'channel',
 'переработка на НПЗ, производство топлива, нефтехимия, энергетика': 'oil refining, fuel production, petrochemicals '
                                                                     'and energy',
 'строительство, промышленное производство, добыча, транспортная и складская инфраструктура': 'construction, '
                                                                                              'industrial production, '
                                                                                              'mining, transport and '
                                                                                              'warehouse '
                                                                                              'infrastructure',
 'потребительский рынок, связь, ИТ-инфраструктура, промышленная автоматизация': 'consumer market, communications, IT '
                                                                                'infrastructure and industrial '
                                                                                'automation',
 'личный транспорт, логистика, строительные работы, перевозки и автосервис': 'personal transport, logistics, '
                                                                             'construction works, transportation and '
                                                                             'auto services',
 'здравоохранение, аптечный рынок, больничные закупки, производство лекарств': 'healthcare, pharmacy market, hospital '
                                                                               'procurement and medicine production',
 'сельское хозяйство, повышение урожайности зерновых, масличных и технических культур': 'agriculture, increasing '
                                                                                        'yields of grain, oilseed and '
                                                                                        'industrial crops',
 'пищевая промышленность, производство готовых продуктов, розничный продовольственный рынок': 'food industry, '
                                                                                              'production of finished '
                                                                                              'foods and retail food '
                                                                                              'market',
 'черная и цветная металлургия, производство стали, сплавов и промышленных материалов': 'ferrous and non-ferrous '
                                                                                        'metallurgy, steel, alloys and '
                                                                                        'industrial materials '
                                                                                        'production',
 'автомобилестроение, строительство, упаковка, энергетика, производство кабелей': 'automotive industry, construction, '
                                                                                  'packaging, energy and cable '
                                                                                  'production',
 'электротехника, кабельная продукция, электроника, машиностроение': 'electrical engineering, cable products, '
                                                                     'electronics and mechanical engineering',
 'строительство, мебельное производство, упаковка, бумажная промышленность': 'construction, furniture production, '
                                                                             'packaging and paper industry',
 'пищевая промышленность, переработка, розничная торговля, общественное питание': 'food industry, processing, retail '
                                                                                  'trade and food service',
 'бумажная промышленность, упаковка, санитарно-гигиенические изделия': 'paper industry, packaging and sanitary-hygiene '
                                                                       'products',
 'автопром, шинная промышленность, строительство, промышленная резина': 'automotive industry, tire industry, '
                                                                        'construction and industrial rubber',
 'упаковка, бытовые товары, автокомпоненты, строительные материалы': 'packaging, household goods, auto components and '
                                                                     'construction materials',
 'фармацевтика, сельское хозяйство, производство пластмасс, лакокрасочная промышленность': 'pharmaceuticals, '
                                                                                           'agriculture, plastics '
                                                                                           'production and '
                                                                                           'paint-and-coatings '
                                                                                           'industry',
 'строительство, машиностроение, инфраструктурные проекты, промышленное оборудование': 'construction, mechanical '
                                                                                       'engineering, infrastructure '
                                                                                       'projects and industrial '
                                                                                       'equipment',
 'розничная торговля, спорт, повседневное потребление, рабочая экипировка': 'retail trade, sports, everyday '
                                                                            'consumption and workwear',
 'розничная торговля, массовый потребительский рынок, спортивная одежда': 'retail trade, mass consumer market and '
                                                                          'sportswear',
 'детские товары, спорт, досуг, розничная торговля': 'children’s goods, sports, leisure and retail trade',
 'домохозяйства, офисы, гостиницы, торговые помещения': 'households, offices, hotels and retail premises',
 'строительство, ремонт, отделочные работы, промышленная теплоизоляция': 'construction, repair, finishing works and '
                                                                         'industrial thermal insulation',
 'розничная торговля, общественное питание, пищевая промышленность': 'retail trade, food service and food industry',
 'пищевая промышленность, розничная торговля, общественное питание': 'food industry, retail trade and food service',
 'огранка, ювелирное производство, инвестиционные и промышленные применения': 'cutting, jewelry production, investment '
                                                                              'and industrial applications',
 ' — как ориентиры по отрасли': ' — as industry reference points',
 ' — примеры компаний по группе': ' — examples of companies in the group',
 ' — примеры брендов по группе': ' — examples of brands in the group',
 ' — примеры индийских фармкомпаний': ' — examples of Indian pharmaceutical companies',
 ' — примеры российских производителей': ' — examples of Russian producers',
 ' — примеры компаний масложирового сектора': ' — examples of companies in the oil-and-fat sector',
 ' — примеры компаний сырьевого и металлургического контура': ' — examples of companies in the raw-material and '
                                                              'metallurgical segments',
 ' — основной российский ориентир по алюминиевой продукции': ' — the main Russian reference point for aluminum '
                                                             'products',
 ' — примеры компаний медного и цветного металлургического сектора': ' — examples of companies in the copper and '
                                                                     'non-ferrous metallurgy sector',
 ' — примеры российских компаний лесопромышленного комплекса': ' — examples of Russian timber-industry companies',
 ' — примеры отраслевых компаний': ' — examples of industry companies',
 ' — примеры производителей отрасли': ' — examples of industry producers',
 ' — примеры компаний и брендов по группе': ' — examples of companies and brands in the group',
 ' — примеры китайских химических компаний': ' — examples of Chinese chemical companies',
 ' — примеры компаний металлургического сектора': ' — examples of metallurgical companies',
 ' — примеры китайских брендов потребительского сегмента': ' — examples of Chinese consumer-segment brands',
 ' — примеры китайских брендов легкой промышленности': ' — examples of Chinese light-industry brands',
 ' — примеры китайских производителей мебели': ' — examples of Chinese furniture producers',
 ' — примеры индийских производителей керамики': ' — examples of Indian ceramic producers',
 ' — примеры индийских чайных брендов': ' — examples of Indian tea brands',
 ' — примеры индийских брендов специй': ' — examples of Indian spice brands',
 ' — основной российский ориентир по алмазной отрасли': ' — the main Russian reference point for the diamond industry',
 ' — профильные российские производители и экспортеры топливно-энергетического сектора': ' — relevant Russian '
                                                                                         'producers and exporters in '
                                                                                         'the fuel and energy sector',
 ' — крупные российские производители и экспортеры минеральных удобрений': ' — major Russian producers and exporters '
                                                                           'of mineral fertilizers',
 ' — профильные российские компании масложирового сектора': ' — relevant Russian companies in the oil-and-fat sector',
 ' — ключевой российский производитель алюминия и алюминиевой продукции': ' — a key Russian producer of aluminum and '
                                                                          'aluminum products',
 ' — профильные российские компании цветной металлургии': ' — relevant Russian non-ferrous metallurgy companies',
 ' — крупные российские компании лесопромышленного комплекса': ' — major Russian timber-industry companies',
 ' — профильные компании рыбопромышленного сектора': ' — relevant companies in the fishery sector',
 ' — профильные российские производители целлюлозно-бумажной продукции': ' — relevant Russian producers of pulp and '
                                                                         'paper products',
 ' — ключевой российский ориентир по алмазной отрасли': ' — a key Russian reference point in the diamond industry',
 ' — профильные российские производители машиностроительного контура': ' — relevant Russian producers in mechanical '
                                                                       'engineering',
 ' — профильные российские производители химической продукции': ' — relevant Russian producers of chemical products',
 ' — крупные российские компании металлургического сектора': ' — major Russian metallurgical companies',
 'Российские производители электротехнической и кабельной продукции; конкретный состав зависит от товарных кодов': 'Russian '
                                                                                                                   'producers '
                                                                                                                   'of '
                                                                                                                   'electrical '
                                                                                                                   'and '
                                                                                                                   'cable '
                                                                                                                   'products; '
                                                                                                                   'the '
                                                                                                                   'specific '
                                                                                                                   'composition '
                                                                                                                   'depends '
                                                                                                                   'on '
                                                                                                                   'commodity '
                                                                                                                   'codes',
 ' — крупные китайские производители строительной, промышленной и двигательной техники': ' — major Chinese producers '
                                                                                         'of construction, industrial '
                                                                                         'and engine equipment',
 ' — китайские производители электроники, бытовой техники и компонентов': ' — Chinese producers of electronics, home '
                                                                          'appliances and components',
 ' — китайские автомобильные бренды, активно представленные на российском рынке': ' — Chinese automotive brands '
                                                                                  'actively represented in the Russian '
                                                                                  'market',
 ' — китайские производители химической и полимерной продукции': ' — Chinese producers of chemical and polymer '
                                                                 'products',
 ' — крупные китайские химические компании': ' — major Chinese chemical companies',
 ' — китайские производители каучука, шин и резинотехнической продукции': ' — Chinese producers of rubber, tires and '
                                                                          'rubber technical goods',
 ' — крупные китайские металлургические компании': ' — major Chinese metallurgical companies',
 ' — китайские производители мебели и интерьерных товаров': ' — Chinese producers of furniture and interior goods',
 ' — крупные индийские фармацевтические производители': ' — major Indian pharmaceutical producers',
 ' — индийские производители оборудования, компонентов и техники': ' — Indian producers of equipment, components and '
                                                                   'machinery',
 ' — индийские производители электротехнической продукции и оборудования': ' — Indian producers of electrical products '
                                                                           'and equipment',
 ' — индийские компании химического и фармацевтического контура': ' — Indian companies in the chemical and '
                                                                  'pharmaceutical segments',
 ' — индийские производители керамической продукции': ' — Indian producers of ceramic products',
 ' — индийские чайные бренды': ' — Indian tea brands',
 ' — индийские бренды специй и продовольственных товаров': ' — Indian brands of spices and food products',
 ' — крупные индийские металлургические компании': ' — major Indian metallurgical companies',
 'Lego производится глобально, а в китайском сегменте заметны Sembo и Mould King как примеры категории': 'Lego is '
                                                                                                         'produced '
                                                                                                         'globally, '
                                                                                                         'while Sembo '
                                                                                                         'and Mould '
                                                                                                         'King are '
                                                                                                         'visible '
                                                                                                         'examples in '
                                                                                                         'the Chinese '
                                                                                                         'segment of '
                                                                                                         'the category',
 'Sembo, Mould King и другие производители потребительских товаров; категория неоднородна': 'Sembo, Mould King and '
                                                                                            'other consumer goods '
                                                                                            'producers; the category '
                                                                                            'is heterogeneous',
 'Китай': 'China',
 'Индия': 'India',
 'Россия': 'Russia',
 'РФ': 'Russia'}

LOCALES.update({'stats04_text_001': {'ru': 'Статистический анализ внешней торговли', 'en': 'Statistical Analysis of Foreign Trade'},
 'stats04_text_002': {'ru': 'Статистический анализ внешней торговли — пояснительная версия страницы.',
                      'en': 'Statistical analysis of foreign trade — explanatory page version.'},
 'stats04_text_003': {'ru': 'Глава 2 · статистическая база исследования',
                      'en': 'Chapter 2 · statistical base of the study'},
 'stats04_text_004': {'ru': 'В разделе представлены расчеты по динамике, структуре и сбалансированности торговли '
                            'России с Китаем и Индией.',
                      'en': 'This section presents calculations on the dynamics, structure and balance of Russia’s '
                            'trade with China and India.'},
 'stats04_text_005': {'ru': 'Особое внимание уделяется не только объему торговли, но и ее содержанию: какие товарные '
                            'группы формируют экспорт и импорт,',
                      'en': 'Special attention is paid not only to trade volume, but also to its composition: which '
                            'commodity groups form exports and imports,'},
 'stats04_text_006': {'ru': 'как изменилась география партнеров и насколько экспортная выручка покрывает импортные '
                            'закупки.',
                      'en': 'how the geography of partners has changed and how far export revenues cover import '
                            'purchases.'},
 'stats04_text_007': {'ru': 'Порядок чтения раздела', 'en': 'How to Read the Section'},
 'stats04_text_008': {'ru': 'Сначала рассматривается масштаб торговли во времени, затем — экспортно-импортная '
                            'структура, далее формально оцениваются структурные сдвиги и коэффициент покрытия. Такой '
                            'порядок позволяет связать графики с экономической интерпретацией: объем → состав → '
                            'изменение структуры → устойчивость торгового баланса.',
                      'en': 'First, the scale of trade over time is considered; then the export-import structure is '
                            'examined; after that, structural shifts and the coverage ratio are formally assessed. '
                            'This order makes it possible to connect the charts with economic interpretation: volume → '
                            'composition → structural change → stability of the trade balance.'},
 'stats04_text_009': {'ru': 'Динамический блок', 'en': 'Dynamics Block'},
 'stats04_text_010': {'ru': 'Динамика показывает, что российско-китайская торговля формировалась как долгосрочный '
                            'крупный контур, тогда как российско-индийское направление резко усилилось в последние '
                            'годы за счет экспортного потока.',
                      'en': 'The dynamics show that Russia-China trade formed as a long-term large-scale track, while '
                            'the Russia-India direction strengthened sharply in recent years due to export flows.'},
 'stats04_text_011': {'ru': 'Внешнеторговый оборот', 'en': 'Foreign Trade Turnover'},
 'stats04_text_012': {'ru': 'Оборот равен сумме экспорта и импорта. Он показывает масштаб торгового взаимодействия, но '
                            'сам по себе не отвечает на вопрос о выгоде или качестве структуры. Поэтому далее '
                            'показатель сопоставляется с сальдо и составом товарных потоков.',
                      'en': 'Turnover equals the sum of exports and imports. It shows the scale of trade interaction, '
                            'but by itself does not answer questions about benefit or structural quality. Therefore, '
                            'the indicator is further compared with the trade balance and the composition of commodity '
                            'flows.'},
 'stats04_text_013': {'ru': 'перестройка торговых потоков после 2022 года',
                      'en': 'restructuring of trade flows after 2022'},
 'stats04_text_014': {'ru': 'Китайское направление', 'en': 'China Direction'},
 'stats04_text_015': {'ru': 'Индийское направление', 'en': 'India Direction'},
 'stats04_text_016': {'ru': 'Экспорт и импорт', 'en': 'Exports and Imports'},
 'stats04_text_017': {'ru': 'Сопоставление экспорта и импорта показывает внутреннюю структуру оборота. Для Китая '
                            'характерны крупные встречные потоки, а для Индии — резкое превышение российского экспорта '
                            'над импортом.',
                      'en': 'Comparing exports and imports shows the internal structure of turnover. China is '
                            'characterized by large two-way flows, while India is characterized by a sharp excess of '
                            'Russian exports over imports.'},
 'stats04_text_018': {'ru': 'Торговое сальдо', 'en': 'Trade Balance'},
 'stats04_text_019': {'ru': 'Сальдо рассчитывается как экспорт минус импорт. Положительное значение означает профицит '
                            'торговли для России. Однако высокий профицит нужно сопоставлять со структурой: он может '
                            'быть следствием сырьевой концентрации, а не широкой диверсификации.',
                      'en': 'The balance is calculated as exports minus imports. A positive value means a trade '
                            'surplus for Russia. However, a high surplus must be compared with the structure: it may '
                            'result from raw-material concentration rather than broad diversification.'},
 'stats04_text_020': {'ru': 'Баланс с Китаем', 'en': 'Balance with China'},
 'stats04_text_021': {'ru': 'В разные годы торговля с Китаем переходила от профицита к дефициту и обратно. Это связано '
                            'с ростом импорта машин, оборудования и электроники, а затем с увеличением российского '
                            'экспорта.',
                      'en': 'In different years, trade with China moved from surplus to deficit and back. This was '
                            'linked to the growth of imports of machinery, equipment and electronics, and later to an '
                            'increase in Russian exports.'},
 'stats04_text_022': {'ru': 'Баланс с Индией', 'en': 'Balance with India'},
 'stats04_text_023': {'ru': 'Сальдо с Индией в последние годы резко выросло и стало одним из самых заметных '
                            'результатов анализа. Его природа — экспортная асимметрия, прежде всего по энергетическому '
                            'сырью.',
                      'en': 'The balance with India has risen sharply in recent years and became one of the most '
                            'notable findings of the analysis. Its nature is export asymmetry, primarily in energy '
                            'commodities.'},
 'stats04_text_024': {'ru': 'Товарная структура', 'en': 'Commodity Structure'},
 'stats04_text_025': {'ru': 'Структурный анализ показывает, какие именно товары формируют торговые потоки. Важно '
                            'различать сырьевые позиции, промышленный импорт, технологические компоненты и нишевые '
                            'товары.',
                      'en': 'Structural analysis shows which goods form trade flows. It is important to distinguish '
                            'raw-material items, industrial imports, technological components and niche goods.'},
 'stats04_text_026': {'ru': 'Справка по компаниям', 'en': 'Company Reference'},
 'stats04_text_027': {'ru': 'Экспорт России', 'en': 'Russian Exports'},
 'stats04_text_028': {'ru': 'В экспорте оценивается, какая часть поставок приходится на сырьевые и полуфабрикатные '
                            'группы. Чем выше доля минерального топлива, тем сильнее зависимость результата от '
                            'энергетической конъюнктуры.',
                      'en': 'The export analysis assesses what share of supplies is accounted for by raw-material and '
                            'semi-finished groups. The higher the share of mineral fuels, the stronger the dependence '
                            'of the result on energy market conditions.'},
 'stats04_text_029': {'ru': 'Россия—Китай', 'en': 'Russia-China'},
 'stats04_text_030': {'ru': 'Россия—Индия', 'en': 'Russia-India'},
 'stats04_text_031': {'ru': 'Китай—Россия', 'en': 'China-Russia'},
 'stats04_text_032': {'ru': 'Индия—Россия', 'en': 'India-Russia'},
 'stats04_text_033': {'ru': 'Россия—Китай, оборот', 'en': 'Russia-China, turnover'},
 'stats04_text_034': {'ru': 'Россия—Индия, оборот', 'en': 'Russia-India, turnover'},
 'stats04_text_035': {'ru': 'РФ—Китай, оборот', 'en': 'Russia-China, turnover'},
 'stats04_text_036': {'ru': 'РФ—Индия, оборот', 'en': 'Russia-India, turnover'},
 'stats04_text_037': {'ru': 'Сальдо РФ—Китай', 'en': 'Russia-China balance'},
 'stats04_text_038': {'ru': 'Сальдо РФ—Индия', 'en': 'Russia-India balance'},
 'stats04_text_039': {'ru': 'Что именно экспортируется в Китай', 'en': 'What Is Exported to China'},
 'stats04_text_040': {'ru': 'Китай: состав экспорта', 'en': 'China: Export Composition'},
 'stats04_text_041': {'ru': 'Структура экспорта в Китай более диверсифицирована, чем в Индию: кроме топлива заметны '
                            'руды, металлы, древесина, рыба, удобрения и другие сырьевые и полуфабрикатные позиции.',
                      'en': 'The export structure to China is more diversified than to India: in addition to fuel, '
                            'ores, metals, timber, fish, fertilizers and other raw-material and semi-finished '
                            'positions are noticeable.'},
 'stats04_text_042': {'ru': 'Подробная таблица состава экспорта в Китай',
                      'en': 'Detailed Table of Export Composition to China'},
 'stats04_text_043': {'ru': 'Что именно экспортируется в Индию', 'en': 'What Is Exported to India'},
 'stats04_text_044': {'ru': 'Индия: состав экспорта', 'en': 'India: Export Composition'},
 'stats04_text_045': {'ru': 'Экспортное направление в Индию заметно более концентрировано: ключевой вклад в него '
                            'вносят минеральное топливо, растительные масла и удобрения.',
                      'en': 'The export direction to India is noticeably more concentrated: mineral fuels, vegetable '
                            'oils and fertilizers make the key contribution.'},
 'stats04_text_046': {'ru': 'Подробная таблица состава экспорта в Индию',
                      'en': 'Detailed Table of Export Composition to India'},
 'stats04_text_047': {'ru': 'Импорт России', 'en': 'Russian Imports'},
 'stats04_text_048': {'ru': 'В импорте важно отделить широкую промышленную зависимость от нишевых поставок. Китай '
                            'поставляет большой набор машин, электроники и транспортных средств, а Индия заметна '
                            'прежде всего по фармацевтике, химии и отдельным промышленным товарам.',
                      'en': 'In imports, it is important to separate broad industrial dependence from niche supplies. '
                            'China supplies a wide range of machinery, electronics and vehicles, while India is '
                            'noticeable primarily in pharmaceuticals, chemicals and selected industrial goods.'},
 'stats04_text_049': {'ru': 'Что именно импортируется из Китая', 'en': 'What Is Imported from China'},
 'stats04_text_050': {'ru': 'Китай: состав импорта', 'en': 'China: Import Composition'},
 'stats04_text_051': {'ru': 'По содержанию это прежде всего машины и оборудование, транспортные средства, электроника, '
                            'пластмассы, химическая продукция и различные потребительские товары.',
                      'en': 'In terms of content, these are primarily machinery and equipment, vehicles, electronics, '
                            'plastics, chemical products and various consumer goods.'},
 'stats04_text_052': {'ru': 'Подробная таблица состава импорта из Китая',
                      'en': 'Detailed Table of Import Composition from China'},
 'stats04_text_053': {'ru': 'Что именно импортируется из Индии', 'en': 'What Is Imported from India'},
 'stats04_text_054': {'ru': 'Индия: состав импорта', 'en': 'India: Import Composition'},
 'stats04_text_055': {'ru': 'Индийские поставки меньше по объему, но важны по отдельным нишам: фармацевтика, химия, '
                            'машины и оборудование, электрооборудование, а также чай и пряности.',
                      'en': 'Indian supplies are smaller in volume, but important in specific niches: pharmaceuticals, '
                            'chemicals, machinery and equipment, electrical equipment, as well as tea and spices.'},
 'stats04_text_056': {'ru': 'Подробная таблица состава импорта из Индии',
                      'en': 'Detailed Table of Import Composition from India'},
 'stats04_text_057': {'ru': 'География экспортных партнеров', 'en': 'Geography of Export Partners'},
 'stats04_text_058': {'ru': 'Сравнение структуры 2000 и 2023 годов показывает перестройку направления российского '
                            'экспорта. Главный сдвиг заключается в снижении роли западных рынков и усилении азиатского '
                            'направления.',
                      'en': 'Comparing the structures of 2000 and 2023 shows a restructuring of Russian export '
                            'destinations. The main shift lies in the declining role of Western markets and the '
                            'strengthening of the Asian direction.'},
 'stats04_text_059': {'ru': 'Ключевой структурный сдвиг', 'en': 'Key Structural Shift'},
 'stats04_text_060': {'ru': 'В 2000 году среди значимых направлений российского экспорта заметную роль играли '
                            'европейские страны и США. К 2023 году центр тяжести сместился к Китаю и Индии, что '
                            'подтверждается как графически, так и расчетом индексов структурных сдвигов.',
                      'en': 'In 2000, European countries and the United States played a visible role among major '
                            'destinations of Russian exports. By 2023, the center of gravity shifted to China and '
                            'India, which is confirmed both visually and by structural shift indices.'},
 'stats04_text_061': {'ru': 'Методологическое уточнение.', 'en': 'Methodological note.'},
 'stats04_text_062': {'ru': 'В данном блоке компании не используются как источник распределения товарооборота.',
                      'en': 'In this block, companies are not used as a source for allocating trade turnover.'},
 'stats04_text_063': {'ru': 'Они приведены для ориентира: в экспорте — как профильные российские производители и '
                            'экспортеры соответствующих групп,',
                      'en': 'They are provided as a reference point: in exports, as relevant Russian producers and '
                            'exporters of the corresponding groups,'},
 'stats04_text_064': {'ru': 'в импорте — как иностранные производители и бренды, продукция которых может быть '
                            'представлена в российских поставках.',
                      'en': 'and in imports, as foreign producers and brands whose products may be represented in '
                            'Russian supplies.'},
 'stats04_text_065': {'ru': 'Для строгого ранжирования по компаниям необходима отдельная таможенная микростатистика по '
                            'участникам ВЭД.',
                      'en': 'Strict ranking by company would require separate customs microstatistics on foreign trade '
                            'participants.'},
 'stats04_text_066': {'ru': 'Зачем блок вынесен отдельно', 'en': 'Why This Block Is Separate'},
 'stats04_text_067': {'ru': 'На защите основное внимание можно оставить на динамике, структуре и коэффициентах. '
                            'Справка по компаниям открывается при необходимости, если возникает вопрос о том, какие '
                            'реальные производители стоят за укрупненными товарными группами.',
                      'en': 'At the defense, the main focus can remain on dynamics, structure and ratios. The company '
                            'reference can be opened if a question arises about which real producers stand behind the '
                            'aggregated commodity groups.'},
 'stats04_text_068': {'ru': 'Российский экспорт', 'en': 'Russian Exports'},
 'stats04_text_069': {'ru': 'Российский импорт', 'en': 'Russian Imports'},
 'stats04_text_070': {'ru': 'Экспорт России в Китай: профильные российские экспортеры',
                      'en': 'Russian Exports to China: Relevant Russian Exporters'},
 'stats04_text_071': {'ru': 'Экспорт России в Индию: профильные российские экспортеры',
                      'en': 'Russian Exports to India: Relevant Russian Exporters'},
 'stats04_text_072': {'ru': 'Импорт России из Китая: иностранные производители и бренды',
                      'en': 'Russian Imports from China: Foreign Producers and Brands'},
 'stats04_text_073': {'ru': 'Импорт России из Индии: иностранные производители и бренды',
                      'en': 'Russian Imports from India: Foreign Producers and Brands'},
 'stats04_text_074': {'ru': 'Таблица-справка по экспортным группам', 'en': 'Reference Table for Export Groups'},
 'stats04_text_075': {'ru': 'Таблица-справка по импортным группам', 'en': 'Reference Table for Import Groups'},
 'stats04_text_076': {'ru': 'Индексы и коэффициенты', 'en': 'Indices and Ratios'},
 'stats04_text_077': {'ru': 'Этот блок переводит наблюдаемые изменения в формальные статистические показатели. Индексы '
                            'Гатева и Салаи измеряют силу структурного сдвига, а коэффициент покрытия отражает '
                            'соотношение экспорта и импорта.',
                      'en': 'This block converts observed changes into formal statistical indicators. The Gatev and '
                            'Salai indices measure the strength of structural shifts, while the coverage ratio '
                            'reflects the ratio of exports to imports.'},
 'stats04_text_078': {'ru': 'Интерпретация:', 'en': 'Interpretation:'},
 'stats04_text_079': {'ru': 'чем ближе индекс к 1, тем сильнее структурный сдвиг. Значения, полученные для внешней '
                            'торговли,',
                      'en': 'the closer the index is to 1, the stronger the structural shift. The values obtained for '
                            'foreign trade'},
 'stats04_text_080': {'ru': 'подтверждают, что изменение географии торговли было существенным, а не только визуально '
                            'заметным.',
                      'en': 'confirm that the change in trade geography was substantial, not merely visually '
                            'noticeable.'},
 'stats04_text_081': {'ru': 'Что фиксируют индексы', 'en': 'What the Indices Capture'},
 'stats04_text_082': {'ru': 'Высокие значения индексов показывают сильную перестройку географии торговли. В экспорте '
                            'это связано с ростом роли Китая и Индии, а в импорте — прежде всего с усилением '
                            'китайского направления как основного источника поставок.',
                      'en': 'High index values indicate a strong restructuring of trade geography. In exports, this is '
                            'associated with the growing role of China and India; in imports, primarily with the '
                            'strengthening of the China direction as the main source of supplies.'},
 'stats04_text_083': {'ru': 'Коэффициент покрытия', 'en': 'Coverage Ratio'},
 'stats04_text_084': {'ru': 'Коэффициент покрытия равен отношению экспорта к импорту. Значение выше 1 означает, что '
                            'экспорт превышает импорт; значение ниже 1 — импорт превышает экспорт. Для удобства на '
                            'графике проведена линия равновесия.',
                      'en': 'The coverage ratio equals exports divided by imports. A value above 1 means exports '
                            'exceed imports; a value below 1 means imports exceed exports. For clarity, an equilibrium '
                            'line is shown on the chart.'},
 'stats04_text_085': {'ru': 'В 2023 году коэффициент покрытия составил', 'en': 'In 2023, the coverage ratio was'},
 'stats04_text_086': {'ru': 'Экспорт превышал импорт, но соотношение оставалось относительно близким к равновесию.',
                      'en': 'Exports exceeded imports, but the ratio remained relatively close to equilibrium.'},
 'stats04_text_087': {'ru': 'Значение отражает экстремальное превышение российского экспорта над импортом из Индии.',
                      'en': 'The value reflects an extreme excess of Russian exports over imports from India.'},
 'stats04_text_088': {'ru': 'Исходные таблицы', 'en': 'Source Tables'},
 'stats04_text_089': {'ru': 'Этот раздел оставлен для проверки числовой базы графиков. Здесь можно посмотреть ряды, из '
                            'которых построены визуализации: оборот, экспорт, импорт, сальдо и коэффициент покрытия.',
                      'en': 'This section is left for checking the numerical base of the charts. Here one can view the '
                            'series used to build the visualizations: turnover, exports, imports, balance and coverage '
                            'ratio.'},
 'stats04_text_090': {'ru': 'Единицы измерения', 'en': 'Units of Measurement'},
 'stats04_text_091': {'ru': 'В исходных рядах денежные показатели хранятся в базовых единицах датасета, а на графиках '
                            'приводятся к млрд долларов США для удобства чтения. Коэффициент покрытия является '
                            'безразмерным отношением.',
                      'en': 'In the source series, monetary indicators are stored in the base units of the dataset, '
                            'while charts present them in USD billions for easier reading. The coverage ratio is a '
                            'dimensionless ratio.'},
 'stats04_text_092': {'ru': 'Год', 'en': 'Year'},
 'stats04_text_093': {'ru': 'Оборот', 'en': 'Turnover'},
 'stats04_text_094': {'ru': 'Экспорт', 'en': 'Export'},
 'stats04_text_095': {'ru': 'Импорт', 'en': 'Import'},
 'stats04_text_096': {'ru': 'Сальдо', 'en': 'Balance'},
 'stats04_text_097': {'ru': 'Стоимость', 'en': 'Value'},
 'stats04_text_098': {'ru': 'Доля', 'en': 'Share'},
 'stats04_text_099': {'ru': 'Товарная группа', 'en': 'Commodity group'},
 'stats04_text_100': {'ru': 'Что входит в группу', 'en': 'What the group includes'},
 'stats04_text_101': {'ru': 'Примеры продукции', 'en': 'Product examples'},
 'stats04_text_102': {'ru': 'Компании', 'en': 'Companies'},
 'stats04_text_103': {'ru': 'Где используется', 'en': 'Where it is used'},
 'stats04_text_104': {'ru': 'Типичная продукция', 'en': 'Typical products'},
 'stats04_text_105': {'ru': 'Профильные российские производители и экспортеры',
                      'en': 'Relevant Russian producers and exporters'},
 'stats04_text_106': {'ru': 'Иностранные производители и бренды', 'en': 'Foreign producers and brands'},
 'stats04_text_107': {'ru': 'Направление', 'en': 'Direction'},
 'stats04_text_108': {'ru': 'Страна', 'en': 'Country'},
 'stats04_text_109': {'ru': 'Индекс Гатева', 'en': 'Gatev Index'},
 'stats04_text_110': {'ru': 'Индекс Салаи', 'en': 'Salai Index'},
 'stats04_text_111': {'ru': 'значение индекса', 'en': 'index value'},
 'stats04_text_112': {'ru': 'доля, %', 'en': 'share, %'},
 'stats04_text_113': {'ru': 'доля лидера', 'en': 'leader share'},
 'stats04_text_114': {'ru': 'ключевая группа', 'en': 'key group'},
 'stats04_text_115': {'ru': 'экспорт = импорт', 'en': 'exports = imports'},
 'stats04_text_116': {'ru': 'коэффициент покрытия, раз', 'en': 'coverage ratio, times'},
 'stats04_text_117': {'ru': 'коэффициент покрытия', 'en': 'coverage ratio'},
 'stats04_text_118': {'ru': 'экспорт / импорт', 'en': 'exports / imports'},
 'stats04_text_119': {'ru': 'граница баланса = 1', 'en': 'balance threshold = 1'},
 'stats04_text_120': {'ru': 'дополнительная ось торгового треугольника', 'en': 'additional axis of the trade triangle'},
 'stats04_text_121': {'ru': 'экспорт', 'en': 'export'},
 'stats04_text_122': {'ru': 'импорт', 'en': 'import'},
 'stats04_text_123': {'ru': 'сальдо', 'en': 'balance'},
 'stats04_text_124': {'ru': 'оборот', 'en': 'turnover'},
 'stats04_text_125': {'ru': 'год; рост к началу периода —', 'en': 'year; growth since the beginning of the period —'},
 'stats04_text_126': {'ru': 'рост к началу периода', 'en': 'growth since the beginning of the period'},
 'stats04_text_127': {'ru': 'Экспорт:', 'en': 'Export:'},
 'stats04_text_128': {'ru': '; импорт:', 'en': '; import:'},
 'stats04_text_129': {'ru': 'экспорт ', 'en': 'export '},
 'stats04_text_130': {'ru': 'или', 'en': 'or'},
 'stats04_text_131': {'ru': 'от показанного состава', 'en': 'of the displayed structure'},
 'stats04_text_132': {'ru': 'в показанной структуре', 'en': 'in the displayed structure'},
 'stats04_text_133': {'ru': 'В группу входят:', 'en': 'The group includes:'},
 'stats04_text_134': {'ru': 'Три крупнейшие группы:', 'en': 'The three largest groups:'},
 'stats04_text_135': {'ru': 'млрд долларов США', 'en': 'USD billion'},
 'stats04_text_136': {'ru': 'млрд $', 'en': 'USD bn'},
 'stats04_text_137': {'ru': 'млрд', 'en': 'bn'},
 'stats04_text_138': {'ru': 'раза', 'en': 'times'},
 'stats04_text_139': {'ru': 'в ', 'en': 'x'},
 'stats04_text_140': {'ru': 'сырая нефть и нефтепродукты, природный газ, уголь и иные виды минерального топлива',
                      'en': 'crude oil and petroleum products, natural gas, coal and other mineral fuels'},
 'stats04_text_141': {'ru': 'нефть марок Urals и ESPO, нефтепродукты, уголь, природный газ',
                      'en': 'Urals and ESPO crude oil, petroleum products, coal and natural gas'},
 'stats04_text_142': {'ru': 'станки, промышленное оборудование, насосы, компрессоры, двигатели, комплектующие и '
                            'механические устройства',
                      'en': 'machine tools, industrial equipment, pumps, compressors, engines, components and '
                            'mechanical devices'},
 'stats04_text_143': {'ru': 'станки, насосы, компрессоры, строительная и промышленная техника, комплектующие',
                      'en': 'machine tools, pumps, compressors, construction and industrial machinery, components'},
 'stats04_text_144': {'ru': 'электроника, кабели, аккумуляторы, электрические машины, компоненты связи и бытовая '
                            'техника',
                      'en': 'electronics, cables, batteries, electrical machinery, communication components and '
                            'household appliances'},
 'stats04_text_145': {'ru': 'кабели, аккумуляторы, бытовая техника, компоненты связи, смартфоны, компьютеры',
                      'en': 'cables, batteries, household appliances, communication components, smartphones and '
                            'computers'},
 'stats04_text_146': {'ru': 'автомобили, грузовой транспорт, автокомпоненты, спецтехника и части транспортных средств',
                      'en': 'cars, freight vehicles, auto components, special-purpose machinery and vehicle parts'},
 'stats04_text_147': {'ru': 'легковые автомобили, грузовики, автобусы, спецтехника, автокомпоненты',
                      'en': 'passenger cars, trucks, buses, special-purpose vehicles and auto components'},
 'stats04_text_148': {'ru': 'лекарственные средства, субстанции, медицинские препараты и фармацевтическая продукция',
                      'en': 'medicines, active substances, medical preparations and pharmaceutical products'},
 'stats04_text_149': {'ru': 'дженерики, субстанции, антибиотики, кардиологические и противовирусные препараты',
                      'en': 'generics, active substances, antibiotics, cardiovascular and antiviral medicines'},
 'stats04_text_150': {'ru': 'калийные, азотные и смешанные минеральные удобрения',
                      'en': 'potash, nitrogen and mixed mineral fertilizers'},
 'stats04_text_151': {'ru': 'калийные, азотные, фосфорные и комплексные минеральные удобрения',
                      'en': 'potash, nitrogen, phosphate and compound mineral fertilizers'},
 'stats04_text_152': {'ru': 'растительные масла, прежде всего подсолнечное и иные масложировые товары',
                      'en': 'vegetable oils, primarily sunflower oil, and other oil-and-fat products'},
 'stats04_text_153': {'ru': 'подсолнечное масло, соевое масло, рапсовое масло, масложировое сырье',
                      'en': 'sunflower oil, soybean oil, rapeseed oil and oil-and-fat raw materials'},
 'stats04_text_154': {'ru': 'железные и цветные руды, концентраты, шлаки и зола',
                      'en': 'ferrous and non-ferrous ores, concentrates, slag and ash'},
 'stats04_text_155': {'ru': 'железорудный концентрат, медные и никелевые руды, шлаки и зола',
                      'en': 'iron ore concentrate, copper and nickel ores, slag and ash'},
 'stats04_text_156': {'ru': 'алюминий необработанный, полуфабрикаты и изделия из алюминия',
                      'en': 'unwrought aluminum, semi-finished products and aluminum goods'},
 'stats04_text_157': {'ru': 'первичный алюминий, алюминиевые сплавы, прокат и полуфабрикаты',
                      'en': 'primary aluminum, aluminum alloys, rolled products and semi-finished products'},
 'stats04_text_158': {'ru': 'рафинированная медь, медные сплавы, полуфабрикаты и изделия из меди',
                      'en': 'refined copper, copper alloys, semi-finished products and copper goods'},
 'stats04_text_159': {'ru': 'рафинированная медь, медная катанка, сплавы и полуфабрикаты',
                      'en': 'refined copper, copper rod, alloys and semi-finished products'},
 'stats04_text_160': {'ru': 'лесоматериалы, пиломатериалы, древесина и продукция первичной обработки',
                      'en': 'timber, sawn wood, wood and primary processed products'},
 'stats04_text_161': {'ru': 'пиломатериалы, фанера, целлюлозное сырье, продукция первичной обработки древесины',
                      'en': 'sawn wood, plywood, pulp raw materials and primary processed wood products'},
 'stats04_text_162': {'ru': 'рыба, ракообразные, морепродукты и замороженная рыбная продукция',
                      'en': 'fish, crustaceans, seafood and frozen fish products'},
 'stats04_text_163': {'ru': 'минтай, краб, лососевые, морепродукты, замороженная рыбная продукция',
                      'en': 'pollock, crab, salmonids, seafood and frozen fish products'},
 'stats04_text_164': {'ru': 'целлюлоза, бумажная масса, бумага и картон',
                      'en': 'pulp, paper pulp, paper and cardboard'},
 'stats04_text_165': {'ru': 'целлюлоза, бумажная масса, бумага, картон, упаковочные материалы',
                      'en': 'pulp, paper pulp, paper, cardboard and packaging materials'},
 'stats04_text_166': {'ru': 'каучук, резина, шины, изделия из резины и полимерные материалы',
                      'en': 'rubber, tires, rubber goods and polymer materials'},
 'stats04_text_167': {'ru': 'синтетический каучук, резинотехнические изделия, шины и полимерные материалы',
                      'en': 'synthetic rubber, rubber technical goods, tires and polymer materials'},
 'stats04_text_168': {'ru': 'пластмассы, полимерные материалы, упаковочные материалы и изделия из пластика',
                      'en': 'plastics, polymer materials, packaging materials and plastic goods'},
 'stats04_text_169': {'ru': 'полимеры, пленки, упаковка, изделия из пластмасс, комплектующие',
                      'en': 'polymers, films, packaging, plastic goods and components'},
 'stats04_text_170': {'ru': 'органическая и неорганическая химия, реактивы, химические полуфабрикаты',
                      'en': 'organic and inorganic chemicals, reagents and chemical semi-finished products'},
 'stats04_text_171': {'ru': 'органическая и неорганическая химия, реактивы, промежуточные продукты, красители',
                      'en': 'organic and inorganic chemicals, reagents, intermediates and dyes'},
 'stats04_text_172': {'ru': 'изделия из черных и цветных металлов, металлоконструкции и полуфабрикаты',
                      'en': 'ferrous and non-ferrous metal products, metal structures and semi-finished products'},
 'stats04_text_173': {'ru': 'металлоконструкции, крепеж, прокат, полуфабрикаты и изделия из черных и цветных металлов',
                      'en': 'metal structures, fasteners, rolled products, semi-finished products and ferrous and '
                            'non-ferrous metal goods'},
 'stats04_text_174': {'ru': 'обувь, элементы обуви и потребительские товары легкой промышленности',
                      'en': 'footwear, footwear components and light-industry consumer goods'},
 'stats04_text_175': {'ru': 'спортивная, повседневная и специальная обувь, подошвы, элементы обуви',
                      'en': 'sports, casual and special-purpose footwear, soles and footwear components'},
 'stats04_text_176': {'ru': 'текстиль, одежда, трикотаж и готовые изделия легкой промышленности',
                      'en': 'textiles, clothing, knitwear and finished light-industry goods'},
 'stats04_text_177': {'ru': 'трикотаж, верхняя одежда, текстильные изделия, готовая одежда',
                      'en': 'knitwear, outerwear, textile products and ready-made clothing'},
 'stats04_text_178': {'ru': 'игрушки, спортивные товары, инвентарь и отдельные потребительские товары',
                      'en': 'toys, sporting goods, equipment and selected consumer goods'},
 'stats04_text_179': {'ru': 'игрушки, спортивный инвентарь, настольные игры, товары для досуга',
                      'en': 'toys, sports equipment, board games and leisure goods'},
 'stats04_text_180': {'ru': 'мебель, осветительные приборы, интерьерные товары и бытовые изделия',
                      'en': 'furniture, lighting fixtures, interior goods and household items'},
 'stats04_text_181': {'ru': 'корпусная мебель, офисная мебель, светильники, интерьерные изделия',
                      'en': 'cabinet furniture, office furniture, lighting fixtures and interior goods'},
 'stats04_text_182': {'ru': 'керамические изделия, плитка, санитарная керамика и огнеупорные материалы',
                      'en': 'ceramic products, tiles, sanitary ceramics and refractory materials'},
 'stats04_text_183': {'ru': 'плитка, санитарная керамика, огнеупорные изделия, техническая керамика',
                      'en': 'tiles, sanitary ceramics, refractory goods and technical ceramics'},
 'stats04_text_184': {'ru': 'чай, пряности, кофе и отдельные продовольственные товары',
                      'en': 'tea, spices, coffee and selected food products'},
 'stats04_text_185': {'ru': 'ассамский чай, дарджилинг, черный чай, пряности, перец, кардамон',
                      'en': 'Assam tea, Darjeeling, black tea, spices, pepper and cardamom'},
 'stats04_text_186': {'ru': 'перец, кардамон, куркума, кориандр, смеси специй',
                      'en': 'pepper, cardamom, turmeric, coriander and spice blends'},
 'stats04_text_187': {'ru': 'драгоценные камни, металлы и отдельные товары ювелирной группы',
                      'en': 'precious stones, metals and selected jewelry-group goods'},
 'stats04_text_188': {'ru': 'алмазы, бриллианты, драгоценные камни, ювелирное сырье',
                      'en': 'diamonds, polished diamonds, precious stones and jewelry raw materials'},
 'stats04_text_189': {'ru': 'товары соответствующей укрупненной группы внешнеторговой классификации',
                      'en': 'goods of the corresponding aggregated foreign trade classification group'},
 'stats04_text_190': {'ru': 'разнородные товары, не вошедшие в основные укрупненные группы',
                      'en': 'heterogeneous goods not included in the main aggregated groups'},
 'stats04_text_191': {'ru': 'без выделения конкретной компании из-за смешанного состава категории',
                      'en': 'without identifying a specific company due to the mixed composition of the category'},
 'stats04_text_192': {'ru': 'зависит от конкретных товарных кодов внутри группы',
                      'en': 'depends on the specific commodity codes within the group'},
 'stats04_text_193': {'ru': 'конкретные компании зависят от детального товарного кода и источника поставки',
                      'en': 'specific companies depend on the detailed commodity code and source of supply'},
 'stats04_text_194': {'ru': 'применение зависит от состава укрупненной товарной группы',
                      'en': 'the use depends on the composition of the aggregated commodity group'},
 'stats04_text_195': {'ru': 'точное распределение по российским экспортерам требует детализации по компаниям и '
                            'товарным кодам',
                      'en': 'precise allocation by Russian exporters requires company-level and commodity-code detail'},
 'stats04_text_196': {'ru': 'конкретные иностранные производители зависят от детального товарного кода, поставщика и '
                            'канала ввоза',
                      'en': 'specific foreign producers depend on the detailed commodity code, supplier and import '
                            'channel'},
 'stats04_text_197': {'ru': 'переработка на НПЗ, производство топлива, нефтехимия, энергетика',
                      'en': 'oil refining, fuel production, petrochemicals and energy'},
 'stats04_text_198': {'ru': 'строительство, промышленное производство, добыча, транспортная и складская инфраструктура',
                      'en': 'construction, industrial production, mining, transport and warehouse infrastructure'},
 'stats04_text_199': {'ru': 'потребительский рынок, связь, ИТ-инфраструктура, промышленная автоматизация',
                      'en': 'consumer market, communications, IT infrastructure and industrial automation'},
 'stats04_text_200': {'ru': 'личный транспорт, логистика, строительные работы, перевозки и автосервис',
                      'en': 'personal transport, logistics, construction works, transportation and auto services'},
 'stats04_text_201': {'ru': 'здравоохранение, аптечный рынок, больничные закупки, производство лекарств',
                      'en': 'healthcare, pharmacy market, hospital procurement and medicine production'},
 'stats04_text_202': {'ru': 'сельское хозяйство, повышение урожайности зерновых, масличных и технических культур',
                      'en': 'agriculture, increasing yields of grain, oilseed and industrial crops'},
 'stats04_text_203': {'ru': 'пищевая промышленность, производство готовых продуктов, розничный продовольственный рынок',
                      'en': 'food industry, production of finished foods and retail food market'},
 'stats04_text_204': {'ru': 'черная и цветная металлургия, производство стали, сплавов и промышленных материалов',
                      'en': 'ferrous and non-ferrous metallurgy, steel, alloys and industrial materials production'},
 'stats04_text_205': {'ru': 'автомобилестроение, строительство, упаковка, энергетика, производство кабелей',
                      'en': 'automotive industry, construction, packaging, energy and cable production'},
 'stats04_text_206': {'ru': 'электротехника, кабельная продукция, электроника, машиностроение',
                      'en': 'electrical engineering, cable products, electronics and mechanical engineering'},
 'stats04_text_207': {'ru': 'строительство, мебельное производство, упаковка, бумажная промышленность',
                      'en': 'construction, furniture production, packaging and paper industry'},
 'stats04_text_208': {'ru': 'пищевая промышленность, переработка, розничная торговля, общественное питание',
                      'en': 'food industry, processing, retail trade and food service'},
 'stats04_text_209': {'ru': 'бумажная промышленность, упаковка, санитарно-гигиенические изделия',
                      'en': 'paper industry, packaging and sanitary-hygiene products'},
 'stats04_text_210': {'ru': 'автопром, шинная промышленность, строительство, промышленная резина',
                      'en': 'automotive industry, tire industry, construction and industrial rubber'},
 'stats04_text_211': {'ru': 'упаковка, бытовые товары, автокомпоненты, строительные материалы',
                      'en': 'packaging, household goods, auto components and construction materials'},
 'stats04_text_212': {'ru': 'фармацевтика, сельское хозяйство, производство пластмасс, лакокрасочная промышленность',
                      'en': 'pharmaceuticals, agriculture, plastics production and paint-and-coatings industry'},
 'stats04_text_213': {'ru': 'строительство, машиностроение, инфраструктурные проекты, промышленное оборудование',
                      'en': 'construction, mechanical engineering, infrastructure projects and industrial equipment'},
 'stats04_text_214': {'ru': 'розничная торговля, спорт, повседневное потребление, рабочая экипировка',
                      'en': 'retail trade, sports, everyday consumption and workwear'},
 'stats04_text_215': {'ru': 'розничная торговля, массовый потребительский рынок, спортивная одежда',
                      'en': 'retail trade, mass consumer market and sportswear'},
 'stats04_text_216': {'ru': 'детские товары, спорт, досуг, розничная торговля',
                      'en': 'children’s goods, sports, leisure and retail trade'},
 'stats04_text_217': {'ru': 'домохозяйства, офисы, гостиницы, торговые помещения',
                      'en': 'households, offices, hotels and retail premises'},
 'stats04_text_218': {'ru': 'строительство, ремонт, отделочные работы, промышленная теплоизоляция',
                      'en': 'construction, repair, finishing works and industrial thermal insulation'},
 'stats04_text_219': {'ru': 'розничная торговля, общественное питание, пищевая промышленность',
                      'en': 'retail trade, food service and food industry'},
 'stats04_text_220': {'ru': 'пищевая промышленность, розничная торговля, общественное питание',
                      'en': 'food industry, retail trade and food service'},
 'stats04_text_221': {'ru': 'огранка, ювелирное производство, инвестиционные и промышленные применения',
                      'en': 'cutting, jewelry production, investment and industrial applications'},
 'stats04_text_222': {'ru': ' — как ориентиры по отрасли', 'en': ' — as industry reference points'},
 'stats04_text_223': {'ru': ' — примеры компаний по группе', 'en': ' — examples of companies in the group'},
 'stats04_text_224': {'ru': ' — примеры брендов по группе', 'en': ' — examples of brands in the group'},
 'stats04_text_225': {'ru': ' — примеры индийских фармкомпаний',
                      'en': ' — examples of Indian pharmaceutical companies'},
 'stats04_text_226': {'ru': ' — примеры российских производителей', 'en': ' — examples of Russian producers'},
 'stats04_text_227': {'ru': ' — примеры компаний масложирового сектора',
                      'en': ' — examples of companies in the oil-and-fat sector'},
 'stats04_text_228': {'ru': ' — примеры компаний сырьевого и металлургического контура',
                      'en': ' — examples of companies in the raw-material and metallurgical segments'},
 'stats04_text_229': {'ru': ' — основной российский ориентир по алюминиевой продукции',
                      'en': ' — the main Russian reference point for aluminum products'},
 'stats04_text_230': {'ru': ' — примеры компаний медного и цветного металлургического сектора',
                      'en': ' — examples of companies in the copper and non-ferrous metallurgy sector'},
 'stats04_text_231': {'ru': ' — примеры российских компаний лесопромышленного комплекса',
                      'en': ' — examples of Russian timber-industry companies'},
 'stats04_text_232': {'ru': ' — примеры отраслевых компаний', 'en': ' — examples of industry companies'},
 'stats04_text_233': {'ru': ' — примеры производителей отрасли', 'en': ' — examples of industry producers'},
 'stats04_text_234': {'ru': ' — примеры компаний и брендов по группе',
                      'en': ' — examples of companies and brands in the group'},
 'stats04_text_235': {'ru': ' — примеры китайских химических компаний',
                      'en': ' — examples of Chinese chemical companies'},
 'stats04_text_236': {'ru': ' — примеры компаний металлургического сектора',
                      'en': ' — examples of metallurgical companies'},
 'stats04_text_237': {'ru': ' — примеры китайских брендов потребительского сегмента',
                      'en': ' — examples of Chinese consumer-segment brands'},
 'stats04_text_238': {'ru': ' — примеры китайских брендов легкой промышленности',
                      'en': ' — examples of Chinese light-industry brands'},
 'stats04_text_239': {'ru': ' — примеры китайских производителей мебели',
                      'en': ' — examples of Chinese furniture producers'},
 'stats04_text_240': {'ru': ' — примеры индийских производителей керамики',
                      'en': ' — examples of Indian ceramic producers'},
 'stats04_text_241': {'ru': ' — примеры индийских чайных брендов', 'en': ' — examples of Indian tea brands'},
 'stats04_text_242': {'ru': ' — примеры индийских брендов специй', 'en': ' — examples of Indian spice brands'},
 'stats04_text_243': {'ru': ' — основной российский ориентир по алмазной отрасли',
                      'en': ' — the main Russian reference point for the diamond industry'},
 'stats04_text_244': {'ru': ' — профильные российские производители и экспортеры топливно-энергетического сектора',
                      'en': ' — relevant Russian producers and exporters in the fuel and energy sector'},
 'stats04_text_245': {'ru': ' — крупные российские производители и экспортеры минеральных удобрений',
                      'en': ' — major Russian producers and exporters of mineral fertilizers'},
 'stats04_text_246': {'ru': ' — профильные российские компании масложирового сектора',
                      'en': ' — relevant Russian companies in the oil-and-fat sector'},
 'stats04_text_247': {'ru': ' — ключевой российский производитель алюминия и алюминиевой продукции',
                      'en': ' — a key Russian producer of aluminum and aluminum products'},
 'stats04_text_248': {'ru': ' — профильные российские компании цветной металлургии',
                      'en': ' — relevant Russian non-ferrous metallurgy companies'},
 'stats04_text_249': {'ru': ' — крупные российские компании лесопромышленного комплекса',
                      'en': ' — major Russian timber-industry companies'},
 'stats04_text_250': {'ru': ' — профильные компании рыбопромышленного сектора',
                      'en': ' — relevant companies in the fishery sector'},
 'stats04_text_251': {'ru': ' — профильные российские производители целлюлозно-бумажной продукции',
                      'en': ' — relevant Russian producers of pulp and paper products'},
 'stats04_text_252': {'ru': ' — ключевой российский ориентир по алмазной отрасли',
                      'en': ' — a key Russian reference point in the diamond industry'},
 'stats04_text_253': {'ru': ' — профильные российские производители машиностроительного контура',
                      'en': ' — relevant Russian producers in mechanical engineering'},
 'stats04_text_254': {'ru': ' — профильные российские производители химической продукции',
                      'en': ' — relevant Russian producers of chemical products'},
 'stats04_text_255': {'ru': ' — крупные российские компании металлургического сектора',
                      'en': ' — major Russian metallurgical companies'},
 'stats04_text_256': {'ru': 'Российские производители электротехнической и кабельной продукции; конкретный состав '
                            'зависит от товарных кодов',
                      'en': 'Russian producers of electrical and cable products; the specific composition depends on '
                            'commodity codes'},
 'stats04_text_257': {'ru': ' — крупные китайские производители строительной, промышленной и двигательной техники',
                      'en': ' — major Chinese producers of construction, industrial and engine equipment'},
 'stats04_text_258': {'ru': ' — китайские производители электроники, бытовой техники и компонентов',
                      'en': ' — Chinese producers of electronics, home appliances and components'},
 'stats04_text_259': {'ru': ' — китайские автомобильные бренды, активно представленные на российском рынке',
                      'en': ' — Chinese automotive brands actively represented in the Russian market'},
 'stats04_text_260': {'ru': ' — китайские производители химической и полимерной продукции',
                      'en': ' — Chinese producers of chemical and polymer products'},
 'stats04_text_261': {'ru': ' — крупные китайские химические компании', 'en': ' — major Chinese chemical companies'},
 'stats04_text_262': {'ru': ' — китайские производители каучука, шин и резинотехнической продукции',
                      'en': ' — Chinese producers of rubber, tires and rubber technical goods'},
 'stats04_text_263': {'ru': ' — крупные китайские металлургические компании',
                      'en': ' — major Chinese metallurgical companies'},
 'stats04_text_264': {'ru': ' — китайские производители мебели и интерьерных товаров',
                      'en': ' — Chinese producers of furniture and interior goods'},
 'stats04_text_265': {'ru': ' — крупные индийские фармацевтические производители',
                      'en': ' — major Indian pharmaceutical producers'},
 'stats04_text_266': {'ru': ' — индийские производители оборудования, компонентов и техники',
                      'en': ' — Indian producers of equipment, components and machinery'},
 'stats04_text_267': {'ru': ' — индийские производители электротехнической продукции и оборудования',
                      'en': ' — Indian producers of electrical products and equipment'},
 'stats04_text_268': {'ru': ' — индийские компании химического и фармацевтического контура',
                      'en': ' — Indian companies in the chemical and pharmaceutical segments'},
 'stats04_text_269': {'ru': ' — индийские производители керамической продукции',
                      'en': ' — Indian producers of ceramic products'},
 'stats04_text_270': {'ru': ' — индийские чайные бренды', 'en': ' — Indian tea brands'},
 'stats04_text_271': {'ru': ' — индийские бренды специй и продовольственных товаров',
                      'en': ' — Indian brands of spices and food products'},
 'stats04_text_272': {'ru': ' — крупные индийские металлургические компании',
                      'en': ' — major Indian metallurgical companies'},
 'stats04_text_273': {'ru': 'Lego производится глобально, а в китайском сегменте заметны Sembo и Mould King как '
                            'примеры категории',
                      'en': 'Lego is produced globally, while Sembo and Mould King are visible examples in the Chinese '
                            'segment of the category'},
 'stats04_text_274': {'ru': 'Sembo, Mould King и другие производители потребительских товаров; категория неоднородна',
                      'en': 'Sembo, Mould King and other consumer goods producers; the category is heterogeneous'},
 'stats04_text_275': {'ru': 'Китай', 'en': 'China'},
 'stats04_text_276': {'ru': 'Индия', 'en': 'India'},
 'stats04_text_277': {'ru': 'Россия', 'en': 'Russia'},
 'stats04_text_278': {'ru': 'РФ', 'en': 'Russia'},
 'stats04_page_title': {'ru': 'Статистический анализ внешней торговли', 'en': 'Statistical Analysis of Foreign Trade'},
 'stats04_tab_company_ref': {'ru': 'Справка по компаниям', 'en': 'Company Reference'},
 'stats04_raw_ru_cn_turnover': {'ru': 'Россия-Китай · оборот', 'en': 'Russia-China · turnover'},
 'stats04_raw_ru_in_turnover': {'ru': 'Россия-Индия · оборот', 'en': 'Russia-India · turnover'},
 'stats04_raw_cn_in_turnover': {'ru': 'Китай-Индия · оборот', 'en': 'China-India · turnover'}})


def _stats04_translate_string(value: str, lang: str | None = None) -> str:
    """Translate visible UI text by exact and safe phrase replacement.

    This helper is intended for Streamlit/Plotly labels, Markdown and HTML blocks.
    It is not applied to source dataframes unless a page explicitly calls it.
    """
    target = _normalize_lang(lang or get_current_lang())
    if target != "en" or not isinstance(value, str) or not value:
        return value

    # Exact match first.
    if value in _STATS04_TEXT_TRANSLATIONS:
        return _STATS04_TEXT_TRANSLATIONS[value]

    result = value
    # Longer phrases first to avoid partial replacements breaking sentences.
    for ru, en in sorted(_STATS04_TEXT_TRANSLATIONS.items(), key=lambda item: len(item[0]), reverse=True):
        if ru in result:
            result = result.replace(ru, en)
    return result


def translate_text(value, lang: str | None = None):
    """Translate a UI string safely.

    Keeps non-string values unchanged. In English mode, first checks LOCALES exact
    entries, then the page-04 phrase dictionary. Dataframe source values are not
    changed unless a page deliberately passes them here for display.
    """
    if not isinstance(value, str):
        return value
    target = _normalize_lang(lang or get_current_lang())
    if target != "en" or not value:
        return value

    for entry in LOCALES.values():
        ru = entry.get("ru") if isinstance(entry, dict) else None
        en = entry.get("en") if isinstance(entry, dict) else None
        if value == ru and en:
            return en
    return _stats04_translate_string(value, target)


def _translate_plotly_figure(fig, lang: str | None = None):
    """Translate Plotly labels/hover/annotations in-place and return the figure."""
    try:
        target = _normalize_lang(lang or get_current_lang())
        if target != "en" or fig is None:
            return fig
        # Layout titles and axis titles.
        try:
            if getattr(fig.layout, "title", None) and getattr(fig.layout.title, "text", None):
                fig.layout.title.text = translate_text(fig.layout.title.text, target)
        except Exception:
            pass
        for axis_name in (
            "xaxis", "yaxis", "xaxis2", "yaxis2", "xaxis3", "yaxis3", "xaxis4", "yaxis4",
            "xaxis5", "yaxis5", "xaxis6", "yaxis6",
        ):
            try:
                axis = getattr(fig.layout, axis_name, None)
                if axis is not None and getattr(axis, "title", None) and getattr(axis.title, "text", None):
                    axis.title.text = translate_text(axis.title.text, target)
            except Exception:
                pass
        # Subplot/regular annotations.
        try:
            for ann in list(getattr(fig.layout, "annotations", []) or []):
                if getattr(ann, "text", None):
                    ann.text = translate_text(ann.text, target)
        except Exception:
            pass
        # Traces: names, hover templates, text arrays.
        try:
            for trace in fig.data:
                if getattr(trace, "name", None):
                    trace.name = translate_text(trace.name, target)
                if getattr(trace, "hovertemplate", None):
                    trace.hovertemplate = translate_text(trace.hovertemplate, target)
                if getattr(trace, "hovertext", None) is not None:
                    ht = trace.hovertext
                    if isinstance(ht, (list, tuple)):
                        trace.hovertext = [translate_text(str(x), target) for x in ht]
                    elif isinstance(ht, str):
                        trace.hovertext = translate_text(ht, target)
                if getattr(trace, "text", None) is not None:
                    txt = trace.text
                    if isinstance(txt, (list, tuple)):
                        trace.text = [translate_text(str(x), target) for x in txt]
                    elif isinstance(txt, str):
                        trace.text = translate_text(txt, target)
        except Exception:
            pass
    except Exception:
        return fig
    return fig


def _translate_options(options, lang: str | None = None):
    try:
        return [translate_text(x, lang) if isinstance(x, str) else x for x in options]
    except Exception:
        return options


def install_streamlit_i18n(st_module=None) -> None:
    """Install lightweight Streamlit UI translation wrappers.

    Wrapped elements: markdown/HTML text, common text widgets, tabs, expanders,
    radio/selectbox/multiselect labels/options/help, and Plotly figure labels.
    The wrappers do not alter dataframe source objects or calculation logic.
    """
    try:
        import streamlit as st
    except Exception:
        return
    st = st_module or st
    if getattr(st, "_diploma_i18n_stats04_patch_installed", False):
        return

    def _wrap_text_fn(name):
        original = getattr(st, name, None)
        if original is None:
            return
        setattr(st, f"_orig_stats04_{name}", original)
        def wrapped(body=None, *args, **kwargs):
            return original(translate_text(body), *args, **kwargs)
        setattr(st, name, wrapped)

    for fn in ("markdown", "info", "warning", "error", "success", "caption", "title", "header", "subheader", "write"):
        _wrap_text_fn(fn)

    if hasattr(st, "button"):
        original_button = st.button
        st._orig_stats04_button = original_button
        def button(label, *args, **kwargs):
            if "help" in kwargs:
                kwargs["help"] = translate_text(kwargs["help"])
            return original_button(translate_text(label), *args, **kwargs)
        st.button = button

    if hasattr(st, "tabs"):
        original_tabs = st.tabs
        st._orig_stats04_tabs = original_tabs
        def tabs(labels, *args, **kwargs):
            return original_tabs(_translate_options(labels), *args, **kwargs)
        st.tabs = tabs

    if hasattr(st, "expander"):
        original_expander = st.expander
        st._orig_stats04_expander = original_expander
        def expander(label, *args, **kwargs):
            return original_expander(translate_text(label), *args, **kwargs)
        st.expander = expander

    for widget_name in ("radio", "selectbox", "multiselect"):
        original = getattr(st, widget_name, None)
        if original is None:
            continue
        setattr(st, f"_orig_stats04_{widget_name}", original)
        def _make_widget_wrapper(original_func):
            def widget(label, options, *args, **kwargs):
                # Translate only displayed labels/options. If page logic needs stable IDs,
                # it should use format_func or an explicit mapping.
                translated_options = _translate_options(options)
                if "help" in kwargs:
                    kwargs["help"] = translate_text(kwargs["help"])
                return original_func(translate_text(label), translated_options, *args, **kwargs)
            return widget
        setattr(st, widget_name, _make_widget_wrapper(original))

    if hasattr(st, "plotly_chart"):
        original_plotly_chart = st.plotly_chart
        st._orig_stats04_plotly_chart = original_plotly_chart
        def plotly_chart(fig, *args, **kwargs):
            return original_plotly_chart(_translate_plotly_figure(fig), *args, **kwargs)
        st.plotly_chart = plotly_chart

    st._diploma_i18n_stats04_patch_installed = True

