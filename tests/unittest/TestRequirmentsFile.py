
import loadModules
import os
from DependencyScanner.RequirementsFile import RequirementsFile
from DependencyScanner.Dependency import Dependency
import unittest

expectedDependencies = [
    Dependency("python_dotenv", "1.0.1"),
    Dependency("requests", "2.32.3"),
    Dependency("robotframework", "7.0.1"),
    Dependency("irgendwas", "1.0.1", "http")
]

class TestRequirementsFile(unittest.TestCase):

    def test_findAndParseRequirmentsFile(self):
        """Find a requrimentesFile with all combinations of dependencies

            combinations of dependencies :
            name
            name & version
            name & version & extra
        """
        workingDir = os.path.join(os.environ["PROJECT_PATH"], "./tests/testdata/requirementsFile/found")
        requirementsFile = RequirementsFile(workingDir=workingDir)
        self.assertIsNotNone(requirementsFile)
        self.assertEqual(len(requirementsFile.dependencies), 4)
        self.assertListEqual(requirementsFile.dependencies, expectedDependencies)

    def test_parseRequirmentsFile(self):
        workingDir = os.path.join(os.environ["PROJECT_PATH"], "./tests/testdata/requirementsFile/found")
        requirementsFilePath = os.path.join(os.environ["PROJECT_PATH"], "./tests/testdata/requirementsFile/found/requirements.txt")
        requirementsFile = RequirementsFile(workingDir=workingDir, requirementsFilePath=requirementsFilePath)
        self.assertIsNotNone(requirementsFile)
        self.assertEqual(len(requirementsFile.dependencies), 4)
        self.assertListEqual(requirementsFile.dependencies, expectedDependencies)


    def test_noRequirmentsFileFound(self):
        

        with self.assertRaises(Exception) as context:
            workingDir = os.path.join(os.environ["PROJECT_PATH"], "./tests/testdata/requirementsFile/noRequirementsFile")
            requirementsFile = RequirementsFile(workingDir=workingDir)
        
        # Optional: Überprüfen der Fehlermeldung
        self.assertEqual(str(context.exception), "No requirementsFile in projectDir found - disbale Dependency Checker if no dependencys get used")

if __name__ == "__main__":
  unittest.main()

