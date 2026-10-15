import re

TOKENS = [
    ('NUMBER', r'\d+'),
    ('IDENTIFIER', r'\$[a-zA-Z]+\$'),
    ('ASSIGN', r':='),
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('MULT', r'\*'),
    ('DIV', r'/'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('SEMICOLON', r';'),
    ('IF', r'if'),
    ('ELSE', r'else'),
    ('WHILE', r'while'),
    ('INT', r'int'),
    ('STRING', r'string'),
    ('BOOL', r'bool'),
    ('TRUE', r'true'),
    ('FALSE', r'false'),
    ('SKIP', r'[ \t\n]+'),
    ('COMMA', r','),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('GT', r'>'),
    ('LT', r'<'),
    ('EQ', r'=='),
    ('NEQ', r'<>'),
    ('GE', r'>='),
    ('LE', r'<='),
]

def tokenize(code):
    tokens = []
    while code:
        for token_type, pattern in TOKENS:
            match = re.match(pattern, code)
            if match:
                text = match.group(0)
                if token_type != 'SKIP':
                    tokens.append((token_type, text))
                code = code[len(text):]
                break
        else:
            raise Exception(f"Lexical Error: Invalid token near '{code[:10]}'")
    return tokens
