from SASTScanner.SASTVulnerability import SASTVulnerability
import loadModules
import unittest
import os
from SASTScanner.SASTScanner import SASTScanner
patterns = [
    {
      "pattern": "[\"\\']?[A-Za-z0-9]{32,}[\"\\']?",
      "name": "API_KEY",
      "message": "API KEY detected - please use Environment Variables or Secret Manager to store secrets",
      "files": [],
      "kinds": ["src"]
    },
    {
      "pattern": "[\"\\']?password[\"\\']?\\s*[:=]\\s*[\"\\'][^\"\\']{8,}[\"\\']",
      "name": "PASSWORD",
      "message": "PASSWORD detected - please use Environment Variables or Secret Manager to store secrets",
      "files": [],
      "kinds": ["src"]
    },
    {
      "pattern": "[\"\\']?secret[\"\\']?\\s*[:=]\\s*[\"\\'][^\"\\']{8,}[\"\\']",
      "name": "SECRET",
      "message": "SECRET detected - please use Environment Variables or Secret Manager to store secrets",
      "files": [],
      "kinds": ["src"]
    },
    {
      "pattern": "-----BEGIN (EC|RSA|DSA|PGP|OPENSSH) PRIVATE KEY-----",
      "name": "PRIVAT KEY",
      "message": "PRIVAT KEY detected - please use Environment Variables or Secret Manager to store secrets",
      "files": [],
      "kinds": ["src"]
    }      
  ]

class SASTScanner(SASTScanner):
    def printVulnerarbilities(self):
        pass


class TestSecretScanner(unittest.TestCase):

    def test_TestSecretScannerFindSecrets(self):
        workingDir = os.path.join(os.environ["PROJECT_PATH"], "./tests/testdata/secretDetection/secrets")
 
        res = SASTScanner("secretDetectionScanner", workingDir, patterns).vulnerarbilities
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


    def test_TestSecretScannerNoSecrets(self):
        workingDir = os.path.join(os.environ["PROJECT_PATH"], "./tests/testdata/secretDetection/noSecrets")
        res = SASTScanner("secretDetectionScanner", workingDir, patterns).vulnerarbilities
        self.assertEqual(len(res), 0)
        self.assertIsInstance(res, list)