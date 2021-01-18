import argparse
import sys
print(str(sys.argv))


parser = argparse.ArgumentParser()

parser.add_argument("fileName", type=str, nargs="+", help="the name of the file reading from")
#       -d      destination file for cat
parser.add_argument("-d", type=str, help="describing destintion for the cat")

#       -b      Number the non-blank output lines, starting at 1.
parser.add_argument("-b", "--nonblank", help="Number the non-blank output lines, starting at 1.")
#      -e      Display non-printing characters (see the -v option), and display
#              a dollar sign (`$') at the end of each line.

#      -n      Number the output lines, starting at 1.

#      -s      Squeeze multiple adjacent empty lines, causing the output to be
#              single spaced.

#      -t      Display non-printing characters (see the -v option), and display
#              tab characters as `^I'.

#      -u      Disable output buffering.

#      -v      Display non-printing characters so they are visible.  Control
#              characters print as `^X' for control-X; the delete character
#              (octal 0177) prints as `^?'.  Non-ASCII characters (with the high
#              bit set) are printed as `M-' (for meta) followed by the character
#              for the low 7 bits.
tempFile = open("tempFile.txt", "a")
arg = parser.parse_args()

linecounter = 0

for argument in sys.argv:
    if not argument.startswith("-") and not argument.__eq__("cat.py"):
        f = open(argument,"r")
        for line in f:
            beginLine = ""
            #if args.nonblank: couldnt implement in time alloted


            tempFile.write(f.read())
    else:
        print("its an argument")