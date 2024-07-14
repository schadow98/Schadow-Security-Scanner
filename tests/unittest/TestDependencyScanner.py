import loadModules
import unittest
import os
from DependencyScanner.DependencyScanner import DependencyScanner
from DependencyScanner.DependencyVulnerability import DependencyVulnerability
from DependencyScanner.Dependency import Dependency
from testdata.vulnerarbilities.expectedVulnerarbilities import expectedVulnerarbilities


class DependencyScanner(DependencyScanner):
    def getVulnerarbilities(self) -> None:
            self.vulnerarbilities += expectedVulnerarbilities
    def printVulnerarbilities(self) -> None:
        pass

class TestDependencyScanner(unittest.TestCase):

    def test_DependencyScannerWithoutFilter(self):
        """Find a requrimentesFile with all combinations of dependencies

            combinations of dependencies :
            name
            name & version
            name & version & extra
        """
        workingDir = os.path.join(os.environ["PROJECT_PATH"], "./tests/testdata/requirementsFile/found")
        dependencyScanner = DependencyScanner(workingDir=workingDir)
        self.assertIsNotNone(dependencyScanner)
        self.assertEqual(len(dependencyScanner.vulnerarbilities), 6)
        
        self.assertListEqual(dependencyScanner.vulnerarbilities, expectedVulnerarbilities)

    def test_DependencyScannerWithFilterCvssScore(self):
        workingDir = os.path.join(os.environ["PROJECT_PATH"], "./tests/testdata/requirementsFile/found")
        requirementsFilePath = os.path.join(os.environ["PROJECT_PATH"], "./tests/testdata/requirementsFile/found/requirements.txt")
        vulnerabilityFilter = {
          "cvssScore": "high",
          "cvssVector": ""
        }
        dependencyScanner = DependencyScanner(workingDir=workingDir, requirementsFilePath=requirementsFilePath, vulnerabilityFilter=vulnerabilityFilter)
        self.assertIsNotNone(dependencyScanner)
        self.assertEqual(len(dependencyScanner.vulnerarbilities), 1)

        
        expectedVulnerarbilitiesFiltered = list(filter(lambda x: x.id == "CVE-2018-18074", expectedVulnerarbilities))

        self.assertListEqual(dependencyScanner.vulnerarbilities, expectedVulnerarbilitiesFiltered)

    def test_DependencyScannerWithFilterCvssVector(self):
        workingDir = os.path.join(os.environ["PROJECT_PATH"], "./tests/testdata/requirementsFile/found")
        requirementsFilePath = os.path.join(os.environ["PROJECT_PATH"], "./tests/testdata/requirementsFile/found/requirements.txt")
        vulnerabilityFilter = {
          "cvssVector": "A:P"
        }
        dependencyScanner = DependencyScanner(workingDir=workingDir, requirementsFilePath=requirementsFilePath, vulnerabilityFilter=vulnerabilityFilter)
        self.assertIsNotNone(dependencyScanner)
        self.assertEqual(len(dependencyScanner.vulnerarbilities), 1)

        expectedVulnerarbilitiesFiltered = list(filter(lambda x: x.id == "CVE-2013-2099", expectedVulnerarbilities))


        self.assertListEqual(dependencyScanner.vulnerarbilities, expectedVulnerarbilitiesFiltered)

    def test_DependencyScannerWithFilterCvssVectorAndCvssVector(self):
        workingDir = os.path.join(os.environ["PROJECT_PATH"], "./tests/testdata/requirementsFile/found")
        requirementsFilePath = os.path.join(os.environ["PROJECT_PATH"], "./tests/testdata/requirementsFile/found/requirements.txt")
        vulnerabilityFilter = {
          "cvssScore": "medium",
          "cvssVector": "A:P"
        }
        dependencyScanner = DependencyScanner(workingDir=workingDir, requirementsFilePath=requirementsFilePath, vulnerabilityFilter=vulnerabilityFilter)
        self.assertIsNotNone(dependencyScanner)
        self.assertEqual(len(dependencyScanner.vulnerarbilities), 1)
        expectedVulnerarbilitiesFiltered = list(filter(lambda x: x.id == "CVE-2013-2099", expectedVulnerarbilities))


        self.assertListEqual(dependencyScanner.vulnerarbilities, expectedVulnerarbilitiesFiltered)

if __name__ == "__main__":
  unittest.main()
