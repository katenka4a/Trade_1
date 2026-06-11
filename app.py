# -*- coding: utf-8 -*-
"""
Минимальный entrypoint Streamlit-приложения.

Файл нужен только для запуска проекта командой:
    streamlit run app.py

Все содержательные страницы проекта остаются в папке pages/.
"""

import streamlit as st


st.set_page_config(
    page_title="Внешняя торговля РФ с Китаем и Индией",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
    <style>
    html, body, [class*="css"] {
        font-family: "Inter", "Source Sans Pro", sans-serif;
        color: #20242A;
    }
    .block-container {
        max-width: 980px;
        padding-top: 4.5rem;
        padding-bottom: 2rem;
    }
    .main-title {
        font-size: 2.35rem;
        line-height: 1.12;
        font-weight: 760;
        letter-spacing: -0.03em;
        color: #121826;
        margin-bottom: 0.75rem;
    }
    .main-title-en {
        font-size: 1.35rem;
        line-height: 1.35;
        font-weight: 540;
        color: #52606D;
        margin-bottom: 2.5rem;
    }
    .edu-note {
        position: fixed;
        left: 0;
        right: 0;
        bottom: 0;
        padding: 0.75rem 1.2rem;
        border-top: 1px solid #E5EAF0;
        background: rgba(255, 255, 255, 0.96);
        color: #7B8794;
        font-size: 0.82rem;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div class="main-title">
        Статистический анализ и прогнозирование внешней торговли России с Китаем и Индией
    </div>
    <div class="main-title-en">
        Statistical Analysis and Forecasting of Russia’s Foreign Trade with China and India
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div class="edu-note">
        Проект носит исключительно учебный характер и подготовлен в рамках выпускной квалификационной работы.
        <br>
        This project is intended solely for educational purposes and was prepared as part of a graduation thesis.
    </div>
    """,
    unsafe_allow_html=True,
)
