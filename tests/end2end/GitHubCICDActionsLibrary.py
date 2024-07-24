import datetime
import time
from robot.api.logger import warn, info, debug, trace, console
import os
import requests
import json
import platform
import uuid
import dotenv
if platform.system() == "Windows":
    info("load .env variables")
    dotenv.load_dotenv(".env")

class GitHubCICDActionsLibrary:
    '''
    
    '''
    def __init__(self):
        self.owner = 'schadow98'
        self.repo = 'SecurityScannerTest'

        self.baseUrl = f'https://api.github.com/repos/{self.owner}/{self.repo}'

    def getHeaders(self):
        github_token = os.getenv('GITHUB_TOKEN')
        if not github_token:
            raise ValueError("Please set the environmentvariable 'GITHUB_TOKEN'.")

        return {
            "Authorization": f"token {github_token}",
            "Accept": "application/vnd.github.v3+json"
        } 

    def trigger_workflow(self, workflow_id):
        self.workflow_id = workflow_id
        url = self.baseUrl + f'/actions/workflows/{self.workflow_id}/dispatches'
        info("url " + url)

        self.run_identifier = str(uuid.uuid4())

        payload = {
            "ref": "main",
            "inputs":{
                "distinct_id": self.run_identifier
            }
        }
        info(payload)
                 
        response = requests.post(url, headers=self.getHeaders(), data=json.dumps(payload))

        if response.status_code == 204:
            info("Workflow successfully triggered")
            info(response.text)
        else:
            error_msg = f"Error while triggering pipeline: {response.status_code}"
            warn(error_msg)
            warn(response.text)
            raise Exception(error_msg)
        
    def checkNameOfRun(self, run):
        return self.run_identifier in run.get("display_title")

    def check_status(self):
        time.sleep(10)
        info(self.workflow_id)
        url = self.baseUrl + f'/actions/runs?created=>{self.getTimeStampXMinInPast(2)}'
        status = "pending"
        counter = 0
        finalRun = None
        while status in ["waiting", "pending", "in_progress"] and counter < 10:
            response = requests.get(url, headers=self.getHeaders())
            if response.status_code >= 400: raise Exception("Error while calling api"+ str(response) )
            runs = list(filter(self.checkNameOfRun, response.json().get("workflow_runs")))
            if len(runs) > 0:
                finalRun = runs[0]
                status = runs[0]["status"]
                info(f"counter {counter} - status {status}")
                
            time.sleep(10)
            counter += 1
        
        info(finalRun)
        
        if status != "completed":
            raise Exception("Run doenst complete")
        
        if finalRun["conclusion"] == "success":
            return True
        elif finalRun["conclusion"] == "failure":
            raise Exception("Workflow failed")
        else:
            raise Exception("workflow unexpected ended")
            


    def getTimeStampXMinInPast(self, x=5):
        current_time = datetime.datetime.now(datetime.UTC)
        time_in_past = current_time - datetime.timedelta(minutes=x)
        return time_in_past.strftime('%Y-%m-%dT%H:%M:%S')