"""
Утилиты: локализация, переключатель языка.
Использование:
    from utils import setup_i18n, L
    setup_i18n()
    st.markdown(L("title_main"))
"""
import streamlit as st
from data.locales import t as _t

APP_LANGUAGES = {
    "ru": "Русский",
    "en": "English",
}

def setup_i18n(default_lang: str = "ru"):
    """Инициализировать язык в session_state и показать переключатель."""
    if "lang" not in st.session_state:
        st.session_state.lang = default_lang

def get_lang() -> str:
    """Получить текущий язык."""
    return st.session_state.get("lang", "ru")

def L(key: str) -> str:
    """Короткий вызов перевода."""
    return _t(key, get_lang())

def Lf(key: str, *args) -> str:
    """Перевод с форматированием: Lf("hello_{name}", name="World")."""
    txt = L(key)
    if args:
        txt = txt.format(*args)
    return txt

import pandas as pd
import numpy as np

# ── Форматирование чисел ──

def to_billions(value):
    """
    Переводит значение из долларов в млрд долларов.
    Проверка порядка: если value > 1e12, вероятно это уже млрд, но делим на 1e9.
    """
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return np.nan
    return float(value) / 1e9

def fmt_billion(value, lang='ru'):
    """Форматирует значение (в долларах) в млрд $ с разделителями."""
    if pd.isna(value) or value is None:
        return "—"
    b = to_billions(value)
    if lang == 'ru':
        return f"{b:,.2f} млрд $".replace(",", " ")
    else:
        return f"{b:,.2f} B USD".replace(",", " ")

def fmt_percent(value, lang='ru'):
    """Форматирует процент с одним знаком."""
    if pd.isna(value):
        return "—"
    return f"{value:.1f}%"

def fmt_sentiment(value):
    """Форматирует тональность с тремя знаками."""
    if pd.isna(value):
        return "—"
    return f"{value:.3f}"

def render_lang_switcher():
    """Показать кнопки переключения языка."""
    current = get_lang()
    cols = st.columns(2)
    for idx, (code, label) in enumerate(APP_LANGUAGES.items()):
        with cols[idx]:
            if st.button(label.upper(), key=f"lang_{code}",
                         disabled=(current == code),
                         use_container_width=True):
                st.session_state.lang = code
                st.rerun()
