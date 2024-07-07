import ast
from SASTScanner.InjectionPattern import InjectionPattern
from SASTScanner.SASTScanner import SASTScanner

import logging
import json
import re

from SASTScanner.SASTVulnerability import SASTVulnerability

class InjectionScanner(SASTScanner):
    def __init__(self, workingDir = ".", patterns = []) -> None:
        self.workingDir = workingDir
        self.patterns = patterns
        self.vulnerarbilities = []
        
        logging.info(self.__dict__)
        super().__init__(workingDir)
        self.scannInjectionPatterns()
        self.printVulnerarbilities()

    def scannInjectionPatterns(self):
        if len(self.patterns) == 0:
            raise Exception("No patterns defined")
        
        for pattern in self.patterns:
            pattern = InjectionPattern(pattern)
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


    def processSrc(self, pattern: InjectionPattern, files: list[str]) -> list[SASTVulnerability]:
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


    def processAST(self, pattern: InjectionPattern, files: list[str]) -> list[SASTVulnerability]:
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

