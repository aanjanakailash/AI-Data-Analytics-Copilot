import streamlit as st


def show_dax(measures):

    st.header("📏 Power BI DAX Measures")

    for measure in measures:

        st.subheader(measure["name"])

        st.code(
            measure["formula"],
            language="sql"
        )