class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}

    def declare(self, var, var_type):
        if var in self.symbol_table:
            raise Exception(f"Semantic Error: '{var}' already declared")
        self.symbol_table[var] = var_type

    def check(self, var):
        if var not in self.symbol_table:
            raise Exception(f"Semantic Error: '{var}' not declared")

    def analyze_assignment(self, var):
        self.check(var)

    def analyze(self, ast):
        # declarations
        for decl in ast.declarations:
            for var in decl.identifiers:
                self.declare(var, decl.var_type)

        # statements
        for stmt in ast.statements:
            if hasattr(stmt, "identifier"):
                self.check(stmt.identifier)