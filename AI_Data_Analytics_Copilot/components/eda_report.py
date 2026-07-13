import streamlit as st


def show_eda_report(report):

    st.header("📈 Exploratory Data Analysis")

    col1, col2 = st.columns(2)

    col1.metric("Rows", report["rows"])
    col2.metric("Columns", report["columns"])

    st.divider()

    st.subheader("Column Data Types")
    st.dataframe(report["data_types"], use_container_width=True)

    st.divider()

    st.subheader("Missing Values")
    st.dataframe(report["missing_values"], use_container_width=True)

    st.divider()

    st.subheader("Duplicate Rows")
    st.metric("Duplicates", report["duplicate_rows"])

    st.divider()

    st.subheader("Summary Statistics")
    st.dataframe(report["summary"], use_container_width=True)