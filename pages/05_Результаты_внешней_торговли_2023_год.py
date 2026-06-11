import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Результаты внешней торговли", page_icon=None, layout="wide")

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

# =============================================================================
# ДАННЫЕ ИТОГОВОГО БЛОКА
# =============================================================================
TOTAL_TRIANGLE = 447.5

pairs_df = pd.DataFrame([
    {
        "Пара": "Россия - Китай",
        "Оборот": 240.1,
        "Доля": 53.7,
        "Экспорт_РФ": 129.2,
        "Импорт_РФ": 110.9,
        "Сальдо": 18.3,
        "Покрытие": 116.5,
        "Роль": "крупнейшая и наиболее сбалансированная ось",
    },
    {
        "Пара": "Россия - Индия",
        "Оборот": 71.2,
        "Доля": 15.9,
        "Экспорт_РФ": 67.1,
        "Импорт_РФ": 4.1,
        "Сальдо": 63.0,
        "Покрытие": 1653.0,
        "Роль": "самая асимметричная пара с преобладанием российского экспорта",
    },
    {
        "Пара": "Китай - Индия",
        "Оборот": 136.2,
        "Доля": 30.4,
        "Экспорт_РФ": np.nan,
        "Импорт_РФ": np.nan,
        "Сальдо": np.nan,
        "Покрытие": np.nan,
        "Роль": "самостоятельный крупный контур торговли внутри треугольника",
    },
])

# Опорные точки сделаны не как абстрактные дуги, а как географические маршруты
# через реальные транспортные узлы. Это делает карту похожей на дорожную схему,
# а не на декоративные линии между столицами.
nodes = {
    # Главные центры
    "Москва": {"lat": 55.7558, "lon": 37.6173, "color": "#2D3A2D", "size": 24, "kind": "main"},
    "Пекин": {"lat": 39.9042, "lon": 116.4074, "color": "#CC2936", "size": 24, "kind": "main"},
    "Нью-Дели": {"lat": 28.6139, "lon": 77.2090, "color": "#E8A838", "size": 23, "kind": "main"},

    # Российские узлы сухопутного направления
    "Казань": {"lat": 55.7961, "lon": 49.1064, "color": "#6A9A7B", "size": 9, "kind": "hub"},
    "Екатеринбург": {"lat": 56.8389, "lon": 60.6057, "color": "#6A9A7B", "size": 10, "kind": "hub"},
    "Новосибирск": {"lat": 55.0084, "lon": 82.9357, "color": "#6A9A7B", "size": 10, "kind": "hub"},
    "Иркутск": {"lat": 52.2864, "lon": 104.2807, "color": "#6A9A7B", "size": 9, "kind": "hub"},
    "Чита": {"lat": 52.0333, "lon": 113.5000, "color": "#6A9A7B", "size": 9, "kind": "hub"},
    "Забайкальск": {"lat": 49.6370, "lon": 117.3240, "color": "#6A9A7B", "size": 11, "kind": "hub"},
    "Хоргос": {"lat": 43.7690, "lon": 80.4180, "color": "#6A9A7B", "size": 10, "kind": "hub"},

    # Дальний Восток и морское направление
    "Владивосток": {"lat": 43.1056, "lon": 131.8740, "color": "#6A9A7B", "size": 12, "kind": "hub"},
    "Порт Восточный": {"lat": 42.7380, "lon": 133.0370, "color": "#6A9A7B", "size": 11, "kind": "hub"},
    "Шанхай": {"lat": 31.2304, "lon": 121.4737, "color": "#6A9A7B", "size": 10, "kind": "hub"},

    # Индийское и южное направление
    "Новороссийск": {"lat": 44.7167, "lon": 37.7333, "color": "#6A9A7B", "size": 12, "kind": "hub"},
    "Астрахань": {"lat": 46.3497, "lon": 48.0408, "color": "#6A9A7B", "size": 9, "kind": "hub"},
    "Бендер-Аббас": {"lat": 27.1832, "lon": 56.2666, "color": "#6A9A7B", "size": 11, "kind": "hub"},
    "Мумбаи": {"lat": 19.0760, "lon": 72.8777, "color": "#6A9A7B", "size": 11, "kind": "hub"},
    "Ченнаи": {"lat": 13.0827, "lon": 80.2707, "color": "#6A9A7B", "size": 12, "kind": "hub"},
}

