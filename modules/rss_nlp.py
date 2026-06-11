"""
Модуль RSS-анализа и тональности для трёх торговых пар:
Россия-Китай, Россия-Индия, Китай-Индия.

Основан на логике из дипломных ноутбуков (TextBlob + feedparser).
"""

import feedparser
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from textblob import TextBlob
import streamlit as st

# ------------------------------------------------------------
# Конфигурация RSS-источников для каждой пары
# ------------------------------------------------------------
RSS_SOURCES = {
    "Россия-Китай": [
        ("https://news.google.com/rss/search?q=Russia+China+trade&hl=en&gl=US&ceid=US:en", "international"),
        ("https://news.google.com/rss/search?q=Russia+China+economic+cooperation&hl=en&gl=US&ceid=US:en", "international"),
        ("https://feeds.bbci.co.uk/news/world/rss.xml", "international"),
        ("https://rss.nytimes.com/services/xml/rss/nyt/World.xml", "international"),
    ],
    "Россия-Индия": [
        ("https://news.google.com/rss/search?q=Russia+India+trade&hl=en&gl=US&ceid=US:en", "international"),
        ("https://news.google.com/rss/search?q=Russia+India+economic+cooperation&hl=en&gl=US&ceid=US:en", "international"),
        ("https://feeds.bbci.co.uk/news/world/rss.xml", "international"),
        ("https://rss.nytimes.com/services/xml/rss/nyt/World.xml", "international"),
    ],
    "Индия-Китай": [
        ("https://news.google.com/rss/search?q=China+India+trade&hl=en&gl=US&ceid=US:en", "international"),
        ("https://news.google.com/rss/search?q=China+India+economic+relations&hl=en&gl=US&ceid=US:en", "international"),
        ("https://feeds.bbci.co.uk/news/world/asia/rss.xml", "international"),
        ("https://rss.nytimes.com/services/xml/rss/nyt/World.xml", "international"),
    ],
}

# Ключевые слова для фильтрации по каждой паре
KEYWORDS = {
    "Россия-Китай": ["russia", "china", "sino-russian", "russian", "china trade", "россия", "китай"],
    "Россия-Индия": ["russia", "india", "russian", "india trade", "россия", "индия"],
    "Индия-Китай": ["china", "india", "sino-indian", "india trade", "china trade", "китай", "индия"],
}


# ------------------------------------------------------------
# Кэшируемая функция загрузки RSS
# ------------------------------------------------------------
@st.cache_data(ttl=1800)
def fetch_rss_cached(url: str, _pair_key: str) -> list:
    """
    Загружает RSS-ленту и возвращает список заголовков.
    Кэшируется на 30 минут.
    """
    try:
        feed = feedparser.parse(url)
        if feed.bozo and not feed.entries:
            return []
        
        keywords = KEYWORDS.get(_pair_key, [])
        headlines = []
        for entry in feed.entries[:10]:
            title = entry.get("title", "")
            summary = entry.get("summary", "")
            text = f"{title} {summary}".lower()
            if any(kw in text for kw in keywords):
                headlines.append(title[:150])
        return headlines
    except Exception:
        return []


# ------------------------------------------------------------
# Тестовые данные (когда RSS недоступен)
# ------------------------------------------------------------
def get_test_data(pair_key: str) -> list:
    """Возвращает тестовые заголовки для заданной пары."""
    test_data = {
        "Россия-Китай": [
            {"title": "Russia and China strengthen strategic partnership", "text": "Russia and China deepen their economic cooperation with new trade agreements and energy deals."},
            {"title": "Trade between Russia and China reaches record levels", "text": "Bilateral trade between Russia and China hits all-time high despite global economic challenges."},
            {"title": "Energy cooperation expands between Moscow and Beijing", "text": "Russia increases energy exports to China, strengthening their economic partnership."},
            {"title": "Logistical challenges persist in trade relations", "text": "Despite growing cooperation, logistical issues affect Russia-China trade routes."},
            {"title": "Western sanctions push closer cooperation", "text": "International sanctions accelerate economic integration between Russia and China."},
            {"title": "Infrastructure projects face delays", "text": "Some joint infrastructure projects between Russia and China experience implementation challenges."},
        ],
        "Россия-Индия": [
            {"title": "Russia and India expand trade cooperation", "text": "Russia and India signed new agreements to boost bilateral trade and economic ties."},
            {"title": "Trade between Russia and India reaches new heights", "text": "Bilateral trade between Russia and India continues to grow with new energy deals."},
            {"title": "Russia-India economic partnership strengthens", "text": "Moscow and New Delhi enhance their strategic partnership through increased trade."},
            {"title": "Payment issues affect Russia-India trade", "text": "Currency and payment challenges create difficulties in Russia-India trade relations."},
            {"title": "Defense and energy cooperation deepens", "text": "Russia and India expand cooperation in defense and energy sectors."},
            {"title": "Agricultural trade grows between nations", "text": "Russia and India increase trade in agricultural products and fertilizers."},
        ],
        "Индия-Китай": [
            {"title": "China-India trade tensions continue", "text": "Trade relations between China and India remain strained due to border disputes and economic competition."},
            {"title": "India reduces dependence on Chinese goods", "text": "India continues to decrease imports from China while promoting domestic manufacturing."},
            {"title": "Trade deficit with China remains high", "text": "Indias trade deficit with China continues to be a major concern for policymakers."},
            {"title": "Limited cooperation continues", "text": "Despite tensions, some areas of economic cooperation between China and India persist."},
            {"title": "China remains Indias largest trading partner", "text": "Despite efforts to diversify, China continues to be Indias most significant trade partner."},
            {"title": "Manufacturing competition grows", "text": "India and China compete for manufacturing investments and global market share."},
        ],
    }
    return test_data.get(pair_key, [])


