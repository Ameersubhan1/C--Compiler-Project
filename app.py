from flask import Flask, request, jsonify
from lexer import tokenize
from parser import Parser
from semantic import SemanticAnalyzer
from intermediate import IntermediateCode
from flask import render_template

app = Flask(__name__)
@app.route('/run', methods=['POST'])
def run_code():
    try:
        code = request.json['code']

        # 1. LEXER
        tokens = tokenize(code)

        # 2. PARSER
        parser = Parser(tokens)
        ast = parser.parse_program()

        # 3. SEMANTIC
        semantic = SemanticAnalyzer()

        for decl in ast.declarations:
            for var in decl.identifiers:
                semantic.declare(var, decl.var_type)

        # 4. INTERMEDIATE CODE
        ic = IntermediateCode()
        for stmt in ast.statements:
            ic.generate(stmt)

        return jsonify({
            "status": "success",

            # 🔥 FULL REPORT DATA
            "tokens": tokens,
            "ast": repr(ast),
            "symbol_table": semantic.symbol_table,
            "quadruples": ic.code,
            "message": "Compilation Successful"
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "error": str(e)
        })

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