trade_routes = [
    {
        "name": "Россия - Китай",
        "short": "РФ - КНР",
        "turnover": 240.1,
        "share": 53.7,
        "color": "#4A7CF7",
        "width": 5.6,
        "dash": "dash",
        "path": ["Москва", "Казань", "Екатеринбург", "Новосибирск", "Иркутск", "Чита", "Забайкальск", "Пекин"],
        "details": "Оборот 240,1 млрд $. Экспорт России 129,2 млрд $, импорт из Китая 110,9 млрд $.",
    },
    {
        "name": "Россия - Индия",
        "short": "РФ - Индия",
        "turnover": 71.2,
        "share": 15.9,
        "color": "#E8A838",
        "width": 4.1,
        "dash": "dash",
        "path": ["Москва", "Новороссийск", "Бендер-Аббас", "Мумбаи", "Нью-Дели"],
        "details": "Оборот 71,2 млрд $. Экспорт России 67,1 млрд $, импорт из Индии 4,1 млрд $.",
    },
    {
        "name": "Китай - Индия",
        "short": "КНР - Индия",
        "turnover": 136.2,
        "share": 30.4,
        "color": "#CC2936",
        "width": 4.8,
        "dash": "dot",
        "path": ["Пекин", "Шанхай", "Ченнаи", "Нью-Дели"],
        "details": "Оборот 136,2 млрд $. Эта ось по масштабу заметно превышает связь России с Индией.",
    },
]

logistics_routes = [
    {
        "name": "Транссибирское направление",
        "group": "Китай",
        "color": "#2D3A2D",
        "width": 3.7,
        "dash": "dash",
        "path": ["Москва", "Казань", "Екатеринбург", "Новосибирск", "Иркутск", "Чита", "Забайкальск", "Пекин"],
        "desc": "Основной сухопутный коридор торговли с Китаем.",
    },
    {
        "name": "Дальневосточный морской маршрут",
        "group": "Китай",
        "color": "#4682B4",
        "width": 3.5,
        "dash": "dashdot",
        "path": ["Москва", "Екатеринбург", "Новосибирск", "Иркутск", "Владивосток", "Порт Восточный", "Шанхай"],
        "desc": "Морское плечо через порты Дальнего Востока.",
    },
    {
        "name": "Южный сухопутный маршрут",
        "group": "Китай",
        "color": "#6A9A7B",
        "width": 3.3,
        "dash": "dot",
        "path": ["Москва", "Екатеринбург", "Хоргос", "Пекин"],
        "desc": "Альтернативная сухопутная опора через Хоргос.",
    },
    {
        "name": "МТК Север - Юг",
        "group": "Индия",
        "color": "#E8A838",
        "width": 3.7,
        "dash": "dash",
        "path": ["Москва", "Астрахань", "Бендер-Аббас", "Мумбаи", "Нью-Дели"],
        "desc": "Ключевой мультимодальный маршрут в Индию.",
    },
    {
        "name": "Черноморско-индийский морской маршрут",
        "group": "Индия",
        "color": "#D4A574",
        "width": 3.3,
        "dash": "dashdot",
        "path": ["Москва", "Новороссийск", "Бендер-Аббас", "Ченнаи", "Нью-Дели"],
        "desc": "Морской канал поставок через южные порты.",
    },
]

