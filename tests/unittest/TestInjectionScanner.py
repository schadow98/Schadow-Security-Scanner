from SASTScanner.SASTVulnerability import SASTVulnerability
import loadModules
import unittest
import os
from SASTScanner.SASTScanner import SASTScanner
patterns = [

    {
        "pattern": "(?<![\\w])eval\\(",
        "name": "eval",
        "message": "eval Method found - please use ast.literal_eval instead",
        "files": [],
        "kinds": ["src", "ast"]
      },
      {
        "pattern": "(SELECT|INSERT|UPDATE|DELETE|DROP|EXEC)\\s+.*(['\"].*['\"].*|.*\\+.*|.*\\{\\d+\\}.*)",
        "name": "sqlPattern",
        "message": "SqlCommand with string concatenation detected",
        "files": [".py"],
        "kinds": ["src"]
      }
  ]

class SASTScanner(SASTScanner):
    def printVulnerarbilities(self):
        pass


class InjectionScanner(unittest.TestCase):

    def test_FindNoInjectionVulnerabilities(self):
        workingDir = os.path.join(os.environ["PROJECT_PATH"], "./tests/testdata/injectionScanner/noFindings")
 
        res = SASTScanner("InjectionScanner", workingDir, patterns).vulnerarbilities
        self.assertEqual(len(res), 0)
        self.assertIsInstance(res, list)

    def test_TestSecretScannerFindSecretsAll(self):
        workingDir = os.path.join(os.environ["PROJECT_PATH"], "./tests/testdata/injectionScanner/findings")
 
        res = SASTScanner("secretDetectionScanner", workingDir, patterns).vulnerarbilities
        self.assertEqual(len(res), 8)
        self.assertIsInstance(res, list)
        for item in res:
            self.assertIsInstance(item, SASTVulnerability)
            self.assertTrue(hasattr(item, 'file'))
            self.assertTrue(hasattr(item, 'name'))
            self.assertTrue(hasattr(item, 'message'))
            self.assertTrue(hasattr(item, 'source'))
            self.assertTrue(hasattr(item, 'pattern'))
            self.assertTrue(hasattr(item, 'line'))
            self.assertTrue(hasattr(item, 'code'))

    def test_TestSecretScannerFindSecretsSrc(self):
        workingDir = os.path.join(os.environ["PROJECT_PATH"], "./tests/testdata/injectionScanner/findings")
        patterns = [{
        "pattern": "(?<![\\w])eval\\(",
        "name": "eval",
        "message": "eval Method found - please use ast.literal_eval instead",
        "files": [],
        "kinds": ["src"]
      }]


        res = SASTScanner("secretDetectionScanner", workingDir, patterns).vulnerarbilities
        self.assertEqual(len(res), 3)
        self.assertIsInstance(res, list)
        for item in res:
            self.assertIsInstance(item, SASTVulnerability)
            self.assertTrue(hasattr(item, 'file'))
            self.assertTrue(hasattr(item, 'name'))
            self.assertTrue(hasattr(item, 'message'))
            self.assertTrue(hasattr(item, 'source'))
            self.assertTrue(hasattr(item, 'pattern'))
            self.assertTrue(hasattr(item, 'line'))
            self.assertTrue(hasattr(item, 'code'))


    def test_TestSecretScannerFindSecretsAst(self):
        workingDir = os.path.join(os.environ["PROJECT_PATH"], "./tests/testdata/injectionScanner/findings")
        patterns = [

    {
        "pattern": "(?<![\\w])eval\\(",
        "name": "eval",
        "message": "eval Method found - please use ast.literal_eval instead",
        "files": [],
        "kinds": ["ast"]
      }]


        res = SASTScanner("secretDetectionScanner", workingDir, patterns).vulnerarbilities
        self.assertEqual(len(res), 3)
        self.assertIsInstance(res, list)
        for item in res:
            self.assertIsInstance(item, SASTVulnerability)
            self.assertTrue(hasattr(item, 'file'))
            self.assertTrue(hasattr(item, 'name'))
            self.assertTrue(hasattr(item, 'message'))
            self.assertTrue(hasattr(item, 'source'))
            self.assertTrue(hasattr(item, 'pattern'))
            self.assertTrue(hasattr(item, 'line'))
            self.assertTrue(hasattr(item, 'code'))

    def test_TestSecretScannerFindSecretsEval(self):
        workingDir = os.path.join(os.environ["PROJECT_PATH"], "./tests/testdata/injectionScanner/findings")
        patterns = [

    {
        "pattern": "(?<![\\w])eval\\(",
        "name": "eval",
        "message": "eval Method found - please use ast.literal_eval instead",
        "files": [],
        "kinds": ["ast", "src"]
      }]


        res = SASTScanner("secretDetectionScanner", workingDir, patterns).vulnerarbilities
        self.assertEqual(len(res), 6)
        self.assertIsInstance(res, list)
        for item in res:
            self.assertIsInstance(item, SASTVulnerability)
            self.assertTrue(hasattr(item, 'file'))
            self.assertTrue(hasattr(item, 'name'))
            self.assertTrue(hasattr(item, 'message'))
            self.assertTrue(hasattr(item, 'source'))
            self.assertTrue(hasattr(item, 'pattern'))
            self.assertTrue(hasattr(item, 'line'))
            self.assertTrue(hasattr(item, 'code'))

    def test_TestSecretScannerFindSecretsSQL(self):
        workingDir = os.path.join(os.environ["PROJECT_PATH"], "./tests/testdata/injectionScanner/findings")
        patterns = [
          {
        "pattern": "(SELECT|INSERT|UPDATE|DELETE|DROP|EXEC)\\s+.*(['\"].*['\"].*|.*\\+.*|.*\\{\\d+\\}.*)",
        "name": "sqlPattern",
        "message": "SqlCommand with string concatenation detected",
        "files": [".py"],
        "kinds": ["src"]
      }
        ]


        res = SASTScanner("secretDetectionScanner", workingDir, patterns).vulnerarbilities
        self.assertEqual(len(res), 2)
        self.assertIsInstance(res, list)
        for item in res:
            self.assertIsInstance(item, SASTVulnerability)
            self.assertTrue(hasattr(item, 'file'))
            self.assertTrue(hasattr(item, 'name'))
            self.assertTrue(hasattr(item, 'message'))
            self.assertTrue(hasattr(item, 'source'))
            self.assertTrue(hasattr(item, 'pattern'))
            self.assertTrue(hasattr(item, 'line'))
            self.assertTrue(hasattr(item, 'code'))