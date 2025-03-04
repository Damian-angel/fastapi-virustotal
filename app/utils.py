import requests

def scan_file_with_virustotal(file, api_key, scan_url): # sacan the file in the api
    
    try:
        files = {"file": (file.filename, file.file, file.content_type)}
        params = {"apikey": api_key}
        response = requests.post(scan_url, files=files, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error scanning file with VirusTotal: {e}")

def get_virustotal_report(resource, api_key, report_url): #return the report 
   
    try:
        params = {"apikey": api_key, "resource": resource}
        response = requests.get(report_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error retrieving report from VirusTotal: {e}")