import logging
import os
import re
import json

from DependencyScanner.Dependency import Dependency

class RequirementsFile(object):
    def __init__(self, workingDir: str, requirementsFilePath: str = None) -> None:
        self.workingDir             = workingDir
        self.requirementsFilePath   = requirementsFilePath
        self.dependencies           = []

        logging.info("RequirementsFile " + json.dumps(self.__dict__, indent=2))
        if not self.requirementsFilePath:
            self.findRequirementsFile()

        self.parseRequirementsFile()

    def __str__(self) -> str:
        return f"RequirementsFile {self.requirementsFilePath} - Dependencies[{len(self.dependencies)}]"
    
    
    def printDependencies(self) -> None:
        for dependency in self.dependencies:
            logging.info(dependency)
        
    def getDependencies(self) -> list[Dependency]:
        return self.dependencies

    def parseRequirementsFile(self) -> list[Dependency]:
        self.dependencies = []
        with open(self.requirementsFilePath) as f:
            for line in f:
                if not line or "==" not in line or line.startswith('#'):
                    continue
                
                seperator = None
                if "==" in line:
                    seperator = "=="
                elif ">=" in line:
                    seperator = ">="
                elif "~=" in line:
                    seperator = "~="
                else:
                    seperator = "None"       
                
                name, version = line.split(seperator)
                version = version.split("[")[0]
                extras = re.findall(r"\[(.*?)\]", line)
                if len(extras) > 0:
                    extras = extras[0]
                else:
                    extras = None
                self.dependencies.append(Dependency(name, version, extras))

        if len(self.dependencies) <=0:
            raise Exception(f"No dependencies defined in {self.requirementsFilePath}")
        
        for dependency in self.dependencies:
            logging.info(str(dependency))
     

    def findRequirementsFile(self) -> str:
        # List all files in the directory
        files = []
        for root, _, filenames in os.walk(self.workingDir):
            for filename in filenames:
                files.append(os.path.join(root, filename))

        # Filter files containing 'requirements' in their names

        for file in files:
            if re.search(r'requirements.txt', file, re.IGNORECASE):
                logging.info("Found an set requirementsFile: " + file)
                self.requirementsFilePath = file
                return

        for file in files:
            if re.search(r'requirements', file, re.IGNORECASE):
                logging.info("Found an set requirementsFile: " + file)
                self.requirementsFilePath = file
                return

        # if not throw Error
        raise Exception("No requirementsFile in projectDir found - disbale Dependency Checker if no dependencys get used")