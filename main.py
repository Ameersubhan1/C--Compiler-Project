from lexer import tokenize
from parser import Parser
from semantic import SemanticAnalyzer
from intermediate import IntermediateCode

code = """
int $x$;
$x$ := 5 + 3 * 2;
"""

# LEXER
tokens = tokenize(code)
print("Tokens:", tokens)

# PARSER
parser = Parser(tokens)
ast = parser.parse_program()
print("✅ Parsing Done")

# SEMANTIC
semantic = SemanticAnalyzer()
semantic.declare("$x$", "int")
print("✅ Semantic OK")

# INTERMEDIATE CODE
ic = IntermediateCode()

for stmt in ast.statements:
    ic.generate(stmt)

print("✅ Quadruples:")
ic.print_code()