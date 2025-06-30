from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid
from dotenv import load_dotenv

from crewai import Crew, Process
from agents import doctor, verifier, nutritionist, exercise_specialist
from tasks import help_patients, nutrition_analysis, exercise_planning, verification_task
from tools import BloodTestReportTool

load_dotenv()

app = FastAPI(title="Blood Test Report Analyser")


def run_crew(query: str, file_path: str = "data/sample.pdf"):
    class CustomBloodTool(BloodTestReportTool):
        def read_data_tool(path=file_path):
            return BloodTestReportTool.read_data_tool(path)

    doctor.tools = [CustomBloodTool]
    verifier.tools = [CustomBloodTool]
    nutritionist.tools = [CustomBloodTool]
    exercise_specialist.tools = [CustomBloodTool]

    medical_crew = Crew(
        agents=[verifier, doctor, nutritionist, exercise_specialist],
        tasks=[verification_task, help_patients, nutrition_analysis, exercise_planning],
        process=Process.sequential
    )

    return medical_crew.kickoff(inputs={'query': query})


@app.get("/")
async def root():
    return {"message": "Blood Test Report Analyser API is running"}


@app.post("/analyze")
async def analyze_blood_report(
    file: UploadFile = File(...),
    query: str = Form(default="Summarise my Blood Test Report")
):
    file_id = str(uuid.uuid4())
    file_path = f"data/blood_test_report_{file_id}.pdf"

    try:
        os.makedirs("data", exist_ok=True)

        with open(file_path, "wb") as f:
            f.write(await file.read())

        if not query.strip():
            query = "Summarise my Blood Test Report"

        response = run_crew(query=query.strip(), file_path=file_path)

        return {
            "status": "success",
            "query": query,
            "analysis": str(response),
            "file_processed": file.filename
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing blood report: {str(e)}")

    finally:
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except:
            pass
