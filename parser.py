from ast_nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    # -------------------------
    # BASIC HELPERS
    # -------------------------
    def current(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return ('EOF', '')

    def match(self, expected):
        token = self.current()
        if token[0] == expected:
            self.pos += 1
            return token
        else:
            raise Exception(f"Syntax Error: Expected {expected}, got {token}")

    # -------------------------
    # PROGRAM
    # -------------------------
    def parse_program(self):
        declarations = self.parse_declarations()
        statements = self.parse_statements()
        return Program(declarations, statements)

    # -------------------------
    # DECLARATIONS
    # -------------------------
    def parse_declarations(self):
        decls = []

        while self.current()[0] in ['INT', 'STRING', 'BOOL']:
            decls.append(self.parse_declaration())
            self.match('SEMICOLON')

        return decls

    def parse_declaration(self):
        var_type = self.current()[1]
        self.pos += 1

        identifiers = self.parse_identifier_list()
        return Declaration(var_type, identifiers)

    def parse_identifier_list(self):
        ids = []
        ids.append(self.match('IDENTIFIER')[1])

        while self.current()[0] == 'COMMA':
            self.match('COMMA')
            ids.append(self.match('IDENTIFIER')[1])

        return ids

    # -------------------------
    # STATEMENTS (FIXED)
    # -------------------------
    def parse_statements(self):
        stmts = []

        while self.current()[0] not in ['EOF', 'RBRACE']:
            stmts.append(self.parse_statement())

            if self.current()[0] == 'SEMICOLON':
                self.match('SEMICOLON')
            else:
                break

        return stmts

    def parse_statement(self):
        token = self.current()

        if token[0] == 'IDENTIFIER':
            return self.parse_assignment()

        elif token[0] == 'IF':
            return self.parse_if()

        elif token[0] == 'WHILE':
            return self.parse_while()

        elif token[0] == 'LBRACE':
            return self.parse_block()

        else:
            raise Exception(f"Invalid statement: {token}")

    # -------------------------
    # ASSIGNMENT
    # -------------------------
    def parse_assignment(self):
        name = self.match('IDENTIFIER')[1]
        self.match('ASSIGN')
        expr = self.parse_expression()
        return Assignment(name, expr)

    # -------------------------
    # IF-ELSE
    # -------------------------
    def parse_if(self):
        self.match('IF')
        self.match('LPAREN')
        condition = self.parse_expression()
        self.match('RPAREN')

        then_branch = self.parse_statement()

        self.match('ELSE')
        else_branch = self.parse_statement()

        return If(condition, then_branch, else_branch)

    # -------------------------
    # WHILE
    # -------------------------
    def parse_while(self):
        self.match('WHILE')
        self.match('LPAREN')
        condition = self.parse_expression()
        self.match('RPAREN')

        body = self.parse_statement()

        return While(condition, body)

    # -------------------------
    # BLOCK { }
    # -------------------------
    def parse_block(self):
        self.match('LBRACE')
        statements = self.parse_statements()
        self.match('RBRACE')
        return statements

    # -------------------------
    # EXPRESSIONS
    # -------------------------
    def parse_expression(self):
        node = self.parse_term()

        while self.current()[0] in ['PLUS', 'MINUS']:
            op = self.current()[1]
            self.pos += 1
            right = self.parse_term()
            node = BinaryOp(node, op, right)

        return node

    def parse_term(self):
        node = self.parse_factor()

        while self.current()[0] in ['MULT', 'DIV']:
            op = self.current()[1]
            self.pos += 1
            right = self.parse_factor()
            node = BinaryOp(node, op, right)

        return node

    def parse_factor(self):
        token = self.current()

        if token[0] == 'NUMBER':
            self.match('NUMBER')
            return Number(token[1])

        elif token[0] == 'IDENTIFIER':
            self.match('IDENTIFIER')
            return Identifier(token[1])

        elif token[0] == 'LPAREN':
            self.match('LPAREN')
            node = self.parse_expression()
            self.match('RPAREN')
            return node

        elif token[0] in ['TRUE', 'FALSE']:
            self.pos += 1
            return Number(token[1])

        else:
            raise Exception(f"Invalid expression: {token}")