# ------------------------------------------------------------
# Класс анализатора тональности
# ------------------------------------------------------------
class RSSSentimentAnalyzer:
    """
    Единый класс для сбора RSS-новостей и анализа тональности
    для всех трёх торговых пар.
    """

    def __init__(self, pair_key: str):
        """
        pair_key: "Россия-Китай", "Россия-Индия" или "Индия-Китай"
        """
        self.pair_key = pair_key
        self.rss_sources = RSS_SOURCES.get(pair_key, [])
        self.stats = {"total": 0, "successful": 0, "failed": 0}

    def analyze_sentiment(self, text: str) -> float:
        """Анализ тональности через TextBlob. Возвращает polarity (-1..1)."""
        try:
            if len(text) < 10:
                return 0.0
            blob = TextBlob(text)
            return round(blob.sentiment.polarity, 4)
        except Exception:
            return 0.0

    def collect_data(self) -> pd.DataFrame:
        """
        Собирает новости из RSS-источников, фильтрует по ключевым словам,
        анализирует тональность. Если RSS пуст — использует тестовые данные.
        Возвращает DataFrame с колонками: title, text, source, sentiment.
        """
        all_articles = []

        for url, country in self.rss_sources:
            headlines = fetch_rss_cached(url, self.pair_key)
            if headlines:
                self.stats["successful"] += 1
                for h in headlines:
                    all_articles.append({
                        "title": h,
                        "text": h,
                        "source": url,
                        "country": country,
                    })
            else:
                self.stats["failed"] += 1

        # Если RSS не дал результатов — используем тестовые данные
        if len(all_articles) == 0:
            test_data = get_test_data(self.pair_key)
            for item in test_data:
                all_articles.append({
                    "title": item["title"],
                    "text": item["text"],
                    "source": "test",
                    "country": "test",
                })

        # Анализ тональности
        for article in all_articles:
            article["sentiment"] = self.analyze_sentiment(article["text"])

        self.stats["total"] = len(all_articles)
        return pd.DataFrame(all_articles)

    def get_summary(self, df: pd.DataFrame) -> dict:
        """
        Возвращает сводку по DataFrame:
        - average_polarity: средняя тональность
        - positive_count: количество позитивных (> 0.05)
        - negative_count: количество негативных (< -0.05)
        - neutral_count: количество нейтральных
        - positive_pct, negative_pct, neutral_pct: проценты
        - overall: текстовая оценка
        - nlp_adjustment: поправка в % (polarity * 20)
        """
        if len(df) == 0:
            return {
                "average_polarity": 0.0,
                "positive_count": 0, "negative_count": 0, "neutral_count": 0,
                "positive_pct": 0, "negative_pct": 0, "neutral_pct": 0,
                "overall": "Нет данных",
                "nlp_adjustment": 0.0,
                "total_articles": 0,
            }

        avg = df["sentiment"].mean()
        pos = len(df[df["sentiment"] > 0.05])
        neg = len(df[df["sentiment"] < -0.05])
        neu = len(df) - pos - neg
        total = len(df)

        # Текстовая оценка (жёсткие пороги — нейтральная зона сужена)
        if avg > 0.3:
            overall = "Выраженный позитивный фон"
        elif avg > 0.15:
            overall = "Умеренно позитивный фон"
        elif avg > 0.05:
            overall = "Слабо позитивный фон"
        elif avg >= -0.05:
            overall = "Нейтральный фон"
        elif avg >= -0.15:
            overall = "Слабо негативный фон"
        elif avg >= -0.3:
            overall = "Умеренно негативный фон"
        else:
            overall = "Выраженный негативный фон"

        # NLP-поправка: полярность * 20 (например, 0.1 -> +2%)
        nlp_adjustment = round(avg * 20, 2)

        return {
            "average_polarity": round(avg, 4),
            "positive_count": pos,
            "negative_count": neg,
            "neutral_count": neu,
            "positive_pct": round(pos / total * 100, 1) if total > 0 else 0,
            "negative_pct": round(neg / total * 100, 1) if total > 0 else 0,
            "neutral_pct": round(neu / total * 100, 1) if total > 0 else 0,
            "overall": overall,
            "nlp_adjustment": nlp_adjustment,
            "total_articles": total,
        }

    def run(self) -> tuple:
        """
        Полный цикл: сбор -> анализ -> сводка.
        Возвращает (DataFrame, summary_dict).
        """
        df = self.collect_data()
        summary = self.get_summary(df)
        return df, summary
