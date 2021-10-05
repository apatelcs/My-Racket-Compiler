# How to write and compile a Blackmail program
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
Enjoy :)
