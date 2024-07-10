import json
import logging

class BaseScanner:
    """
    BaseScanner class is the basis for the other scanners.
    It 's provide mehthods, that all scanners need.
    """

    def printVulnerarbilities(self)-> None:
        """
        This method prints the vulnerabilities found by the scanner.
        """
        if len(self.vulnerarbilities) == 0:
            logging.info(f"{self.__class__.__name__} found {len(self.vulnerarbilities)} DependencyVulnerabilities")
        else:
            logging.error("-"*20)
            logging.error(f"{self.__class__.__name__} found {len(self.vulnerarbilities)} DependencyVulnerabilities")
            logging.error("-"*20)
        
            for vulnerability in self.vulnerarbilities:
                logging.error(json.dumps(vulnerability.__dict__, indent=2))