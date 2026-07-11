import requests
import streamlit as st
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

st.set_page_config(
    page_title="Adaptive LLM Safety Platform",
    page_icon="🛡️",
    layout="wide"
)

# =====================================
# Sidebar
# =====================================

st.sidebar.title("🛡️ Adaptive LLM Safety")

st.sidebar.markdown("---")

st.sidebar.success("🟢 FastAPI Connected")

st.sidebar.info("🔄 Auto Refresh: 15 sec")

st.sidebar.markdown("Version: **v1.0.0**")

st.sidebar.markdown("---")

st.sidebar.write("**Tech Stack**")
st.sidebar.write("• FastAPI")
st.sidebar.write("• Ollama")
st.sidebar.write("• Streamlit")
st.sidebar.write("• Plotly")
st.sidebar.write("• SQLite")

# =====================================
# Auto Refresh
# =====================================

st_autorefresh(
    interval=15000,
    key="dashboard_refresh"
)

st.title("🛡️ Adaptive LLM Safety Platform")

st.caption(
    "Real-time Dashboard for LLM Safety Evaluation"
)

st.markdown("---")

try:

    # =====================================
    # Statistics
    # =====================================

    stats = requests.get(
        "http://127.0.0.1:8000/stats"
    ).json()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "📊 Total",
        stats["total_experiments"]
    )

    col2.metric(
        "🟢 Safe",
        stats["safe"]
    )

    col3.metric(
        "🔴 Unsafe",
        stats["unsafe"]
    )

    col4.metric(
        "⚠ Average Risk",
        stats["average_risk_score"]
    )

    st.success("✅ Connected to FastAPI Successfully")

    st.markdown("---")

    # =====================================
    # Search
    # =====================================

    search = st.text_input(
        "🔍 Search Prompt or Strategy"
    ).lower()

    # =====================================
    # History
    # =====================================

    history = requests.get(
        "http://127.0.0.1:8000/history"
    ).json()

    history.reverse()

    st.subheader("📜 Recent Experiments")

    table = []

    for experiment in history:

        strategy = experiment["strategy"]
        prompt = experiment["original_prompt"]

        if (
            search
            and search not in strategy.lower()
            and search not in prompt.lower()
        ):
            continue

        score = experiment["risk_score"]

        if score <= 2:
            risk = "🟢 Low"
        elif score <= 5:
            risk = "🟡 Medium"
        else:
            risk = "🔴 High"

        table.append({
            "Strategy": strategy,
            "Prompt": prompt,
            "Status": "🟢 Safe" if experiment["safe"] else "🔴 Unsafe",
            "Risk": risk,
            "Risk Score": score,
            "Created": experiment["created_at"]
        })

    if len(table) == 0:

        st.warning("No experiments found.")

    else:

        st.dataframe(
            table,
            use_container_width=True
        )

    st.markdown("---")

    # =====================================
    # Charts
    # =====================================

    left, right = st.columns(2)

    with left:

        st.subheader("🥧 Safety Distribution")

        pie = px.pie(
            names=["Safe", "Unsafe"],
            values=[
                stats["safe"],
                stats["unsafe"]
            ],
            hole=0.45
        )

        st.plotly_chart(
            pie,
            use_container_width=True
        )

    with right:

        st.subheader("📈 Strategy Distribution")

        strategies = stats["strategies"]

        bar = px.bar(
            x=list(strategies.keys()),
            y=list(strategies.values()),
            labels={
                "x": "Strategy",
                "y": "Experiments"
            }
        )

        st.plotly_chart(
            bar,
            use_container_width=True
        )

    st.markdown("---")

    # =====================================
    # Risk Trend
    # =====================================

    st.subheader("📉 Risk Score Trend")

    if history:

        trend = px.line(
            x=[
                f"Exp {i+1}"
                for i in range(len(history))
            ],
            y=[
                experiment["risk_score"]
                for experiment in history
            ],
            markers=True,
            labels={
                "x": "Experiment",
                "y": "Risk Score"
            }
        )

        st.plotly_chart(
            trend,
            use_container_width=True
        )

    st.markdown("---")

    # =====================================
    # Export
    # =====================================

    st.subheader("⬇️ Export Reports")

    col1, col2 = st.columns(2)

    with col1:

        st.link_button(
            "📄 Download CSV",
            "http://127.0.0.1:8000/history/export/csv"
        )

    with col2:

        st.link_button(
            "📑 Download JSON",
            "http://127.0.0.1:8000/history/export/json"
        )

    st.markdown("---")

    st.caption(
        "Adaptive LLM Safety Platform • Version 1.0 • Built with FastAPI, Ollama, Streamlit, Plotly & SQLite"
    )

except Exception as e:

    st.error("❌ Cannot connect to FastAPI")

    st.exception(e)