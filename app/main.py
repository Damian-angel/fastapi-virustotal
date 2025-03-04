from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import requests
import os
import time
from dotenv import load_dotenv
from app.utils import scan_file_with_virustotal, get_virustotal_report

# Load environment variables
load_dotenv()

app = FastAPI()

VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
VIRUSTOTAL_SCAN_URL = "https://www.virustotal.com/vtapi/v2/file/scan"
VIRUSTOTAL_REPORT_URL = "https://www.virustotal.com/vtapi/v2/file/report"

@app.post("/scan-file/")
async def scan_file(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded")

    try:
        #Scan the file with VirusTotal
        scan_result = scan_file_with_virustotal(file, VIRUSTOTAL_API_KEY, VIRUSTOTAL_SCAN_URL)
        resource = scan_result.get("resource")  # Get the resource ID

        if not resource:
            raise HTTPException(status_code=500, detail="Failed to get resource ID from VirusTotal")

        # retry until the report is ready
        max_retries = 5
        retry_delay = 10  
        report_result = None

        for _ in range(max_retries):
            time.sleep(retry_delay)
            report_result = get_virustotal_report(resource, VIRUSTOTAL_API_KEY, VIRUSTOTAL_REPORT_URL)
            if report_result.get("response_code") == 1:  # Report is ready
                break
        else:
            raise HTTPException(status_code=500, detail="Report not ready after multiple retries")

        # Return the results
        return JSONResponse(content={
            "scan_result": scan_result,
            "report_result": report_result
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))