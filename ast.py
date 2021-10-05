class Int:
    def __init__(self, val: int):
        self.val = val
    def __repr__(self):
        return f'Int({self.val})'

class Prim1:
    def __init__(self, op: str, expr: any):
        self.op = op
        self.expr = expr
    def __repr__(self):
        return f'({self.op} {self.expr})'