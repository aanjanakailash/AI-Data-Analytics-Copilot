import streamlit as st
import pandas as pd


def show_chat(chat_agent, df):

    st.header("💬 Chat With Your Data")

    question = st.chat_input("Ask any question about your dataset...")

    if not question:
        return

    with st.spinner("Analyzing your data..."):

        response = chat_agent.ask(df, question)

    # ----------------------------
    # Error
    # ----------------------------

    if not response["success"]:

        st.error(response["error"])

        if "code" in response:
            with st.expander("🐍 Generated Pandas Code"):
                st.code(response["code"], language="python")

        return

    # ----------------------------
    # Insight Response
    # ----------------------------

    if response.get("type") == "insight":

        st.success("🧠 AI Business Insight")

        st.markdown(response["result"])

        return

    # ----------------------------
    # Query Response
    # ----------------------------

    st.success("✅ Analysis Completed")

    if "code" in response:

        with st.expander("🐍 Generated Pandas Code"):
            st.code(response["code"], language="python")

    st.subheader("📊 Result")

    result = response["result"]

    if isinstance(result, pd.DataFrame):
        st.dataframe(result, use_container_width=True)

    elif isinstance(result, pd.Series):
        st.dataframe(result.to_frame())

    else:
        st.write(result)