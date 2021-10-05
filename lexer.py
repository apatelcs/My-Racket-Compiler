from tok_types import *
import re

def tokenize(text):
    toks = []
    pos = 0

    while pos < len(text):
        if text[pos] in ' \t\n':
            pos += 1
        elif text[pos] == '(':
            token = Tok(TokType.LParen)
            toks.append(token)
            pos += 1
        elif text[pos] == ')':
            token = Tok(TokType.RParen)
            toks.append(token)
            pos += 1
        elif x := re.search(r'^[0-9]+', text[pos:]):
            token = Tok(TokType.Int, int(x.group()))
            toks.append(token)
            pos += x.span()[1]
        elif x := re.search(r'^add1', text[pos:]):
            token = Tok(TokType.Prim1, x.group())
            toks.append(token)
            pos += x.span()[1]
        elif x := re.search(r'^sub1', text[pos:]):
            token = Tok(TokType.Prim1, x.group())
            toks.append(token)
            pos += x.span()[1]
        else:
            toks.append(Tok(TokType.INVALID))
            print('PARSE ERROR: Invalid input')
            return None
            
    return toks