from virustotal_python import Virustotal
import requests
import json
import os
import time

class antiVirus:
    def __init__(self, api_key):
        self.api_key = api_key
        self.vtotal = Virustotal(API_KEY = api_key)

    def get_files(self, file_path):
        items = os.listdir(file_path)
        for item in items:
            full_path = os.path.join(file_path, item)
            if os.path.isdir(full_path):
                self.get_files(full_path)
            else:
                malicious, suspicious = self.upload_file(full_path)
                print(f"File: {full_path} | Malicious: {malicious} | Suspicious: {suspicious}")

    def upload_file(self, file_path):
        try:
            with open(file_path, "rb") as file:
                resp = self.vtotal.request("files", files={"file": file}, method="POST")
                analysis_id = resp.json()["data"]["id"]
                print(f"{file_path} file uploaded. Analysis ID: {analysis_id}")

                analysis_result = self.get_analysis(analysis_id)
                stats = analysis_result["data"]["attributes"]["stats"]
                malicious = stats.get("malicious", 0)
                suspicious = stats.get("suspicious", 0)
                return malicious, suspicious
        except Exception as e:
            print(f"Error uploading {file_path}: {e}")
            return None, None

    def get_analysis(self, analysis_id, max_retries = 15):
        retries = 0
        while retries < max_retries:
            try:
                resp = self.vtotal.request(f"analyses/{analysis_id}", method="GET")
                data = resp.json()
                status = data["data"]["attributes"]["status"]
                if status == "completed":
                    return data
                else:
                    print("Analysis not ready yet, waiting 5 seconds...")
                    time.sleep(5)
                    retries += 1
            except Exception as e:
                print(f"Error retrieving analysis {analysis_id}: {e}")
                time.sleep(5)
                retries += 1
        print("Reached max retries, stopping wait.")
        return None


