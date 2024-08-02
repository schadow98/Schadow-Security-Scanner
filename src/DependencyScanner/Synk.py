import os
import json
import logging

import requests

from DependencyScanner.Dependency import Dependency
from DependencyScanner.DependencyVulnerability import DependencyVulnerability

class Synk(object):
    """
    Synk class checks the dependency in the synk security database
    It needs a payment -> and then environmentvariables of the account need to set
    """
    def __init__(self) -> None:
        self.synkAuthToken: str = os.getenv("SYNK_AUTH_TOKEN")
        if not self.synkAuthToken:
            raise Exception("No Environment Variable Set: SYNK_AUTH_TOKEN - maybe create .env-File or configurate Pipeline")
        self.organizationId: str = os.getenv("ORGANIZATION_ID")
        if not self.organizationId:
            raise Exception("No Environment Variable Set: ORGANIZATION_ID - maybe create .env-File or configurate Pipeline")
        self.snykApiUrl: str = 'https://snyk.io/api/v1/test/pip'
        logging.info("Synk " + json.dumps(self.__dict__(), indent=2))

    def __dict__(self) -> dict:
        return {
          "synkAuthToken": "************************************",
          "organizationId": "************************************",
          "snykApiUrl": "https://snyk.io/api/v1/test/npm"
        }

    def checkDependecies(self, dependencies: list[Dependency]) -> list[DependencyVulnerability]:

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
