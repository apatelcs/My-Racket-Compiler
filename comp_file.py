from lexer import *
from parse import *
from comp import *
import argparse

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--ifile', type = str, default = "prog.rkt")
    argparser.add_argument('--ofile', type = str, default = "prog.s")
    args = argparser.parse_args()

    with open(args.ifile, 'r') as inf:
        lines = inf.readlines()
        rkt_code = ''
        for i, line in enumerate(lines):
            if i == 0: continue
            rkt_code += line
        inf.close()

    ts = tokenize(rkt_code)
    ex = parse(ts)
    asm_code = comp(ex)

    with open(args.ofile, 'w') as outf:
        outf.write(asm_code)
        outf.close()