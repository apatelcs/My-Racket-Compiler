from lexer import *
from parse import *
from interp import *
from comp import *

filename = "prog.rkt" # SET FILENAME

with open(filename) as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if i == 0: continue
        ts = tokenize(line)
        e = parse(ts)
        fn = interp(e)
        print(f'Line {i} evaluated to {fn}')
        asm = comp(e)
        print(f'Here is the assembly for line {i}:\n{asm}\n')