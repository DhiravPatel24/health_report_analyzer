# groq_service.py
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import json
import config

class GroqService:
    def __init__(self):
        self.llm = ChatGroq(
            groq_api_key=config.GROQ_API_KEY,
            model=config.MODEL,
            temperature=0.2,
        )
        
    def extract_health_data(self, page_data):
        """
        Extract health data by sending the page text to Groq model.
        """
        prompt_extract_health_with_meds = PromptTemplate.from_template(
        """
        ### SCRAPED TEXT FROM HEALTH REPORT:
        {page_data}
        
        ### INSTRUCTION:
        The scraped text is from a health report. Your job is to:
        1. Extract the potential diseases or conditions based on the symptoms or test results mentioned.
        2. For each disease or condition, recommend possible medications along with the dosage if available.
        3. For each test result mentioned, indicate whether it is within the normal range, overvalued, or undervalued, and provide an explanation of the potential problems or health issues caused by abnormal values.
        4. Link each disease (if any) to the test results: if a test result indicates that the person has a certain disease (e.g., high cholesterol indicating risk for cardiovascular diseases), mark that disease as "confirmed" based on the test and explain why, referencing the test value and its implication.
        5. Suggest possible medical actions, lifestyle changes, and doctors that could help based on the extracted data.
        6. Return the information in a JSON format containing the following keys:
            - `potential_diseases` (list of potential diseases or conditions),
            - `recommended_medications` (a dictionary with diseases as keys and lists of medications as values),
            - `test_results` (list of dictionaries with each test result, its value, reference range, interpretation, and potential implications),
            - `medical_recommendations` (list of recommended actions or treatments),
            - `suggested_doctors` (types of doctors or specialties that might help),
            - `confirmed_diseases` (list of diseases that are confirmed based on test results, including the test value and the reasoning behind the confirmation).
        
        Only return the valid JSON.
        ### VALID JSON (NO PREAMBLE):    
        """
        )
        
        chain_extract_health_with_meds = prompt_extract_health_with_meds | self.llm
        res_health_with_meds = chain_extract_health_with_meds.invoke(input={'page_data': page_data})
        health_report_analysis_with_meds = res_health_with_meds.content
        try:
            start_index = health_report_analysis_with_meds.find("{")
            end_index = health_report_analysis_with_meds.rfind("}") + 1
            json_string = health_report_analysis_with_meds[start_index:end_index]
            health_report = json.loads(json_string)
            return health_report
        except json.JSONDecodeError as e:
            return {"error": f"Error decoding JSON: {e}"}
