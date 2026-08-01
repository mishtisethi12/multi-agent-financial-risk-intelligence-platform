import streamlit as st
import sys
import os

# ---------------------------------------
# Add project root to Python path
# ---------------------------------------

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from utils.finance import (
    analyze_portfolio,
    calculate_var,
    calculate_sharpe
)

from components.sidebar import render_sidebar
from components.dashboard import render_dashboard
from components.portfolio import render_portfolio
from components.advisor import render_advisor

# ---------------------------------------
# PAGE CONFIG
# ---------------------------------------

st.set_page_config(
    page_title="Financial Risk Intelligence Platform",
    page_icon="📈",
    layout="wide"
)

# ---------------------------------------
# CSS
# ---------------------------------------

st.markdown("""
<style>

/* App Background */
.stApp{
    background: #0E1117;
}

/* Main Heading */
h1{
    color:#4EA8FF !important;
    font-weight:800;
}

h2,h3{
    color:#E8EEF7 !important;
}

/* Metric Cards */
[data-testid="stMetric"]{
    background:#1A1F2E;
    border:1px solid #2E6BE6;
    border-radius:18px;
    padding:18px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.35);
}

/* Metric Label */
[data-testid="stMetricLabel"]{
    color:#9DB5D8 !important;
    font-size:16px;
    font-weight:600;
}

/* Metric Value */
[data-testid="stMetricValue"]{
    color:#FFFFFF !important;
    font-size:28px;
    font-weight:700;
}

/* Buttons */
.stButton>button{
    background:#2563EB;
    color:white;
    border:none;
    border-radius:12px;
    height:3em;
    font-size:16px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#1D4ED8;
    color:white;
}

/* Text Area */
textarea{
    border-radius:12px !important;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#151A28;
}

/* Sidebar Text */
section[data-testid="stSidebar"] *{
    color:white !important;
}

/* Alerts */
[data-testid="stAlert"]{
    border-radius:12px;
}

/* Tables */
[data-testid="stDataFrame"]{
    border-radius:15px;
    overflow:hidden;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------
# LIVE DATA
# ---------------------------------------

total_value, stock_values = analyze_portfolio()

var, volatility = calculate_var(total_value)

sharpe = calculate_sharpe(volatility)

# ---------------------------------------
# SIDEBAR
# ---------------------------------------

render_sidebar(stock_values)

# ---------------------------------------
# TABS
# ---------------------------------------

dashboard_tab, portfolio_tab, advisor_tab = st.tabs(
    [
        " Dashboard",
        " Portfolio",
        "🤖 AI Advisor"
    ]
)

# ---------------------------------------
# DASHBOARD
# ---------------------------------------

with dashboard_tab:

    render_dashboard(
        total_value,
        sharpe,
        var,
        stock_values
    )

# ---------------------------------------
# PORTFOLIO
# ---------------------------------------

with portfolio_tab:

    render_portfolio()

# ---------------------------------------
# AI ADVISOR
# ---------------------------------------

with advisor_tab:

    render_advisor()
    st.divider()

st.caption(
    "Built with Python • FastMCP • Google Gemini • Streamlit • Yahoo Finance • Pandas • TextBlob"
)