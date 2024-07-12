import logging
import json

from BaseScanner import BaseScanner
from DependencyScanner.RequirementsFile import RequirementsFile
from DependencyScanner.Sonatype import Sonatype
from DependencyScanner.Synk import Synk
from DependencyScanner.DependencyVulnerability import DependencyVulnerability

class DependencyScanner(BaseScanner):
    """
    DependencyScanner class is the main class to analyze the dependencies and search in security dbs for vulnerabilities

    Args:
            workingDir (str): The working directory where the scanner will operate. Default is the current directory.
            requirementsFilePath (str): path of the requirementsFile
            dbs list[str]: string for which security dbs get searched
    """
    def __init__(self, workingDir: str, requirementsFilePath: str = None, dbs: list[str] = ["Sonatype"], vulnerabilityFilter: dict={}) -> list[DependencyVulnerability]:
        self.name = self.__class__.__name__
        self.workingDir             = workingDir
        self.requirementsFilePath   = requirementsFilePath
        self.dbs                    = dbs
        self.vulnerabilityFilter    = vulnerabilityFilter
        logging.info("DependencyScanner " + json.dumps(self.__dict__, indent=2))

        self.requirementsFile   = RequirementsFile(workingDir, requirementsFilePath)

        self.vulnerarbilities = []
        self.getVulnerarbilities()
        self.optionalFilterVulterabilites()
        self.printVulnerarbilities()
        


    # initializes the restapi call to the security dbs
    def getVulnerarbilities(self) -> None:
        if len(self.dbs) == 0:
            raise Exception("No db defined to check for vulnerability")

        for db in self.dbs:
            db = db.lower()
            api = None
            if db == "sonatype":
                api = Sonatype()
            elif db =="synk":
                api = Synk()
            else:
                logging.warn(f"Skipping db becouse not defined: {db}")
                continue
            self.vulnerarbilities += api.checkDependecies(self.requirementsFile.getDependencies())

    # filters the founded vulterabilites - for cvssScore = high -> only vulterabilites with higher cvssScore of 7 gets printed
    def optionalFilterVulterabilites(self) -> None:
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

        # function to calculate the boolean for the filter
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

