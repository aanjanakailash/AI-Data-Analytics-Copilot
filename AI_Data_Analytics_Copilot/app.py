import streamlit as st

# ============================
# Agents
# ============================

from agents.eda_agent import EDAAgent
from agents.cleaning_agent import CleaningAgent
from agents.profiler_agent import ProfilerAgent
from agents.dashboard_agent import DashboardAgent
from agents.dax_agent import DAXAgent
from agents.insight_agent import InsightAgent
from agents.chat_agent import ChatAgent

# ============================
# Components
# ============================

from components.uploader import upload_file
from components.eda_report import show_eda_report
from components.profiler_report import show_profile
from components.dashboard import show_dashboard
from components.dashboard_report import show_dashboard_plan
from components.dax_report import show_dax
from components.insight_report import show_insights
from components.chat_ui import show_chat
from components.export_report import show_export

# ============================
# Page Config
# ============================

st.set_page_config(
    page_title="AI Data Analytics Copilot",
    page_icon="📊",
    layout="wide"
)

# ============================
# Premium UI Theme (CSS only — no logic below this block)
# ============================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

html, body, [class*="css"], [class*="st-"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* ---------- Force a light, readable text theme ----------
   Streamlit falls back to its dark-theme text color (white) on
   any native element (st.header/st.write/etc. inside the report
   components) that doesn't set its own color. On our light card
   backgrounds that becomes invisible, so we pin the theme
   variables Streamlit's own CSS reads from. */
:root, .stApp {
    --text-color: #1e293b;
    --background-color: #f8fafc;
    --secondary-background-color: #ffffff;
    color: #1e293b;
}

/* ---------- App background ---------- */
.stApp {
    background: radial-gradient(circle at top left, #eef2ff 0%, #f8fafc 35%, #f8fafc 100%);
}

/* Safety net: anything rendered by the report/agent components
   inside our card containers stays dark-on-light regardless of
   the active Streamlit theme. Our own header/hero/footer text
   uses classed selectors with explicit colors, which win over
   this on specificity, so they are unaffected. */
div[data-testid="stVerticalBlockBorderWrapper"] h1,
div[data-testid="stVerticalBlockBorderWrapper"] h2,
div[data-testid="stVerticalBlockBorderWrapper"] h3,
div[data-testid="stVerticalBlockBorderWrapper"] h4,
div[data-testid="stVerticalBlockBorderWrapper"] p,
div[data-testid="stVerticalBlockBorderWrapper"] span,
div[data-testid="stVerticalBlockBorderWrapper"] label,
div[data-testid="stVerticalBlockBorderWrapper"] li,
div[data-testid="stVerticalBlockBorderWrapper"] [data-testid="stMarkdownContainer"] {
    color: #1e293b !important;
}

#MainMenu, footer[class^="css"], header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

/* ---------- Sticky gradient header ---------- */
.app-header {
    position: sticky;
    top: 0.5rem;
    z-index: 999;
    background: linear-gradient(135deg, #4338ca 0%, #6d28d9 55%, #9333ea 100%);
    border-radius: 22px;
    padding: 22px 32px;
    margin-bottom: 28px;
    box-shadow: 0 12px 32px rgba(79, 70, 229, 0.28);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
}
.app-header-left { color: #ffffff; }
.app-header-title {
    font-size: 1.65rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    margin: 0;
    color: #ffffff;
}
.app-header-subtitle {
    font-size: 0.92rem;
    font-weight: 400;
    color: rgba(255,255,255,0.85);
    margin-top: 2px;
}
.app-header-right {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}
.app-badge {
    background: rgba(255,255,255,0.16);
    border: 1px solid rgba(255,255,255,0.28);
    color: #ffffff;
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 0.80rem;
    font-weight: 600;
    backdrop-filter: blur(6px);
    white-space: nowrap;
}

/* ---------- Hero section ---------- */
.hero-wrap {
    text-align: center;
    padding: 30px 20px 10px 20px;
    margin-bottom: 10px;
}
.hero-title {
    font-size: 2.3rem;
    font-weight: 800;
    letter-spacing: -0.03em;
    background: linear-gradient(135deg, #4338ca, #9333ea);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 10px;
}
.hero-desc {
    font-size: 1.02rem;
    color: #475569;
    max-width: 640px;
    margin: 0 auto;
    line-height: 1.6;
}

/* ---------- Section title inside cards ---------- */
.section-title-row {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 14px;
}
.section-icon-badge {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 42px;
    height: 42px;
    border-radius: 14px;
    background: linear-gradient(135deg, #4f46e5, #9333ea);
    font-size: 1.2rem;
    box-shadow: 0 4px 14px rgba(79,70,229,0.28);
    flex-shrink: 0;
}
.section-title-text {
    font-size: 1.12rem;
    font-weight: 700;
    color: #1e293b;
    letter-spacing: -0.01em;
}
.section-subtitle-text {
    font-size: 0.85rem;
    color: #64748b;
    margin-top: 1px;
}

/* ---------- Card containers (bordered st.container) ---------- */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,0.78) !important;
    backdrop-filter: blur(14px);
    border-radius: 20px !important;
    border: 1px solid rgba(148,163,184,0.18) !important;
    box-shadow: 0 6px 24px rgba(15, 23, 42, 0.06);
    padding: 6px !important;
    margin-bottom: 22px;
}
div[data-testid="stVerticalBlockBorderWrapper"] > div {
    padding: 14px 10px;
}

/* ---------- Metrics / KPI cards ---------- */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.85);
    backdrop-filter: blur(10px);
    border-radius: 16px;
    padding: 18px 20px;
    border: 1px solid rgba(148,163,184,0.18);
    box-shadow: 0 4px 18px rgba(15, 23, 42, 0.05);
    transition: transform 0.22s ease, box-shadow 0.22s ease;
}
[data-testid="stMetric"]:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 28px rgba(79,70,229,0.16);
}
[data-testid="stMetricLabel"] { font-weight: 600; color: #64748b; }
[data-testid="stMetricValue"] { font-weight: 800; color: #312e81; }

/* ---------- Buttons ---------- */
.stButton > button {
    background: linear-gradient(135deg, #4f46e5, #9333ea);
    color: #ffffff;
    border: none;
    border-radius: 12px;
    padding: 0.6rem 1.4rem;
    font-weight: 600;
    font-size: 0.95rem;
    width: 100%;
    box-shadow: 0 4px 14px rgba(79,70,229,0.25);
    transition: transform 0.18s ease, box-shadow 0.18s ease;
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 24px rgba(79,70,229,0.35);
    color: #ffffff;
    border: none;
}
.stButton > button:active { transform: translateY(0px); }
.stDownloadButton > button {
    background: linear-gradient(135deg, #4f46e5, #9333ea);
    color: #ffffff;
    border: none;
    border-radius: 12px;
    font-weight: 600;
    box-shadow: 0 4px 14px rgba(79,70,229,0.25);
}

/* ---------- File uploader ---------- */
[data-testid="stFileUploaderDropzone"] {
    background: rgba(255,255,255,0.85);
    border: 2px dashed #a5b4fc;
    border-radius: 18px;
    padding: 10px;
}
[data-testid="stFileUploaderDropzone"]:hover { border-color: #7c3aed; }

/* ---------- Alerts (info / success / warning / error) ---------- */
[data-testid="stAlert"] {
    border-radius: 14px;
    backdrop-filter: blur(6px);
    box-shadow: 0 4px 16px rgba(15, 23, 42, 0.05);
}

/* ---------- Spinner ---------- */
.stSpinner > div {
    border-top-color: #7c3aed !important;
}

/* ---------- Dataframes / tables ---------- */
[data-testid="stDataFrame"] {
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(15, 23, 42, 0.05);
}

/* ---------- Chat elements (ChatGPT-style) ---------- */
[data-testid="stChatMessage"] {
    background: rgba(255,255,255,0.85);
    border-radius: 16px;
    padding: 6px 10px;
    margin-bottom: 10px;
    box-shadow: 0 3px 14px rgba(15,23,42,0.05);
    border: 1px solid rgba(148,163,184,0.15);
}
[data-testid="stChatInput"] textarea, [data-testid="stChatInputTextArea"] {
    border-radius: 14px !important;
}

/* ---------- Section divider replacement ---------- */
hr { border-color: rgba(148,163,184,0.25); }

/* ---------- Footer ---------- */
.app-footer {
    background: #1f2937;
    color: #e5e7eb;
    border-radius: 24px 24px 0 0;
    padding: 34px 24px 26px 24px;
    text-align: center;
    margin-top: 40px;
}
.app-footer-title {
    font-size: 1.15rem;
    font-weight: 800;
    color: #ffffff;
}
.app-footer-tagline {
    font-size: 0.92rem;
    color: #cbd5e1;
    margin-top: 4px;
}
.app-footer-stack {
    font-size: 0.82rem;
    color: #94a3b8;
    margin-top: 14px;
}
.app-footer-dev {
    margin-top: 18px;
    font-size: 0.88rem;
    color: #e5e7eb;
}
.app-footer-dev-name {
    font-weight: 700;
    color: #ffffff;
}
.app-footer-icons {
    margin-top: 12px;
    display: flex;
    justify-content: center;
    gap: 18px;
}
.app-footer-icons a {
    text-decoration: none;
    color: #e5e7eb;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.12);
    width: 38px;
    height: 38px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1rem;
    transition: background 0.2s ease;
}
.app-footer-icons a:hover { background: rgba(255,255,255,0.18); }
.app-footer-copy {
    margin-top: 18px;
    font-size: 0.78rem;
    color: #64748b;
}
</style>
""", unsafe_allow_html=True)

# ============================
# UI Helper Renderers (presentation only)
# ============================

def render_header():
    html = (
        '<div class="app-header">'
        '<div class="app-header-left">'
        '<p class="app-header-title">📊 AI Data Analytics Copilot</p>'
        '<p class="app-header-subtitle">Smart AI-Powered Business Intelligence Platform</p>'
        '</div>'
        '<div class="app-header-right">'
        '<span class="app-badge">🤖 AI Powered</span>'
        '<span class="app-badge">📈 Data Analytics</span>'
        '<span class="app-badge">⚡ Streamlit</span>'
        '</div>'
        '</div>'
    )
    st.markdown(html, unsafe_allow_html=True)


def render_hero():
    html = (
        '<div class="hero-wrap">'
        '<div class="hero-title">Turn Raw Data into Intelligent Decisions</div>'
        '<div class="hero-desc">'
        'Analyze any CSV or Excel dataset using Artificial Intelligence. '
        'Generate dashboards, DAX measures, business insights and chat with your data.'
        '</div>'
        '</div>'
    )
    st.markdown(html, unsafe_allow_html=True)


def section_title(icon: str, title: str, subtitle: str = None):
    subtitle_html = f'<div class="section-subtitle-text">{subtitle}</div>' if subtitle else ""
    html = (
        '<div class="section-title-row">'
        f'<div class="section-icon-badge">{icon}</div>'
        '<div>'
        f'<div class="section-title-text">{title}</div>'
        f'{subtitle_html}'
        '</div>'
        '</div>'
    )
    st.markdown(html, unsafe_allow_html=True)


def render_footer():
    html = (
        '<div class="app-footer">'
        '<div class="app-footer-title">📊 AI Data Analytics Copilot</div>'
        '<div class="app-footer-tagline">Transforming Raw Data into Intelligent Business Insights</div>'
        '<div class="app-footer-stack">Built with ❤️ using Python • Streamlit • Plotly • Pandas • AI</div>'
        '<div class="app-footer-dev">👨‍💻 Developed by '
        '<span class="app-footer-dev-name">Kailash J Choudhary</span></div>'
        '<div class="app-footer-icons">'
        '<a href="https://github.com/aanjanakailash/AI-Data-Analytics-Copilot" title="GitHub">🐙</a>'
        '<a href="linkedin.com/in/kailash-j-choudhary-b39325300" title="LinkedIn">💼</a>'
        '<a href="" title="Email">✉️</a>'
        '</div>'
        '<div class="app-footer-copy">© 2026 All Rights Reserved</div>'
        '</div>'
    )
    st.markdown(html, unsafe_allow_html=True)


# ============================
# Header + Hero
# ============================

render_header()
render_hero()

# ============================
# Upload Dataset
# ============================

with st.container(border=True):
    section_title("📤", "Upload Dataset", "CSV or Excel files supported")
    df, filename = upload_file()

if df is None:
    st.info("👆 Upload a CSV or Excel file .")
    st.stop()

# ============================
# Session State
# ============================

if "measures" not in st.session_state:
    st.session_state.measures = None

if "insights" not in st.session_state:
    st.session_state.insights = None

# ============================
# Dataset Uploaded
# ============================

st.success(f"✅ {filename} uploaded successfully.")

# ============================
# Dataset Metrics
# ============================

with st.container(border=True):
    section_title("📈", "Dataset Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    with col3:
        memory = round(df.memory_usage(deep=True).sum() / 1024**2, 2)
        st.metric("Memory (MB)", memory)

# ============================
# Dataset Preview
# ============================

with st.container(border=True):
    section_title("📄", "Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

# ============================
# EDA
# ============================

with st.container(border=True):
    section_title("🔍", "Exploratory Data Analysis")

    eda_agent = EDAAgent()
    eda_report = eda_agent.analyze(df)

    show_eda_report(eda_report)

# ============================
# Data Cleaning
# ============================

with st.container(border=True):
    section_title("🧹", "Data Cleaning")

    cleaning_agent = CleaningAgent()
    clean_df = cleaning_agent.clean(df)

    st.success("✅ Dataset cleaned successfully!")

    st.markdown("**Cleaned Dataset Preview**")
    st.dataframe(clean_df.head(10), use_container_width=True)

# ============================
# Dataset Profiling
# ============================

with st.container(border=True):
    section_title("🧬", "Dataset Profiling")

    profiler_agent = ProfilerAgent()
    profile = profiler_agent.profile(clean_df)

    show_profile(profile)

# ============================
# Interactive Dashboard
# ============================

with st.container(border=True):
    section_title("📊", "Smart Dashboard")
    show_dashboard(clean_df, profile)

# ============================
# Dashboard Plan (Optional)
# ============================

# Uncomment if you want AI Dashboard Plan

# st.divider()
#
# st.subheader("🖥 AI Dashboard Plan")
#
# if st.button("Generate Dashboard Plan"):
#
#     dashboard_agent = DashboardAgent()
#
#     with st.spinner("Generating Dashboard Plan..."):
#
#         dashboard_plan = dashboard_agent.generate_dashboard(profile)
#
#     show_dashboard_plan(dashboard_plan)

# ============================
# AI DAX Generator
# ============================

with st.container(border=True):
    section_title("📐", "AI DAX Generator")

    if st.button("📐 Generate DAX Measures"):

        dax_agent = DAXAgent()

        with st.spinner("Generating DAX Measures..."):

            try:

                st.session_state.measures = dax_agent.generate(profile)

            except Exception as e:

                st.error(e)

    if st.session_state.measures is not None:

        show_dax(st.session_state.measures)

# ============================
# AI Business Insights
# ============================

with st.container(border=True):
    section_title("🧠", "AI Business Insights", "Generate AI-powered business insights")

    if st.button("🚀 Generate AI Insights"):

        insight_agent = InsightAgent()

        with st.spinner("Generating Insights..."):

            try:

                st.session_state.insights = insight_agent.generate(
                    clean_df,
                    profile
                )

            except Exception as e:

                st.error(e)

    if st.session_state.insights is not None:

        show_insights(st.session_state.insights)

# ============================
# AI Chatbot
# ============================

with st.container(border=True):
    section_title("💬", "AI Data Analyst")

    chat_agent = ChatAgent()

    show_chat(chat_agent, clean_df)

# ============================
# Export PDF
# ============================

with st.container(border=True):
    section_title("📄", "Export Report")

    show_export(
        filename,
        clean_df,
        profile,
        st.session_state.insights,
        st.session_state.measures
    )

# ============================
# Footer
# ============================

render_footer()
