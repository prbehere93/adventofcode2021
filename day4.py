"""
--- Day 3: Giant Squid ---
"""
from pathlib import Path

file_path = Path.cwd().joinpath("files/day4.txt")
file_input = file_path.read_text(encoding="utf-8").split("\n")
file_input = list(filter(len, file_input))

print(file_input)

bingo_numbers = file_input[0]

bingo_boards = {}

for_board = [
    (i, j)
    for i, j in zip(range(1, len(file_input), 5), range(6, len(file_input) + 1, 5))
]

for ind, i in enumerate(for_board):
    bingo_boards[ind] = [
        list(filter(bool, i.split(" ")))
        for i in file_input[i[0] : i[1]]  # filter empty strings ('') and parse boards
    ]

print(bingo_boards)


def check_bingo(board: list) -> bool:
    pass