# =============================================================================
# СТИЛИ
# =============================================================================
st.markdown(
    """
    <style>
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #212529;
    }
    .stApp { background: #FFFFFF; }
    h1, h2, h3, h4, h5 {
        font-family: 'Source Sans Pro', 'Inter', sans-serif;
        font-weight: 600;
        letter-spacing: -0.01em;
        color: #1a1a2e;
    }
    .hero-kicker {
        font-size: 0.78rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #6C757D;
        margin-bottom: 0.35rem;
    }
    .hero-title {
        font-size: 2.25rem;
        font-weight: 700;
        color: #1a1a2e;
        margin: 0;
        line-height: 1.08;
    }
    .hero-subtitle {
        color: #6C757D;
        font-size: 1rem;
        margin-top: 0.55rem;
        margin-bottom: 1.25rem;
        max-width: 1080px;
        line-height: 1.55;
    }
    .card {
        background: #FFFFFF;
        border: 1px solid #E9ECEF;
        border-radius: 12px;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.04);
    }
    .stat-card { padding: 1rem 1.05rem; min-height: 124px; }
    .stat-label {
        color: #6C757D;
        font-size: 0.81rem;
        margin-bottom: 0.4rem;
        letter-spacing: 0.02em;
    }
    .stat-value {
        color: #1a1a2e;
        font-size: 1.9rem;
        font-weight: 700;
        line-height: 1.0;
        margin-bottom: 0.38rem;
    }
    .stat-note {
        color: #495057;
        font-size: 0.86rem;
        line-height: 1.42;
    }
    .section-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #1a1a2e;
        margin-top: 1.55rem;
        margin-bottom: 0.35rem;
    }
    .section-subtitle {
        color: #6C757D;
        font-size: 0.96rem;
        margin-bottom: 0.8rem;
    }
    .info-card { padding: 0.92rem 1rem; margin-bottom: 0.85rem; }
    .info-title {
        color: #1a1a2e;
        font-weight: 700;
        font-size: 0.98rem;
        margin-bottom: 0.25rem;
    }
    .info-text {
        color: #495057;
        font-size: 0.86rem;
        line-height: 1.45;
    }
    .highlight-box {
        padding: 0.92rem 1rem;
        border-left: 4px solid #4A7CF7;
        margin-bottom: 0.8rem;
    }
    .highlight-title {
        color: #1a1a2e;
        font-weight: 700;
        font-size: 0.95rem;
        margin-bottom: 0.20rem;
    }
    .highlight-text {
        color: #495057;
        font-size: 0.87rem;
        line-height: 1.45;
    }
    .footnote {
        color: #ADB5BD;
        font-size: 0.78rem;
        margin-top: 0.2rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        border-bottom: 1px solid #E9ECEF;
    }
    .stTabs [data-baseweb="tab"] {
        background: #FFFFFF;
        border-radius: 10px 10px 0 0;
        color: #495057;
        padding: 0.75rem 1rem;
        border: 1px solid #E9ECEF;
        border-bottom: none;
    }
    .stTabs [aria-selected="true"] {
        background: #F8F9FA;
        color: #1a1a2e;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

lang_col1, lang_col2 = st.columns([6, 1])
with lang_col2:
    if render_lang_switcher:
        render_lang_switcher()

# =============================================================================
# ФУНКЦИИ
# =============================================================================
def money(v: float) -> str:
    return f"{v:.1f} млрд $".replace(".", ",")

def pct(v: float) -> str:
    return f"{v:.1f}%".replace(".", ",")

def interpolate_segment(lat1, lon1, lat2, lon2, n=45):
    """Лёгкая интерполяция между опорными точками без декоративных дуг."""
    t = np.linspace(0, 1, n)
    # Небольшая поправка на широту делает линию менее механической, но не уводит маршрут от географии.
    lat = lat1 + (lat2 - lat1) * t + 0.18 * np.sin(np.pi * t) * np.sign(lon2 - lon1)
    lon = lon1 + (lon2 - lon1) * t
    return lat, lon

def path_to_line(path, n_per_segment=45):
    lats, lons = [], []
    for i in range(len(path) - 1):
        a, b = nodes[path[i]], nodes[path[i + 1]]
        seg_lat, seg_lon = interpolate_segment(a["lat"], a["lon"], b["lat"], b["lon"], n=n_per_segment)
        if i > 0:
            seg_lat = seg_lat[1:]
            seg_lon = seg_lon[1:]
        lats.extend(seg_lat)
        lons.extend(seg_lon)
    return np.array(lats), np.array(lons)

def add_dashed_route(fig, lat, lon, color, width, dash="dash", hovertext=None, opacity=0.94):
    """Контурный пунктир: белая подложка + серая обводка + цветная пунктирная линия."""
    fig.add_trace(go.Scattergeo(
        lat=lat,
        lon=lon,
        mode="lines",
        line=dict(width=width + 6.4, color="rgba(255,255,255,0.98)", dash=dash),
        hoverinfo="skip",
        showlegend=False,
    ))
    fig.add_trace(go.Scattergeo(
        lat=lat,
        lon=lon,
        mode="lines",
        line=dict(width=width + 3.0, color="rgba(33,37,41,0.34)", dash=dash),
        hoverinfo="skip",
        showlegend=False,
    ))
    fig.add_trace(go.Scattergeo(
        lat=lat,
        lon=lon,
        mode="lines",
        line=dict(width=width, color=color, dash=dash),
        opacity=opacity,
        hoverinfo="text" if hovertext else "skip",
        hovertext=hovertext,
        showlegend=False,
    ))

def base_geo_layout(fig: go.Figure, height=700):
    fig.update_layout(
        height=height,
        margin=dict(l=8, r=8, t=8, b=8),
        template="plotly_white",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        geo=dict(
            projection_type="natural earth",
            showcountries=True,
            countrycolor="#CED4DA",
            countrywidth=0.85,
            showframe=False,
            showcoastlines=True,
            coastlinecolor="#DEE2E6",
            showland=True,
            landcolor="#F5F7FA",
            showocean=True,
            oceancolor="#F8FBFF",
            showlakes=True,
            lakecolor="#EEF4FA",
            bgcolor="#FFFFFF",
            lonaxis=dict(range=[18, 138]),
            lataxis=dict(range=[5, 70]),
        ),
        hoverlabel=dict(bgcolor="white", font_size=12, font_family="Inter", bordercolor="#DEE2E6"),
        showlegend=False,
    )
    return fig

def add_country_layer(fig):
    fig.add_trace(go.Choropleth(
        locations=["Russia", "China", "India"],
        z=[2.4, 3.0, 1.9],
        showscale=False,
        colorscale=[
            [0.0, "#F5F7FA"],
            [0.45, "#EDF2F7"],
            [0.75, "#E7EEF8"],
            [1.0, "#DDE8F8"],
        ],
        marker=dict(line=dict(color="#CED4DA", width=1.0)),
        hoverinfo="location",
    ))

def add_main_nodes(fig, names):
    lat = [nodes[n]["lat"] for n in names]
    lon = [nodes[n]["lon"] for n in names]
    sizes = [nodes[n]["size"] for n in names]
    colors = [nodes[n]["color"] for n in names]
    fig.add_trace(go.Scattergeo(
        lat=lat,
        lon=lon,
        mode="markers",
        marker=dict(size=[s * 1.65 for s in sizes], color=colors, opacity=0.13, line=dict(width=0)),
        hoverinfo="skip",
        showlegend=False,
    ))
    fig.add_trace(go.Scattergeo(
        lat=lat,
        lon=lon,
        mode="markers+text",
        marker=dict(size=sizes, color=colors, line=dict(width=2.4, color="white")),
        text=names,
        textposition="top center",
        textfont=dict(size=11, color="#1a1a2e", family="Inter"),
        hoverinfo="text",
        hovertext=names,
        showlegend=False,
    ))

def add_hub_nodes(fig, names, show_text=True):
    if not names:
        return
    lat = [nodes[n]["lat"] for n in names]
    lon = [nodes[n]["lon"] for n in names]
    sizes = [nodes[n]["size"] for n in names]
    fig.add_trace(go.Scattergeo(
        lat=lat,
        lon=lon,
        mode="markers+text" if show_text else "markers",
        marker=dict(size=sizes, color="#6A9A7B", line=dict(width=1.8, color="white"), symbol="diamond"),
        text=names if show_text else None,
        textposition="bottom center",
        textfont=dict(size=8.3, color="#2D3A2D", family="Inter"),
        hoverinfo="text",
        hovertext=names,
        showlegend=False,
    ))

def add_route_number_markers(fig, path, color):
    # Номера ставятся только на ключевые точки, не на каждую мелкую интерполяцию.
    lat = [nodes[p]["lat"] for p in path]
    lon = [nodes[p]["lon"] for p in path]
    numbers = [str(i + 1) for i in range(len(path))]
    fig.add_trace(go.Scattergeo(
        lat=lat,
        lon=lon,
        mode="markers+text",
        marker=dict(size=14, color="#343A40", line=dict(width=1.6, color="white"), symbol="square"),
        text=numbers,
        textposition="middle center",
        textfont=dict(size=8, color="white", family="Inter"),
        hoverinfo="text",
        hovertext=[f"{i + 1}. {point}" for i, point in enumerate(path)],
        showlegend=False,
    ))

def create_trade_map(focus_pair="Все связи", show_hubs=True, show_labels=False):
    fig = go.Figure()
    add_country_layer(fig)

    selected_routes = trade_routes if focus_pair == "Все связи" else [r for r in trade_routes if r["name"] == focus_pair]

    used_hubs = []
    for route in selected_routes:
        lat, lon = path_to_line(route["path"], n_per_segment=42)
        hovertext = (
            f"<b>{route['name']}</b><br>"
            f"Оборот: {money(route['turnover'])}<br>"
            f"Доля в треугольнике: {pct(route['share'])}<br>"
            f"{route['details']}"
        )
        add_dashed_route(fig, lat, lon, route["color"], route["width"], dash=route["dash"], hovertext=hovertext)
        used_hubs.extend([p for p in route["path"] if nodes[p]["kind"] == "hub"])

        if show_labels:
            idx = int(len(lat) * 0.58)
            fig.add_trace(go.Scattergeo(
                lat=[lat[idx]],
                lon=[lon[idx]],
                mode="markers+text",
                marker=dict(size=24, color="white", line=dict(width=2.4, color=route["color"])),
                text=[f"<b>{route['turnover']:.1f}</b>".replace(".", ",")],
                textposition="middle center",
                textfont=dict(size=9, color=route["color"], family="Inter"),
                hoverinfo="skip",
                showlegend=False,
            ))

    if show_hubs:
        add_hub_nodes(fig, sorted(set(used_hubs)), show_text=False)
    add_main_nodes(fig, ["Москва", "Пекин", "Нью-Дели"])
    base_geo_layout(fig, height=700)
    return fig

def create_logistics_map(focus="Все маршруты", show_steps=True):
    fig = go.Figure()
    add_country_layer(fig)

    selected = logistics_routes if focus == "Все маршруты" else [r for r in logistics_routes if r["group"] == focus]
    used_points = []

    for route in selected:
        lat, lon = path_to_line(route["path"], n_per_segment=38)
        hovertext = f"<b>{route['name']}</b><br>{route['desc']}"
        add_dashed_route(fig, lat, lon, route["color"], route["width"], dash=route["dash"], hovertext=hovertext, opacity=0.92)
        used_points.extend(route["path"])
        if show_steps:
            add_route_number_markers(fig, route["path"], route["color"])

    used_points = sorted(set(used_points), key=lambda n: (nodes[n]["lon"], nodes[n]["lat"]))
    add_hub_nodes(fig, [n for n in used_points if nodes[n]["kind"] == "hub"], show_text=False)
    add_main_nodes(fig, [n for n in used_points if nodes[n]["kind"] == "main"])
    base_geo_layout(fig, height=700)
    return fig

def create_triangle_share_chart():
    fig = go.Figure(go.Pie(
        labels=pairs_df["Пара"],
        values=pairs_df["Оборот"],
        hole=0.65,
        sort=False,
        marker=dict(colors=["#4A7CF7", "#E8A838", "#CC2936"], line=dict(color="white", width=2)),
        textinfo="percent",
        textfont=dict(size=13, color="#1a1a2e"),
        hovertemplate="%{label}<br>Оборот: %{value:.1f} млрд $<br>Доля: %{percent}<extra></extra>",
    ))
    fig.update_layout(
        height=370,
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#1a1a2e"),
        annotations=[dict(
            text="447,5<br><span style='font-size:12px;color:#6C757D'>млрд $</span>",
            x=0.5,
            y=0.5,
            showarrow=False,
            font=dict(size=22, color="#1a1a2e"),
        )],
        legend=dict(orientation="h", y=-0.08, x=0.5, xanchor="center"),
    )
    return fig

def create_axis_bar_chart():
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=pairs_df["Оборот"],
        y=pairs_df["Пара"],
        orientation="h",
        marker=dict(color=["#4A7CF7", "#E8A838", "#CC2936"]),
        text=[money(v) for v in pairs_df["Оборот"]],
        textposition="outside",
        hovertemplate="%{y}<br>Оборот: %{x:.1f} млрд $<extra></extra>",
    ))
    fig.update_layout(
        height=370,
        margin=dict(l=20, r=20, t=10, b=10),
        template="plotly_white",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(title="млрд долларов США", gridcolor="#E9ECEF", zeroline=False),
        yaxis=dict(title="", gridcolor="rgba(0,0,0,0)"),
        font=dict(color="#1a1a2e"),
        showlegend=False,
    )
    return fig

def create_rf_structure_chart():
    df = pd.DataFrame([
        {"Партнёр": "Китай", "Экспорт": 129.2, "Импорт": 110.9},
        {"Партнёр": "Индия", "Экспорт": 67.1, "Импорт": 4.1},
    ])
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df["Партнёр"],
        y=df["Экспорт"],
        name="Экспорт России",
        marker=dict(color="#4A7CF7"),
        text=[money(v) for v in df["Экспорт"]],
        textposition="outside",
        hovertemplate="%{x}<br>Экспорт России: %{y:.1f} млрд $<extra></extra>",
    ))
    fig.add_trace(go.Bar(
        x=df["Партнёр"],
        y=df["Импорт"],
        name="Импорт России",
        marker=dict(color="#E8A838"),
        text=[money(v) for v in df["Импорт"]],
        textposition="outside",
        hovertemplate="%{x}<br>Импорт России: %{y:.1f} млрд $<extra></extra>",
    ))
    fig.update_layout(
        height=390,
        margin=dict(l=20, r=20, t=10, b=10),
        template="plotly_white",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        barmode="group",
        yaxis=dict(title="млрд долларов США", gridcolor="#E9ECEF", zeroline=False),
        legend=dict(orientation="h", y=1.1, x=0.5, xanchor="center"),
        font=dict(color="#1a1a2e"),
    )
    return fig

def pair_summary(pair_name: str):
    row = pairs_df[pairs_df["Пара"] == pair_name].iloc[0]
    if pair_name == "Россия - Китай":
        return {
            "title": "Россия - Китай",
            "text": "Крупнейшая ось торгового треугольника и наиболее устойчивое направление по масштабу и относительному балансу.",
            "points": [
                f"Оборот: {money(row['Оборот'])}",
                f"Доля в треугольнике: {pct(row['Доля'])}",
                f"Сальдо России: {money(row['Сальдо'])}",
                f"Коэффициент покрытия: {pct(row['Покрытие'])}",
            ],
        }
    if pair_name == "Россия - Индия":
        return {
            "title": "Россия - Индия",
            "text": "Менее масштабная, но наиболее асимметричная связь, в которой почти весь результат формируется российским экспортом.",
            "points": [
                f"Оборот: {money(row['Оборот'])}",
                f"Доля в треугольнике: {pct(row['Доля'])}",
                f"Сальдо России: {money(row['Сальдо'])}",
                f"Коэффициент покрытия: {pct(row['Покрытие'])}",
            ],
        }
    return {
        "title": "Китай - Индия",
        "text": "Связь между двумя азиатскими гигантами сама по себе масштабна и подчёркивает центральное положение Китая во всей конфигурации.",
        "points": [
            f"Оборот: {money(row['Оборот'])}",
            f"Доля в треугольнике: {pct(row['Доля'])}",
            "По объёму эта ось почти вдвое превышает торговлю России с Индией.",
            "Именно она усиливает роль Китая как основного экономического центра треугольника.",
        ],
    }

# =============================================================================
# СТРАНИЦА
# =============================================================================
st.markdown(
    """
    <div class="hero-kicker">Финальный аналитический блок</div>
    <div class="hero-title">Результаты внешней торговли в 2023 году</div>
    <div class="hero-subtitle">
        Итоговый обзор торгового треугольника Россия - Китай - Индия. Карта построена не прямыми линиями между столицами,
        а пунктирными маршрутами через опорные транспортные узлы, чтобы визуализация выглядела географически осмысленно.
    </div>
    """,
    unsafe_allow_html=True,
)

card1, card2, card3, card4 = st.columns(4)
with card1:
    st.markdown(f"""
        <div class="card stat-card">
            <div class="stat-label">Совокупный товарооборот треугольника</div>
            <div class="stat-value">{money(TOTAL_TRIANGLE)}</div>
            <div class="stat-note">Итоговый масштаб торговли между Россией, Китаем и Индией в 2023 году.</div>
        </div>
        """, unsafe_allow_html=True)
with card2:
    st.markdown(f"""
        <div class="card stat-card">
            <div class="stat-label">Главная ось</div>
            <div class="stat-value">{money(240.1)}</div>
            <div class="stat-note">Россия - Китай формирует {pct(53.7)} всего треугольника.</div>
        </div>
        """, unsafe_allow_html=True)
with card3:
    st.markdown(f"""
        <div class="card stat-card">
            <div class="stat-label">Самостоятельный азиатский контур</div>
            <div class="stat-value">{money(136.2)}</div>
            <div class="stat-note">Ось Китай - Индия по масштабу выше, чем связь России с Индией.</div>
        </div>
        """, unsafe_allow_html=True)
with card4:
    st.markdown(f"""
        <div class="card stat-card">
            <div class="stat-label">Наиболее асимметричная пара</div>
            <div class="stat-value">{money(71.2)}</div>
            <div class="stat-note">Россия - Индия: сильное преобладание российского экспорта.</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="section-title">Интерактивная карта сотрудничества</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Пунктирные линии показывают не абстрактные дуги, а маршруты через ключевые географические узлы. Подробности раскрываются при наведении.</div>',
    unsafe_allow_html=True,
)

