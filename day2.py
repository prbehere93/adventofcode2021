"""
Calculate the horizontal position and depth you would have after following the planned course
What do you get if you multiply your final horizontal position by your final depth?
"""
from pathlib import Path

file_path = Path.cwd().joinpath("day2.txt")

course_path = file_path.read_text(encoding="utf-8").split("\n")

horizontal_position = 0
depth = 0
aim = 0

for i in course_path:
    if i.startswith("forward"):
        horizontal_position = horizontal_position + int(i[-1])
        depth = depth + aim * int(i[-1])
    elif i.startswith("down"):
        aim = aim + int(i[-1])
    elif i.startswith("up"):
        aim = aim - int(i[-1])
    else:
        print("nope")
print(f"{horizontal_position=}  {depth=}")
print(f"Answer {horizontal_position * depth}")
