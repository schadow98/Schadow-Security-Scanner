import unittest
import os
from argparse import Namespace

from DependencyScanner.DependencyVulnerability import DependencyVulnerability
from SASTScanner.SASTVulnerability import SASTVulnerability
from SecurityScanner import SecurityScanner

class TestSecurityScanner(unittest.TestCase):
    def testDisableScanner(self):
        workingDir = os.path.join(os.environ["PROJECT_PATH"], "tests/testdata/requirementsFile/found")
        namespace = Namespace(
            path=workingDir,
            disableDependenyScanner=True,
            disableInjectionScanner=True,
            disableSecretScanner=True,
            enableCustomScanner=False,
            requirementsFile="",
            configFile="",
            logLevel="WARNING"
        )
        securityScanner = SecurityScanner(namespace)
        self.assertEqual(len(securityScanner.scanners), 0)
        self.assertEqual(len(securityScanner.getVulnerabilities()), 0)
        self.assertIsNotNone(securityScanner.configFile)
        self.assertIsNotNone(securityScanner.config)
        self.assertIsInstance(securityScanner.config, dict)
        self.assertEqual(securityScanner.logLevel, namespace.logLevel)
        self.assertEqual(securityScanner.requirementsFile, namespace.requirementsFile)
        self.assertIsNotNone(securityScanner.requirementsFile)
        self.assertEqual(securityScanner.enableCustomScanner, namespace.enableCustomScanner)


    def testEnableCustomScanners(self):
        workingDir = os.path.join(os.environ["PROJECT_PATH"], "tests/testdata/xss")
        namespace = Namespace(
            path=workingDir,
            disableDependenyScanner=True,
            disableInjectionScanner=True,
            disableSecretScanner=True,
            enableCustomScanner=True,
            requirementsFile="",
            configFile="",
            logLevel="CRITICAL"
        )
        securityScanner = SecurityScanner(namespace)
        self.assertEqual(len(securityScanner.scanners), 1)
        self.assertIsNotNone(securityScanner.configFile)
        self.assertIsNotNone(securityScanner.config)
        self.assertIsInstance(securityScanner.config, dict)
        self.assertEqual(securityScanner.logLevel, namespace.logLevel)
        self.assertEqual(securityScanner.requirementsFile, namespace.requirementsFile)
        self.assertIsNotNone(securityScanner.requirementsFile)
        self.assertEqual(securityScanner.enableCustomScanner, namespace.enableCustomScanner)
        for item in securityScanner.getVulnerabilities():
            self.assertTrue(isinstance(item, SASTVulnerability))


    def testEnableAllScanners(self):
        workingDir = os.path.join(os.environ["PROJECT_PATH"], "tests/testdata/secretScanner")
        namespace = Namespace(
            path=workingDir,
            disableDependenyScanner=False,
            disableInjectionScanner=False,
            disableSecretScanner=False,
            enableCustomScanner=True,
            requirementsFile="",
            configFile="",
            logLevel="CRITICAL"
        )
        securityScanner = SecurityScanner(namespace)
        self.assertEqual(len(securityScanner.scanners), 4)
        self.assertIsNotNone(securityScanner.configFile)
        self.assertIsNotNone(securityScanner.config)
        self.assertIsInstance(securityScanner.config, dict)
        self.assertEqual(securityScanner.logLevel, namespace.logLevel)
        self.assertEqual(securityScanner.requirementsFile, namespace.requirementsFile)
        self.assertIsNotNone(securityScanner.requirementsFile)
        self.assertEqual(securityScanner.enableCustomScanner, namespace.enableCustomScanner)
        for item in securityScanner.getVulnerabilities():
            self.assertTrue(isinstance(item, SASTVulnerability) or isinstance(item, DependencyVulnerability))

    def testWrongConfigExpectException(self):
        workingDir = os.path.join(os.environ["PROJECT_PATH"], "tests/testdata/xss")
        namespace = Namespace(
            path=workingDir,
            disableDependenyScanner=False,
            disableInjectionScanner=True,
            disableSecretScanner=True,
            enableCustomScanner=False,
            requirementsFile="",
            configFile="",
            logLevel="CRITICAL"
        )
       
        with self.assertRaises(Exception) as context:
            securityScanner = SecurityScanner(namespace)
        self.assertEqual(str(context.exception), "No requirementsFile in projectDir found - disbale Dependency Checker if no dependencys get used")


    def testAnotherDirButWithRequirementsFilePath(self):
        workingDir = os.path.join(os.environ["PROJECT_PATH"], "tests/testdata/xss")
        namespace = Namespace(
            path=workingDir,
            disableDependenyScanner=False,
            disableInjectionScanner=True,
            disableSecretScanner=True,
            enableCustomScanner=False,
            requirementsFile=os.path.join(os.environ["PROJECT_PATH"], "tests/testdata/requirementsFile/found/requirements.txt"),
            configFile="",
            logLevel="CRITICAL"
        )
       

        securityScanner = SecurityScanner(namespace)
        self.assertEqual(len(securityScanner.scanners), 1) 
        self.assertIsNotNone(securityScanner.configFile)
        self.assertIsNotNone(securityScanner.config)
        self.assertIsInstance(securityScanner.config, dict)
        self.assertEqual(securityScanner.logLevel, namespace.logLevel)
        self.assertEqual(securityScanner.requirementsFile, namespace.requirementsFile)
        self.assertIsNotNone(securityScanner.requirementsFile)
        self.assertEqual(securityScanner.enableCustomScanner, namespace.enableCustomScanner)
        for item in securityScanner.getVulnerabilities():
            self.assertTrue(isinstance(item, SASTVulnerability) or isinstance(item, DependencyVulnerability))

if __name__ == '__main__':
    unittest.main()
