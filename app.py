# app.py
import streamlit as st
from pdf_utils import extract_pdf_text
from groq_service import GroqService
from health_report import HealthReport

def create_streamlit_app():

    st.title("Health Report Analyzer 🩺")
    # Upload file input
    uploaded_file = st.file_uploader("Upload Health Report PDF", type="pdf")

    # When the user uploads a file and clicks on the submit button
    if uploaded_file is not None:
        if st.button("Analyze Report"):
            # Extract text from the PDF
            page_data = extract_pdf_text(uploaded_file)
            
            # Extract health data from Groq model
            groq_service = GroqService()
            health_report = groq_service.extract_health_data(page_data)
            
            # If Groq model returned an error
            if "error" in health_report:
                st.error(health_report["error"])
            else:
                # Display the health report
                health_report_obj = HealthReport(health_report)
                health_report_obj.display_health_report()

# Run the Streamlit app
if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Health Report Analyzer", page_icon="🩺")
    create_streamlit_app()
