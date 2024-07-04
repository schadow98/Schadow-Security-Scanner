import os
import json
import logging

import requests

from DependencyScanner.Dependency import Dependency
from DependencyScanner.Vulnerability import Vulnerability

class SynkAPI(object):
    def __init__(self) -> None:
        self.synkAuthToken = os.getenv("SYNK_AUTH_TOKEN")
        if not self.synkAuthToken:
            raise Exception("No Environment Variable Set: SYNK_AUTH_TOKEN - maybe create .env-File or configurate Pipeline")
        self.organizationId = os.getenv("ORGANIZATION_ID")
        if not self.organizationId:
            raise Exception("No Environment Variable Set: ORGANIZATION_ID - maybe create .env-File or configurate Pipeline")
        self.snykApiUrl = 'https://snyk.io/api/v1/test/pip'
        logging.info("SynkAPI " + json.dumps(self.__dict__(), indent=2))

    def __dict__(self) -> dict:
        return {
          "synkAuthToken": "************************************",
          "organizationId": "************************************",
          "snykApiUrl": "https://snyk.io/api/v1/test/npm"
        }

    def checkDependecies(self, dependencies: list[Dependency]) -> list[Vulnerability]:

        headers = {
            'Authorization': f'token {self.synkAuthToken}',
            'Content-Type': 'application/json'
        }
        data = {
            'dependencies': {dep.name : dep.version for dep in dependencies}
        }
        response = requests.post(self.snykApiUrl, headers=headers, json=data)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Fehler bei der API-Anfrage: {response.status_code}, {response.text}")
