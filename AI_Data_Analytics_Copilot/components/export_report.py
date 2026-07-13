import streamlit as st
from services.pdf_service import PDFService


def show_export(
    dataset_name,
    df,
    profile,
    insights,
    measures
):

    st.header("📥 Export Report")

    if st.button("📄 Generate AI PDF Report"):

        pdf = PDFService()

        file = pdf.generate(
            filename="AI_Data_Report.pdf",
            dataset_name=dataset_name,
            df=df,
            profile=profile,
            insights=insights,
            dax=measures
        )

        with open(file, "rb") as f:

            st.download_button(
                label="⬇ Download PDF",
                data=f,
                file_name="AI_Data_Report.pdf",
                mime="application/pdf"
            )