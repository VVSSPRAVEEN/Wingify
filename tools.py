from langchain_community.document_loaders import PyMuPDFLoader
from crewai_tools import tool

import fitz  # PyMuPDF
import os


class BloodTestReportTool:
    @tool("Extract text from a PDF blood test report")
    def extract_text_from_pdf(file_path: str) -> str:
        """
        Extracts text from a PDF file located at the given file path using PyMuPDF.
        Returns the plain text content of the PDF.
        """
        try:
            doc = fitz.open(file_path)
            text = ""
            for page in doc:
                text += page.get_text()
            doc.close()
            return text
        except Exception as e:
            return f"Error reading PDF: {str(e)}"


class NutritionTool:
    @tool("Analyze blood report for nutritional advice")
    def analyze_nutrition(report: str) -> str:
        """
        Analyzes the blood test report and returns nutritional advice
        based on deficiencies and abnormalities in the report.
        """
        if "Vitamin D" in report:
            return "Consider increasing your Vitamin D intake."
        return "No specific nutritional issues found."


class ExerciseTool:
    @tool("Recommend exercises based on blood report")
    def recommend_exercise(report: str) -> str:
        """
        Provides exercise recommendations based on markers found in the blood report.
        """
        if "cholesterol" in report.lower():
            return "Include more cardio exercises like walking, jogging, or swimming."
        return "Maintain a balanced exercise routine."


class VerificationTool:
    @tool("Verify if the blood report is complete")
    def verify_report(report: str) -> str:
        """
        Verifies whether the report includes key components like Hemoglobin, WBC count, etc.
        """
        required_markers = ["Hemoglobin", "WBC", "Platelets"]
        missing = [marker for marker in required_markers if marker not in report]
        if missing:
            return f"The report is missing: {', '.join(missing)}"
        return "The blood report appears to be complete."
