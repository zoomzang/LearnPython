import argparse
import sys
import re
from os import walk

parser = argparse.ArgumentParser()
parser.add_argument("directory",type=str,help="help yourself,", default=".")
parser.add_argument("-name", type=str, help="Pattern for finding the files")
args = parser.parse_args()
f = []
for (dirpath, dirnames, filenames)  in walk(sys.argv[1]):
    f.extend(filenames)
    break
re.search
pattern = "*"

for x in f:
    match = re.search('*',f)
    if match:
        print(x)
    break