tab1, tab2 = st.tabs(["Торговые потоки", "Логистические маршруты"])

with tab1:
    map_col, panel_col = st.columns([2.2, 1.0])
    with map_col:
        c1, c2, c3 = st.columns([1.25, 0.95, 0.95])
        with c1:
            focus_pair = st.selectbox("Фокус", ["Все связи", "Россия - Китай", "Россия - Индия", "Китай - Индия"])
        with c2:
            show_hubs = st.toggle("Узлы", value=True)
        with c3:
            show_labels = st.toggle("Числа на карте", value=False)
        st.plotly_chart(create_trade_map(focus_pair, show_hubs, show_labels), use_container_width=True)
        st.markdown(
            '<div class="footnote">Толщина пунктирной линии отражает относительный масштаб торговой связи. Маршруты проведены через опорные города и порты.</div>',
            unsafe_allow_html=True,
        )

    with panel_col:
        panel_pairs = ["Россия - Китай", "Россия - Индия", "Китай - Индия"] if focus_pair == "Все связи" else [focus_pair]
        for name in panel_pairs:
            s = pair_summary(name)
            bullets = ''.join([f'<li style="margin-bottom:0.28rem;">{p}</li>' for p in s["points"]])
            st.markdown(f"""
                <div class="card info-card">
                    <div class="info-title">{s['title']}</div>
                    <div class="info-text" style="margin-bottom:0.45rem;">{s['text']}</div>
                    <div class="info-text"><ul style="padding-left:1rem; margin:0;">{bullets}</ul></div>
                </div>
                """, unsafe_allow_html=True)

