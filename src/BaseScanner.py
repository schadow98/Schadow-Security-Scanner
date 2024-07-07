import json
import logging

class BaseScanner(object):
    def printVulnerarbilities(self)-> None:
        logging.error("-"*20)
        logging.error(f"{self.__class__.__name__} found {len(self.vulnerarbilities)} DependencyVulnerabilities")
        logging.error("-"*20)
        
        for vulnerability in self.vulnerarbilities:
            logging.error(json.dumps(vulnerability.__dict__, indent=2))