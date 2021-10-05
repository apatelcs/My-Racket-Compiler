# The below code was adapted from https://github.com/davidcallanan/py-myopl-code/blob/master/ep1/shell.py

from lexer import *
from parse import *
from interp import *

while True:
    # Displays 'blackmail > ' and waits for user input
    text = input('blackmail > ')
    # Checks if input is quit to quit the shell
    if text == 'quit': break
    # Otherwise, tokenizes, parses, and interprets the inputted code
    result = interp(parse(tokenize(text)))
    # Prints result
    print(result)