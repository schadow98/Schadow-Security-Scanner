import os
import logging
import json

class SASTScanner(object):
    def __init__(self, workingDir: str):  # -> list[Vulnerability]:
        self.workingDir         = workingDir
        self.sourceCodeFiles    = set()
        self.findAllSourceCodeFiles()
        logging.info("SASTScanner " + json.dumps(self.__dict__(), indent=2))

    def __dict__(self) -> None:
        return {
            "workingDir": self.workingDir,
            "sourceCodeFiles": list(self.sourceCodeFiles)
        }

    def findAllSourceCodeFiles(self) -> None:
        # List all files in the directory
        for root, _, filenames in os.walk(self.workingDir):
            for filename in filenames:
                full_path = os.path.join(root, filename)
                if not full_path.startswith('.\\.'):
                    self.sourceCodeFiles.add(full_path)

    def getFilteredSourceCodeFiles(self, filters = [".py"]) -> list[str]:
        def filterByFilename(path):
            path = path.lower()
            for filter in filters:
                if path.endswith(filter):
                    return True
            return False
            
        return filter(filterByFilename, self.sourceCodeFiles)

