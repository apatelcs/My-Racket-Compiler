# My-Racket-Compiler
This is a personal project where I have created a lexer, parser, interpreter, and compiler for a small subset of the Racket programming language. This subset only allows integer literals and incrementing/decrementing functions. Examples of valid programs are shown below:
```Racket
#lang racket
42
```
```Racket
#lang racket
(sub1 (add1 (sub1 0)))
```
This project takes concepts I have learned in the Introduction to Compilers course at the University of Maryland and applies them using Python. The lexer tokenizes the input string (representing the Racket program). Then, the parser uses recursive descent parsing to take the list of tokens and return an Abstract Syntax Tree (AST) representation of the program. This AST is then fed into either the interpreter or the compiler. The interpreter takes the AST and evaluates it using Python. The compiler takes the AST and converts it into a set of x86 assembly instructions.
## How to write and compile a Blackmail program
Feel free to use the few features I have provided:

1) You can use an interactive shell by entering `python3.10 shell.py` into the terminal (note that Python3.10 is a dependency for this project).
2) You can write your code in any file with the `.rkt` extension (by default I have provided a `prog.rkt` file for you to play around with). To compile and run the file, use the following commands:
```
make prog.s
make prog.run
```
Note that you can change the filename, so using `FNAME` as a placeholder, run:
```
python3.10 comp_file.py --ifile="FNAME.rkt" --ofile="FNAME.s"

make FILENAME.run
```
To clean up the folder at the end, simply run:
```
make clean
```
## Dependencies
- Python3.10
- Must have nasm installed
- Must have gcc installed