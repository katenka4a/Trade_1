# -*- coding: utf-8 -*-
"""
RSS-анализатор торговых пар для диплома.
Перенос из ноутбука: три класса, три пары торговых отношений.
Возвращает DataFrame статей с тональностью (TextBlob).
"""
import feedparser
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from textblob import TextBlob
import time
import warnings
warnings.filterwarnings('ignore')

# ──────────────────────────────────────────────
# Настройки источников для каждой пары
# ──────────────────────────────────────────────
RSS_CONFIG = {
    "Россия-Китай": {
        "keywords": ["russia", "china", "россия", "китай", "trade", "торговля", "sino-russian"],
        "topic": "Торговые отношения Россия-Китай",
        "sources": [
            ("https://news.google.com/rss/search?q=Russia+China+trade&hl=en&gl=US&ceid=US:en", "international"),
            ("https://news.google.com/rss/search?q=Russia+China+economic+cooperation&hl=en&gl=US&ceid=US:en", "international"),
            ("https://news.google.com/rss/search?q=Sino-Russian+trade&hl=en&gl=US&ceid=US:en", "international"),
            ("https://news.google.com/rss/search?q=Россия+Китай+торговля&hl=ru&gl=RU&ceid=RU:ru", "russia"),
            ("https://feeds.bbci.co.uk/news/world/rss.xml", "international"),
            ("https://rss.nytimes.com/services/xml/rss/nyt/World.xml", "international"),
        ],
    },
    "Россия-Индия": {
        "keywords": ["russia", "india", "россия", "индия", "trade", "торговля"],
        "topic": "Торговые отношения Россия-Индия",
        "sources": [
            ("https://news.google.com/rss/search?q=Russia+India+trade&hl=en&gl=US&ceid=US:en", "international"),
            ("https://news.google.com/rss/search?q=Russia+India+economic+cooperation&hl=en&gl=US&ceid=US:en", "international"),
            ("https://feeds.bbci.co.uk/news/world/rss.xml", "international"),
            ("https://rss.nytimes.com/services/xml/rss/nyt/World.xml", "international"),
            ("https://news.google.com/rss/search?q=Россия+Индия+торговля&hl=ru&gl=RU&ceid=RU:ru", "russia"),
        ],
    },
    "Китай-Индия": {
        "keywords": ["china", "india", "китай", "индия", "trade", "торговля", "sino-indian"],
        "topic": "Торговые отношения Китай-Индия",
        "sources": [
            ("https://news.google.com/rss/search?q=China+India+trade&hl=en&gl=US&ceid=US:en", "international"),
            ("https://news.google.com/rss/search?q=China+India+economic+relations&hl=en&gl=US&ceid=US:en", "international"),
            ("https://news.google.com/rss/search?q=Sino-Indian+trade&hl=en&gl=US&ceid=US:en", "international"),
            ("https://feeds.bbci.co.uk/news/world/asia/rss.xml", "international"),
            ("https://rss.nytimes.com/services/xml/rss/nyt/World.xml", "international"),
        ],
    },
}


def analyze_sentiment(text):
    """Анализ тональности текста с помощью TextBlob, возвращает полярность [-1, 1]."""
    try:
        if not text or len(str(text)) < 10:
            return 0.0
        blob = TextBlob(str(text))
        return blob.sentiment.polarity
    except Exception:
        return 0.0


