"""
Finding if the next no. is greater than the previous no.
"""
from pathlib import Path

file_path = Path.cwd().joinpath("day1.txt")

depth = file_path.read_text(encoding="utf-8").split("\n")

depth = [int(i) for i in depth]

s = 0
for ind, num in enumerate(depth):
    if ind > 0:
        if num > depth[ind - 1]:
            s = s + 1

print(s)
