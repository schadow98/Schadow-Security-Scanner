import logging
import json

from DependencyScanner.RequirmentsFile import RequirementsFile
from DependencyScanner.Sonatype import Sonatype
from DependencyScanner.Vulnerability import Vulnerability

class DependencyScanner(object):
    def __init__(self, workingDir: str, requirementsFilePath: str = None) -> list[Vulnerability]:
        self.workingDir             = workingDir
        self.requirementsFilePath   = requirementsFilePath
        logging.info("DependencyScanner " + json.dumps(self.__dict__, indent=2))

        self.requirementsFile   = RequirementsFile(workingDir, requirementsFilePath)
        self.sonatypeApi        = Sonatype()

        self.vulnerarbilities = self.sonatypeApi.checkDependecies(self.requirementsFile.getDependencies())
        print(self.vulnerarbilities)