class RSSSentimentAnalyzer:
    """
    Универсальный анализатор RSS для заданной торговой пары.
    Использование:
        analyzer = RSSSentimentAnalyzer("Россия-Китай")
        df = analyzer.run_analysis()
    """

    def __init__(self, pair_key: str):
        self.pair_key = pair_key
        cfg = RSS_CONFIG.get(pair_key)
        if cfg is None:
            raise ValueError(f"Неизвестная пара: {pair_key}. Допустимые: {list(RSS_CONFIG.keys())}")
        self.keywords = cfg["keywords"]
        self.topic = cfg["topic"]
        self.rss_sources = cfg["sources"]
        self.start_date = datetime.now() - timedelta(days=30)
        self.stats = {"total_articles": 0, "successful": 0, "failed": 0}

    def fetch_rss(self, url, country):
        """Получение RSS-ленты (до 10 статей на источник)."""
        try:
            feed = feedparser.parse(url)
            articles = []
            for entry in feed.entries[:10]:
                title = entry.get("title", "")
                summary = entry.get("summary", "")
                text = f"{title} {summary}".lower()
                if not any(kw in text for kw in self.keywords):
                    continue
                articles.append({
                    "title": str(title)[:100],
                    "text": f"{title} {summary}"[:300],
                    "source": url,
                    "country": country,
                    "date": datetime.now(),
                    "pair_key": self.pair_key,
                })
            return articles
        except Exception:
            return []

    def collect_data(self):
        """Сбор статей со всех источников."""
        all_articles = []
        for url, country in self.rss_sources:
            try:
                articles = self.fetch_rss(url, country)
                if articles:
                    all_articles.extend(articles)
                    self.stats["successful"] += 1
                else:
                    self.stats["failed"] += 1
            except Exception:
                self.stats["failed"] += 1
        self.stats["total_articles"] = len(all_articles)
        return all_articles

    def run_analysis(self, verbose=False):
        """
        Полный цикл: сбор -> тональность -> DataFrame.
        Возвращает DataFrame с колонками:
          - title, text, sentiment (pol), category, source, date, pair_key
        """
        if verbose:
            print(f"Запуск анализа RSS: {self.topic}")

        articles = self.collect_data()
        if not articles:
            if verbose:
                print("Нет данных для анализа")
            return self._empty_result()

        # Анализ тональности
        for art in articles:
            art["sentiment"] = analyze_sentiment(art["text"])

        df = pd.DataFrame(articles)
        df["category"] = df["sentiment"].apply(
            lambda x: "positive" if x > 0.05 else ("negative" if x < -0.05 else "neutral")
        )

        if verbose:
            print(f"Проанализировано статей: {len(df)}")
            print(f"Средняя тональность: {df['sentiment'].mean():.3f}")
            pos = (df["category"] == "positive").mean() * 100
            neg = (df["category"] == "negative").mean() * 100
            print(f"Позитивных: {pos:.1f}%, Негативных: {neg:.1f}%")

        return df

    def _empty_result(self):
        return pd.DataFrame(columns=[
            "title", "text", "source", "country", "date", "pair_key", "sentiment", "category"
        ])

    def get_summary_sentiment(self):
        """
        Быстрый метод: возвращает словарь:
          - avg_sentiment: средняя тональность
          - pos_pct: доля позитивных
          - neg_pct: доля негативных
          - neu_pct: доля нейтральных
          - count: количество статей
        """
        df = self.run_analysis(verbose=False)
        if df.empty:
            return {"avg_sentiment": 0.0, "pos_pct": 0, "neg_pct": 0, "neu_pct": 100, "count": 0}

        avg = float(df["sentiment"].mean())
        pos = int((df["category"] == "positive").sum())
        neg = int((df["category"] == "negative").sum())
        neu = int((df["category"] == "neutral").sum())
        total = len(df)
        return {
            "avg_sentiment": avg,
            "pos_pct": round(pos / total * 100, 1) if total else 0,
            "neg_pct": round(neg / total * 100, 1) if total else 0,
            "neu_pct": round(neu / total * 100, 1) if total else 0,
            "count": total,
        }


# ──────────────────────────────────────────────
# Функция для одновременного анализа всех пар
# ──────────────────────────────────────────────
def analyze_all_pairs(verbose=False):
    """Анализирует все три торговые пары, возвращает словарь {пара: DataFrame}."""
    results = {}
    for pair in RSS_CONFIG:
        if verbose:
            print(f"\n{'='*50}\nАнализ: {pair}\n{'='*50}")
        analyzer = RSSSentimentAnalyzer(pair)
        results[pair] = analyzer.run_analysis(verbose=verbose)
    return results


def get_all_summaries():
    """Возвращает словарь {пара: summary_sentiment} для всех пар."""
    summaries = {}
    for pair in RSS_CONFIG:
        analyzer = RSSSentimentAnalyzer(pair)
        summaries[pair] = analyzer.get_summary_sentiment()
    return summaries


# ──────────────────────────────────────────────
# Демонстрация если запущен как main
# ──────────────────────────────────────────────
if __name__ == "__main__":
    print("🚀 ТЕСТОВЫЙ ЗАПУСК RSS-АНАЛИЗАТОРА")
    print("=" * 50)

    for pair in ["Россия-Китай", "Россия-Индия", "Китай-Индия"]:
        print(f"\n--- {pair} ---")
        analyzer = RSSSentimentAnalyzer(pair)
        summary = analyzer.get_summary_sentiment()
        print(f"Статей: {summary['count']}")
        print(f"Средняя тональность: {summary['avg_sentiment']:.3f}")
        print(f"Позитивные: {summary['pos_pct']}%")
        print(f"Негативные: {summary['neg_pct']}%")
        print(f"Нейтральные: {summary['neu_pct']}%")
