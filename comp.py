from ast import *

def comp(e):
    asm = ''

    asm += 'global _entry\n'
    asm += 'default rel\n'
    asm += 'section .text\n'
    asm += '_entry:\n'
    asm += comp_e(e)
    asm += 'ret'
    return asm

def comp_e(e):
    asm = ''
    if isinstance(e, Int):
        asm += f'mov rax, {e.val}\n'
    elif isinstance(e, Prim1):
        match e.op:
            case 'add1':
                asm += comp_e(e.expr)
                asm += 'add rax, 1\n'
            case 'sub1':
                asm += comp_e(e.expr)
                asm += 'sub rax, 1\n'
    return asm