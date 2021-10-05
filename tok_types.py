from enum import Enum
# Initializes the Token Types
class TokType(Enum):
    INVALID = -1
    EOF = 0
    Int = 1
    LParen = 2
    RParen = 3
    Prim1 = 4
    
# Creates Tok class
class Tok:
    # Has type and val (optional) fields
    def __init__(self, type_: TokType, val: any = None):
        self.type_ = type_
        self.val = val
    # Define this to display nicely
    def __repr__(self):
        if self.val: return f'{self.type_} : {self.val}'
        return f'{self.type_}'