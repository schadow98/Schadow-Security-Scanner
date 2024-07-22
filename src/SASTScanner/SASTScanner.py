import ast
import os
import logging
import json
import re

from BaseScanner import BaseScanner
from SASTScanner.SASTPattern import SASTPattern
from SASTScanner.SASTVulnerability import SASTVulnerability

class SASTScanner(BaseScanner):
    def __init__(self, name:str, workingDir: str, patterns: list[dict] = []):  # -> list[Vulnerability]:
        self.name = name 
        self.workingDir         = workingDir
        self.sourceCodeFiles    = set()
        self.findAllSourceCodeFiles()      
        
        self.patterns = patterns
        self.vulnerarbilities = []
        logging.info(f"{self.name} " + json.dumps(self.__dict__(), indent=2))
        
        self.scannInjectionPatterns()
        self.printVulnerarbilities()


    def __dict__(self) -> None:
        return {
            "workingDir": self.workingDir,
            "sourceCodeFiles": list(self.sourceCodeFiles)
        }

    def findAllSourceCodeFiles(self) -> None:
        # List all files in the directory
        for root, _, filenames in os.walk(self.workingDir):
            # skip caching - binary files cant get proceeded
            # skipping logs - becouse else the securityscanner finds their a lot of vulnarability
            if "__pycache__" in root or "logs" in root or "dist" in root or "build" in root or "docs" in root: continue
            for filename in filenames:
                if filename.endswith(".pyc"): continue
                full_path = os.path.join(root, filename)
                if not full_path.startswith('.\\.'):
                    self.sourceCodeFiles.add(full_path)

    def getFilteredSourceCodeFiles(self, filters = [".py"]) -> list[str]:

        if len(filters) == 0: return self.sourceCodeFiles
        def filterByFilename(path):
            path = path.lower()
            for filter in filters:
                if path.endswith(filter):
                    return True
            return False
            
        return list(filter(filterByFilename, self.sourceCodeFiles))

    def processSrc(self, pattern: SASTPattern, files: list[str]) -> list[SASTVulnerability]:
        sastVulnerabilities = []
        regex = re.compile(pattern.pattern)
        for filePath in files:
            with open(filePath, "r") as file:
                for lineCounter, line in enumerate(file, start=1):
                    found = re.findall(regex, line)
                    if found:
                        sastVulnerabilities.append(SASTVulnerability(pattern.name, 
                                                                         pattern.message, 
                                                                         "srcScanner", 
                                                                         pattern.pattern, 
                                                                         filePath, 
                                                                         lineCounter, 
                                                                         line))
        return sastVulnerabilities


    def processAST(self, pattern: SASTPattern, files: list[str]) -> list[SASTVulnerability]:
        eval_calls = []

        class EvalVisitor(ast.NodeVisitor):
            def __init__(self, filePath):
                self.filePath = filePath
            
            def visit_Call(self, node):
                # Prüfen, ob die aufgerufene Funktion eval ist
                if isinstance(node.func, ast.Name) and node.func.id == pattern.name:
                    eval_calls.append(SASTVulnerability(pattern.name, 
                                                        pattern.message, 
                                                        "astScanner", 
                                                        f"function with name {pattern.name} is called", 
                                                        filePath, f"line {node.lineno}-{node.end_lineno}:col {node.col_offset}-{node.end_col_offset}", 
                                                        ast.unparse(node)))
                self.generic_visit(node)

        for filePath in files:
            with open(filePath, "r") as file:
                content = file.read()
                try:
                    tree = ast.parse(content, filename=filePath)
                    visitor = EvalVisitor(filePath)
                    visitor.visit(tree)
                except SyntaxError as e:
                    logging.warn(f"Skipping file: Syntax error in file {filePath}: {e}")
        return eval_calls

    def scannInjectionPatterns(self) -> None:
        if len(self.patterns) == 0:
            raise Exception("No patterns defined")
        
        for pattern in self.patterns:
            pattern = SASTPattern(pattern)
            files = self.getFilteredSourceCodeFiles(pattern.files)
            for kind in pattern.kinds:
                kind = kind.lower()
                if kind == "src":
                    method = self.processSrc
                elif kind == "ast":
                    method = self.processAST
                else:
                    logging.warn(f"Skip kind becouse not defined: {kind}")
                    continue

                self.vulnerarbilities +=method(pattern, files)