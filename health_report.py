# health_report.py
import pandas as pd

class HealthReport:
    def __init__(self, health_report):
        self.health_report = health_report

    def display_health_report(self):
        """
        Display the health report in a structured format.
        """
        import streamlit as st
        st.title("Your Personalized Health Report 📄")
        
        # Display Potential Diseases
        st.subheader("Potential Diseases")
        if self.health_report.get("potential_diseases"):
            for disease in self.health_report["potential_diseases"]:
                st.write(f"- {disease}")
        else:
            st.write("No diseases identified.")
        
        # Display Recommended Medications in a structured table
        st.subheader("Recommended Medications")
        if self.health_report.get("recommended_medications"):
            medication_data = []
            for disease, medications in self.health_report["recommended_medications"].items():
                medication_data.append([disease, ", ".join(medications)])

            # Create a Pandas DataFrame to remove the index
            df_medications = pd.DataFrame(medication_data, columns=["Disease", "Medications"])

            # Display the table without the index
            st.table(df_medications.set_index('Disease'))  # Remove the index column by setting it as part of the data
        else:
            st.write("No medications recommended.")
        
        # Display Medical Recommendations
        st.subheader("Medical Recommendations")
        if self.health_report.get("medical_recommendations"):
            for recommendation in self.health_report["medical_recommendations"]:
                st.write(f"- {recommendation}")
        else:
            st.write("No specific medical recommendations provided.")

        # Display Suggested Doctors
        st.subheader("Suggested Doctors")
        if self.health_report.get("suggested_doctors"):
            for doctor in self.health_report["suggested_doctors"]:
                st.write(f"- {doctor}")
        else:
            st.write("No specific doctor recommendations.")
