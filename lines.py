import sys
import os

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

if not os.path.isfile(sys.argv[1]):
    sys.exit("File does not exist")

count = 0

with open(sys.argv[1], "r") as file:
    line = file.readline()

    while line:
        if line.strip() != "" and not line.lstrip().startswith("#"):
            count += 1

        line = file.readline()

print(count)
