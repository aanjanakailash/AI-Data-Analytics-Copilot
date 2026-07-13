import streamlit as st
import pandas as pd


def upload_file():

    uploaded_file = st.file_uploader(
        "📂 Upload CSV or Excel File",
        type=["csv", "xlsx"]
    )

    if uploaded_file is not None:

        try:

            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)

            else:
                df = pd.read_excel(uploaded_file)

            return df, uploaded_file.name

        except Exception as e:

            st.error(f"Error : {e}")

            return None, None

    return None, None