from ast import *
from tok_types import *
from lexer import *

def parse(tok_lst):
    if tok_lst is None: return None
    if empty_check(tok_lst, "PARSE ERROR: Must write a valid program"): return None

    match tok_lst[0].type_:
        case TokType.LParen:
            _ = tok_lst.pop(0)
            if empty_check(tok_lst, "PARSE ERROR: Opening paren followed by nothing"): return None
            match tok_lst[0].type_:
                case TokType.Prim1:
                    op = tok_lst.pop(0).val
                    if empty_check(tok_lst, "PARSE ERROR: Primitive operation followed by nothing"): return None
                    sub_expr = parse(tok_lst)
                    if sub_expr is None: return None
                    if empty_check(tok_lst, "PARSE ERROR: Missing closing paren"): return None
                    match tok_lst[0].type_:
                        case TokType.RParen:
                            _ = tok_lst.pop(0)
                            return Prim1(op, sub_expr)
                        case _:
                            print("ERROR: Must be closing paren")
                            return None
                case _:
                    print("ERROR: Invalid operation")
                    return None
        case TokType.Int:
            i = tok_lst.pop(0).val
            return Int(i)
        case _:
            print("ERROR: Invalid expression starter")
            return None

def empty_check(lst, message: str):
    if len(lst) == 0:
        print(message)
        return True

    return False