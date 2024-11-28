import pandas as pd
import streamlit as st

class HealthReport:
    def __init__(self, health_report):
        self.health_report = health_report

    def display_health_report(self):
        """
        Display the health report in a structured format.
        """
        st.title("Your Personalized Health Report 📄")
        
        # Display Test Results first in a table format
        st.subheader("Test Results")
        if self.health_report.get("test_results"):
            test_results_data = []
            for test in self.health_report["test_results"]:
                test_name = test.get("test_name") or test.get("parameter")
                test_results_data.append([
                    test_name,
                    test.get("value"),
                    test.get("reference_range"),
                    test.get("interpretation"),
                    test.get("potential_implications")
                ])
            print(test_results_data)
            # Create a DataFrame for the test results
            df_test_results = pd.DataFrame(test_results_data, columns=[
                "Test Parameter", "Value", "Reference Range", "Interpretation", "Potential Implications"
            ])

            # Display the test results table
            st.table(df_test_results)
        else:
            st.write("No test results provided.")
        
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


        st.subheader("Confirmed Diseases Based on Test Results")
        if self.health_report.get("confirmed_diseases"):
            for disease_info in self.health_report["confirmed_diseases"]:
                st.write(f"**{disease_info['disease']}**")
                st.write(f"Test Value: {disease_info.get('test_value', 'N/A')}")
                if(disease_info.get('reference_range')):
                    st.write(f"Reference Range: {disease_info.get('reference_range', 'N/A')}")
                st.write(f"Reasoning: {disease_info['reasoning']}")
        else:
            st.write("No diseases have been confirmed based on the test results.")