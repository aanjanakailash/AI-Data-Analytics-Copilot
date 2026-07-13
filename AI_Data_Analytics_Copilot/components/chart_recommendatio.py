import streamlit as st


def show_chart_recommendations(recommendations):

    st.header("🤖 AI Chart Recommendations")

    for index, chart in enumerate(recommendations):

        with st.container(border=True):

            st.subheader(chart["chart"])

            col1, col2 = st.columns(2)

            with col1:
                st.write("**X Axis**")
                st.info(chart["x"])

            with col2:
                st.write("**Y Axis**")
                st.info(chart["y"])

            st.write("**Aggregation**")
            st.success(chart["aggregation"])

            st.write("**Why this chart?**")
            st.write(chart["reason"])

            st.button(
                "➕ Add to Dashboard",
                key=f"add_{index}"
            )