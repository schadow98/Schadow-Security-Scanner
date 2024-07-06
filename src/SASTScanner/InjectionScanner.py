from SASTScanner.SASTScanner import SASTScanner

import logging
import json

class InjectionScanner(SASTScanner):
    def __init__(self, workingDir = ".", patterns = []) -> None:
        self.workingDir = workingDir
        
        logging.info(self.__dict__)
        super().__init__(workingDir)
   

