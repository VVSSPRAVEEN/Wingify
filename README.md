# Blood Test Report Analyzer

This project is a web API that helps you analyze blood test reports using AI. You upload a PDF file (your blood report), and the system will return insights like health suggestions, nutrition advice, exercise plans, and report verification — just like a real medical assistant.

We’ve used a tool called CrewAI to build different virtual experts (called agents), each with their own job, like doctor, nutritionist, or exercise expert.

---

## What this project does

- Lets you upload your blood test PDF report
- Uses AI to understand and analyze the content
- Returns a report summary with health advice
- Runs everything through a FastAPI web server

---

## Setup and How to Run

These are the steps you need to follow to get the project working on your own computer.

### Step 1: Clone the project

You can download this project using Git.

```bash
git clone https://github.com/your-username/blood-report-analyzer.git
cd blood-report-analyzer


Step 2: Create virtual environment
Virtual environment helps keep your dependencies separate from other projects.

bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate       # On Windows use: .venv\Scripts\activate
Step 3: Install requirements
This installs all the libraries needed for this project.

bash
Copy
Edit
pip install -r requirements.txt
Step 4: Run the API server
Start the backend server using this command.

bash
Copy
Edit
uvicorn main:app --reload
If successful, you’ll see that the server is running at:
http://127.0.0.1:8000

You can open the browser and visit:
http://127.0.0.1:8000/docs
This gives you a simple interface to test your API.

API Endpoints
GET /
This is a simple test endpoint.
It just tells you the server is working.

Response example:

json
Copy
Edit
{
  "message": "Blood Test Report Analyser API is running"
}
POST /analyze
This is the main endpoint that you will use to upload your blood report for analysis.

Input (Form Fields):

file: The PDF report file to upload.

query (optional): A question or prompt like "Summarize my report".

How to test:

You can use Postman or run this command in your terminal:

bash
Copy
Edit
curl -X POST http://127.0.0.1:8000/analyze \
  -F "file=@data/sample.pdf" \
  -F "query=Summarize my blood report"
Output (JSON):

json
Copy
Edit
{
  "status": "success",
  "query": "Summarize my blood report",
  "analysis": "Your Hemoglobin levels are normal. Vitamin D levels are low. Consider more sun exposure or supplements.",
  "file_processed": "sample.pdf"
}
Bugs Found and How I Fixed Them
Here’s a list of problems I found in the original code and what I did to fix them:

Bug 1: Wrong import for tool
Problem:
The code was trying to import tool using from crewai_tools.tool import tool which gave an error.

Fix:
Changed it to: from crewai.tools import tool

Bug 2: Missing PyMuPDF import
Problem:
fitz (used for reading PDF) was not working correctly.

Fix:
Made sure PyMuPDF was installed using pip install PyMuPDF and confirmed that import fitz works.

Bug 3: Wrong API path in test script
Problem:
The test script test_api.py was using an endpoint /analyze-report that did not exist.

Fix:
Changed the path to /analyze, which matches the actual endpoint in FastAPI.

Bug 4: 500 Internal Server Error
Problem:
There were many small issues like using tools incorrectly or forgetting docstrings in some functions.

Fix:
Added required docstrings to each tool function. Also added proper try-except handling and logging to understand any errors.

Bug 5: tool decorator not found
Problem:
Tool decorators were being imported incorrectly or used from the wrong path.

Fix:
Fixed the import to match CrewAI’s latest structure and checked against official documentation.