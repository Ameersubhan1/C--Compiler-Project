class IntermediateCode:
    def __init__(self):
        self.code = []
        self.temp_count = 0

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def generate(self, node):
        if node.__class__.__name__ == "Number":
            return node.value

        elif node.__class__.__name__ == "Identifier":
            return node.name

        elif node.__class__.__name__ == "BinaryOp":
            left = self.generate(node.left)
            right = self.generate(node.right)
            temp = self.new_temp()
            self.code.append((node.op, left, right, temp))
            return temp

        elif node.__class__.__name__ == "Assignment":
            value = self.generate(node.expression)
            self.code.append((":=", value, "-", node.identifier))

    def print_code(self):
        for line in self.code:
            print(line)