with tab2:
    log_col, note_col = st.columns([2.2, 1.0])
    with log_col:
        lc1, lc2 = st.columns([1.25, 0.95])
        with lc1:
            logistics_focus = st.selectbox("Маршруты", ["Все маршруты", "Китай", "Индия"])
        with lc2:
            show_steps = st.toggle("Нумерация узлов", value=True)
        st.plotly_chart(create_logistics_map(logistics_focus, show_steps), use_container_width=True)
        st.markdown(
            '<div class="footnote">Номера показывают последовательность прохождения маршрута через транспортные узлы.</div>',
            unsafe_allow_html=True,
        )

    with note_col:
        logistics_notes = {
            "Все маршруты": [
                ("Китайское направление", "Опирается сразу на несколько типов логистики: сухопутные коридоры, пограничные переходы и дальневосточные порты."),
                ("Индийское направление", "Сильнее зависит от морской и мультимодальной схемы, включая Новороссийск, Бендер-Аббас и МТК Север - Юг."),
                ("Общий смысл", "Китайские маршруты выглядят более диверсифицированными, тогда как индийская ось заметнее завязана на длинную внешнюю логистику."),
            ],
            "Китай": [
                ("Сухопутная опора", "Главный плюс китайского направления - наличие мощных сухопутных коридоров и альтернативных пограничных маршрутов."),
                ("Морское плечо", "Порты Дальнего Востока усиливают устойчивость и масштаб торговли с Китаем."),
                ("Итог", "Логистика с Китаем выглядит более глубокой и диверсифицированной, чем с Индией."),
            ],
            "Индия": [
                ("Морская зависимость", "Основной груз идёт через морские и мультимодальные маршруты, что повышает роль портовой и транзитной инфраструктуры."),
                ("Коридор Север - Юг", "Именно он выступает стратегической логистической основой для усиления связи России с Индией."),
                ("Итог", "Индийское направление перспективно, но по логистике более уязвимо и сложнее, чем китайское."),
            ],
        }
        for title, text in logistics_notes[logistics_focus]:
            st.markdown(f"""
                <div class="card highlight-box">
                    <div class="highlight-title">{title}</div>
                    <div class="highlight-text">{text}</div>
                </div>
                """, unsafe_allow_html=True)

