class Node:
    pass


class Program(Node):
    def __init__(self, declarations, statements):
        self.declarations = declarations
        self.statements = statements

    def __repr__(self):
        return f"""
Program:
  Declarations: {self.declarations}
  Statements: {self.statements}
"""


class Declaration(Node):
    def __init__(self, var_type, identifiers):
        self.var_type = var_type
        self.identifiers = identifiers

    def __repr__(self):
        return f"Declaration({self.var_type}, {self.identifiers})"


class Assignment(Node):
    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression

    def __repr__(self):
        return f"{self.identifier} := {self.expression}"


class BinaryOp(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"({self.left} {self.op} {self.right})"


class Number(Node):
    def __repr__(self):
        return str(self.value)

    def __init__(self, value):
        self.value = value


class Identifier(Node):
    def __repr__(self):
        return self.name

    def __init__(self, name):
        self.name = name

class Program(Node):
    def __init__(self, declarations, statements):
        self.declarations = declarations
        self.statements = statements

    def __repr__(self):
        return f"Program(declarations={self.declarations}, statements={self.statements})"