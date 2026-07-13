import streamlit as st


def show_profile(profile):

    st.header("📋 Dataset Profile")

    st.subheader("🔢 Numeric Columns")
    st.write(profile["numeric"])

    st.subheader("📝 Categorical Columns")
    st.write(profile["categorical"])

    st.subheader("📅 Date Columns")
    st.write(profile["datetime"])

    st.subheader("✅ Boolean Columns")
    st.write(profile["boolean"])

    st.subheader("🆔 ID Columns")
    st.write(profile["id_columns"])