import streamlit as st


def show_dashboard_plan(plan):

    st.header("🧠 Dashboard Plan")

    st.subheader("📊 KPI Cards")

    st.write(plan["kpis"])

    st.subheader("📈 Charts")

    st.write(plan["charts"])

    st.subheader("🎯 Filters")

    st.write(plan["filters"])