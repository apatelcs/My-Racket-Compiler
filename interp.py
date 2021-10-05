from ast import *
from parse import *

def interp(e):
    if isinstance(e, Int):
        return e.val
    elif isinstance(e, Prim1):
        match e.op:
            case 'add1':
                return interp(e.expr) + 1
            case 'sub1':
                return interp(e.expr) - 1