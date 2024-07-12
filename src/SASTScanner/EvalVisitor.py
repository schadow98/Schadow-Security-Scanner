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