import sys
import pathlib
import os.path

print("ok", file=sys.stdout)
print("error", file=sys.stderr)

string = "test"
print(type(string.encode()))

l = [1, 2, 3]
print(*l, sep=";", end="\n")

with open('test.txt') as f:
    print(f.read())

p = pathlib.Path('test.txt')
print(p.resolve())

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    print(f)
