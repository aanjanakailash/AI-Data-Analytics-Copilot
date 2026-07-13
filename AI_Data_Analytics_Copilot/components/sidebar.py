import streamlit as st


def sidebar_menu():

    menu = st.sidebar.radio(
        "📂 Navigation",
        [
            "Dashboard",
            "EDA Report",
            "Cleaning Report",
            "Dataset Profile",
            "Dashboard Plan",
            "DAX Measures",
            "AI Insights",
            "Chat"
        ]
    )

    return menu