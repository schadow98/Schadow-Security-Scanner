import logging
import json

from DependencyScanner.RequirmentsFile import RequirementsFile
from DependencyScanner.Sonatype import Sonatype
from DependencyScanner.Synk import Synk
from DependencyScanner.Vulnerability import Vulnerability

class DependencyScanner(object):
    def __init__(self, workingDir: str, requirementsFilePath: str = None, dbs: list[str] = ["Sonatype"], vulnerabilityFilter: dict={}) -> list[Vulnerability]:
        self.workingDir             = workingDir
        self.requirementsFilePath   = requirementsFilePath
        self.dbs                    = dbs
        self.vulnerabilityFilter    = vulnerabilityFilter
        logging.info("DependencyScanner " + json.dumps(self.__dict__, indent=2))

        self.requirementsFile   = RequirementsFile(workingDir, requirementsFilePath)

        self.vulnerarbilities = []
        self.getVulnerarbilities()
        self.optionalFilterDependencies()
        self.printVulnerarbilities()
        
    def printVulnerarbilities(self)-> None:
        for vulnerability in self.vulnerarbilities:
            logging.error(json.dumps(vulnerability.__dict__, indent=2))


    def getVulnerarbilities(self) -> None:
        if len(self.dbs) == 0:
            raise Exception("No db defined to check for vulnerability")

        for db in self.dbs:
            db = db.lower()
            api = None
            if db == "sonatype":
                api = Sonatype()
            elif db =="sonatype":
                api = Synk()
            else:
                logging.warn(f"Skipping db becouse not defined: {db}")
                continue
            self.vulnerarbilities += api.checkDependecies(self.requirementsFile.getDependencies())


    def optionalFilterDependencies(self) -> None:
        if len(self.vulnerabilityFilter.keys()) == 0: return

        if "cvssScore" in self.vulnerabilityFilter:
            if isinstance(self.vulnerabilityFilter["cvssScore"], str):
                self.vulnerabilityFilter["cvssScore"] = {
                    "none": 0,
                    "low": 0.1,
                    "medium": 4,
                    "high": 7,
                    "critical": 9
                }.get(self.vulnerabilityFilter["cvssScore"].lower(), None)

                if self.vulnerabilityFilter["cvssScore"] is None:
                    logging.warn("No valid filter for cvssScore defined - set to 0")
                    self.vulnerabilityFilter["cvssScore"] = 0


        def checkVulnerability(vulnerability):
            for key, value in self.vulnerabilityFilter.items():
                
                if isinstance(value, float) or isinstance(value, int) :
                    if value < getattr(vulnerability, key):
                        continue
                    else:
                        return False

                if not value in getattr(vulnerability, key):
                    return False

            return True

        self.vulnerarbilities = list(filter(checkVulnerability, self.vulnerarbilities))

