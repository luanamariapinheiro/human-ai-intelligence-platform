import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Human + AI",
    layout="wide"
)

st.markdown("""
<style>

/* FUNDO GERAL */

.stApp {

    background: linear-gradient(
        135deg,
        #1E293B,
        #334155
    );

    color: #F8FAFC;
}

/* TITULO PRINCIPAL */

h1 {

    color: #FFFFFF !important;

    font-size: 54px !important;

    font-weight: 800 !important;

    letter-spacing: -1px;
}

/* SUBTITULO */

h2, h3 {

    color: #E2E8F0 !important;
}

p {

    color: #CBD5E1 !important;

    font-size: 16px;
}

/* SIDEBAR */

[data-testid="stSidebar"] {

    background: linear-gradient(
        180deg,
        #0F172A,
        #1E293B
    );

    border-right: 1px solid rgba(255,255,255,0.08);
}

/* TEXTO SIDEBAR */

[data-testid="stSidebar"] * {

    color: #F8FAFC !important;
}

/* CARDS METRICAS */

[data-testid="metric-container"] {

    background: rgba(255,255,255,0.05);

    border: 1px solid rgba(255,255,255,0.08);

    padding: 24px;

    border-radius: 20px;

    backdrop-filter: blur(12px);

    box-shadow: 0 8px 24px rgba(0,0,0,0.25);
}

/* LABEL METRICAS */

[data-testid="metric-container"] label {

    color: #CBD5E1 !important;

    font-size: 15px !important;

    font-weight: 600 !important;
}

/* VALOR METRICAS */

[data-testid="metric-container"] div {

    color: #FFFFFF !important;

    font-weight: 700;
}

/* GRAFICO */

.js-plotly-plot {

    border-radius: 20px;

    overflow: hidden;

    box-shadow: 0 8px 24px rgba(0,0,0,0.25);
}

/* TABELA */

[data-testid="stDataFrame"] {

    background: rgba(255,255,255,0.04);

    border-radius: 20px;

    border: 1px solid rgba(255,255,255,0.08);

    padding: 10px;
}

/* SELECTBOX */

.stSelectbox div[data-baseweb="select"] {

    background-color: #334155;

    border-radius: 12px;

    border: 1px solid rgba(255,255,255,0.12);
}

/* ALERTA */

[data-testid="stAlert"] {

    background: rgba(255,255,255,0.05);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 18px;

    color: white;
}

</style>
""", unsafe_allow_html=True)

st.title("🚀 Human + AI Intelligence Platform")

st.subheader(
    "Profissões com maior potencial de amplificação através da Inteligência Artificial"
)

df = pd.read_csv(
    "data/ai_workforce_analysis.csv"
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Profissões Analisadas",
    len(df)
)

col2.metric(
    "Clusters Cognitivos",
    df["Cluster"].nunique()
)

col3.metric(
    "Maior AI Score",
    round(df["AI Enhancement Score"].max(), 2)
)

st.sidebar.title("Filtros")

cluster = st.sidebar.selectbox(
    "Selecione o Cluster",
    sorted(df["Cluster"].unique())
)

filtered_df = df[
    df["Cluster"] == cluster
]

fig = px.scatter(

    filtered_df,

    x="PCA1",
    y="PCA2",

    color="AI Enhancement Score",

    size="AI Enhancement Score",

    hover_name="Title",

    template="plotly_dark",

    color_continuous_scale="Turbo"
)

fig.update_traces(

    marker=dict(

        line=dict(
            width=1.2,
            color="rgba(255,255,255,0.8)"
        )
    ),

    opacity=0.9
)

fig.update_layout(

    title={
        "text": "Human + AI Cognitive Landscape",
        "x": 0.5
    },

    title_font_size=30,

    plot_bgcolor="#1E293B",

    paper_bgcolor="#1E293B",

    font=dict(
        color="#F8FAFC",
        size=15
    ),

    xaxis=dict(
        title="Cognitive Dimension 1",
        gridcolor="rgba(255,255,255,0.08)",
        zerolinecolor="rgba(255,255,255,0.12)"
    ),

    yaxis=dict(
        title="Cognitive Dimension 2",
        gridcolor="rgba(255,255,255,0.08)",
        zerolinecolor="rgba(255,255,255,0.12)"
    ),

    coloraxis_colorbar=dict(
        title="AI Score"
    ),

    height=720
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("🏆 Principais Profissões")

top_jobs = filtered_df.sort_values(
    by="AI Enhancement Score",
    ascending=False
)

st.dataframe(

    top_jobs[[
        "Title",
        "AI Enhancement Score"
    ]].head(10),

    use_container_width=True,

    hide_index=True
)

st.info(
    """
    Profissões com maiores níveis de pensamento crítico,
    aprendizado ativo e raciocínio dedutivo tendem
    a apresentar maior potencial de amplificação através da IA.
    """
)