st.markdown('<div class="section-title">Визуальный итог по структуре сотрудничества</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Диаграммы поддерживают карту и показывают относительный вес каждой оси без дублирования подробных расчётов с других страниц.</div>',
    unsafe_allow_html=True,
)

c_left, c_right = st.columns(2)
with c_left:
    st.markdown('<div class="card info-card"><div class="info-title">Доли в торговом треугольнике</div></div>', unsafe_allow_html=True)
    st.plotly_chart(create_triangle_share_chart(), use_container_width=True)
with c_right:
    st.markdown('<div class="card info-card"><div class="info-title">Оборот по ключевым осям</div></div>', unsafe_allow_html=True)
    st.plotly_chart(create_axis_bar_chart(), use_container_width=True)

st.markdown('<div class="card info-card"><div class="info-title">Экспорт и импорт России по двум основным направлениям</div></div>', unsafe_allow_html=True)
st.plotly_chart(create_rf_structure_chart(), use_container_width=True)

st.markdown('<div class="section-title">Ключевые выводы</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Итоговая интерпретация 2023 года: масштаб, структура и центр тяжести сотрудничества.</div>',
    unsafe_allow_html=True,
)

conclusion_col1, conclusion_col2 = st.columns(2)
conclusions = [
    (
        "Китай - центральный узел всей конструкции",
        "Именно Китай соединяет в себе крупнейшую ось с Россией и очень крупный самостоятельный контур с Индией. По этой причине он выступает главным экономическим полюсом торгового треугольника.",
    ),
    (
        "Россия - Китай - ведущая ось сотрудничества",
        "На эту пару приходится 240,1 млрд $, или 53,7% всего треугольника. При этом связь выглядит относительно сбалансированной, что выгодно отличает её от оси Россия - Индия.",
    ),
    (
        "Россия - Индия - сильная асимметрия при меньшем масштабе",
        "Оборот 71,2 млрд $ сопровождается высоким положительным сальдо России и крайне высоким коэффициентом покрытия. Это указывает на ярко выраженную экспортную направленность связи.",
    ),
    (
        "Финальная конфигурация неравномерна",
        "Треугольник Россия - Китай - Индия в 2023 году представляет собой не равновесное пространство, а систему, где Россия выступает поставщиком, Китай - центральным рынком и хабом, а Индия - быстро растущим, но более узким направлением.",
    ),
]

for i, (title, text) in enumerate(conclusions):
    box = f"""
        <div class="card highlight-box">
            <div class="highlight-title">{title}</div>
            <div class="highlight-text">{text}</div>
        </div>
    """
    if i % 2 == 0:
        with conclusion_col1:
            st.markdown(box, unsafe_allow_html=True)
    else:
        with conclusion_col2:
            st.markdown(box, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
