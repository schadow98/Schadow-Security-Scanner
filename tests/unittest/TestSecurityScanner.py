import unittest
import loadModules
from SecurityScanner import SecurityScanner

class TestSecurityScanner(unittest.TestCase):

  def test_positive_zahlen(self):
    """Testet die Funktion berechne_quadrat mit positiven Zahlen."""
    zahlen = [1, 2, 3, 4, 5]
    ergebnisse = [zahl * zahl for zahl in zahlen]
    
if __name__ == "__main__":
  unittest.main()
