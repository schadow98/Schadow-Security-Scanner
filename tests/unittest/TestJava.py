from SASTScanner.SASTVulnerability import SASTVulnerability
import loadModules
import unittest
import os
from SASTScanner.SASTScanner import SASTScanner


class SASTScanner(SASTScanner):
    def printVulnerarbilities(self):
        pass

patternsInjection = [

    {
        "pattern": "(?<![\\w])eval\\(",
        "name": "eval",
        "message": "eval Method found - please use ast.literal_eval instead",
        "files": [".java"],
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

patternsSecret = [
  {
    "pattern": "[\"\\']?[A-Za-z0-9]{32,}[\"\\']?",
    "name": "API_KEY",
    "message": "API KEY detected - please use Environment Variables or Secret Manager to store secrets",
    "files": [".java"],
    "kinds": ["src"]
  },
  {
    "pattern": "[\"\\']?password[\"\\']?\\s*[:=]\\s*[\"\\'][^\"\\']{8,}[\"\\']",
    "name": "PASSWORD",
    "message": "PASSWORD detected - please use Environment Variables or Secret Manager to store secrets",
    "files": [".java"],
    "kinds": ["src"]
  },
  {
    "pattern": "[\"\\']?secret[\"\\']?\\s*[:=]\\s*[\"\\'][^\"\\']{8,}[\"\\']",
    "name": "SECRET",
    "message": "SECRET detected - please use Environment Variables or Secret Manager to store secrets",
    "files": [".java"],
    "kinds": ["src"]
  },
  {
    "pattern": "-----BEGIN (EC|RSA|DSA|PGP|OPENSSH) PRIVATE KEY-----",
    "name": "PRIVAT KEY",
    "message": "PRIVAT KEY detected - please use Environment Variables or Secret Manager to store secrets",
    "files": [".java"],
    "kinds": ["src"]
  }      
]

class TestJava(unittest.TestCase):

    def test_TestJavaFindSecrets(self):
        workingDir = os.path.join(os.environ["PROJECT_PATH"], "./tests/testdata/java")

        res = SASTScanner("secretDetectionScanner", workingDir, patternsSecret).vulnerarbilities
        self.assertEqual(len(res), 4)
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

    def test_TestJavaFindInjection(self):
        workingDir = os.path.join(os.environ["PROJECT_PATH"], "./tests/testdata/java")

        res = SASTScanner("injectionDetectionScanner", workingDir, patternsInjection).vulnerarbilities
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

    def test_TestJavaFindInjectionAndSecrets(self):
        workingDir = os.path.join(os.environ["PROJECT_PATH"], "./tests/testdata/java")

        res = SASTScanner("injectionDetectionScanner", workingDir, patternsInjection+patternsSecret).vulnerarbilities
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