import unittest
import os

# Automatische Testentdeckung und Ausführung
loader = unittest.TestLoader()
fileDir = os.path.dirname(os.path.abspath(__file__))
tests = loader.discover(fileDir, pattern='*')
testRunner = unittest.runner.TextTestRunner()
result = testRunner.run(tests)

if not result.wasSuccessful():
    raise Exception("The unittests failed")