import requests
import os

API_URL = "http://127.0.0.1:8000/analyze"
PDF_FILE_PATH = "Data/blood_test_report.pdf"

def test_upload():
    if not os.path.exists(PDF_FILE_PATH):
        print(f"❌ Error: File not found at {PDF_FILE_PATH}")
        return

    print(f"Uploading {PDF_FILE_PATH} to {API_URL}")

    try:
        with open(PDF_FILE_PATH, 'rb') as f:
            files = {'file': (os.path.basename(PDF_FILE_PATH), f, 'application/pdf')}
            data = {'query': 'Summarise my Blood Test Report'}
            response = requests.post(API_URL, files=files, data=data)

        response.raise_for_status()
        print("✅ Success")
        print("📄 Response JSON:")
        print(response.json())

    except requests.exceptions.HTTPError as e:
        print(f"❌ Request failed: {e}")
        print(response.text)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    test_upload()
