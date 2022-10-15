"""
--- Day 3: Binary Diagnostic ---
"""
from pathlib import Path
from turtle import position
import pandas as pd

file_path = Path.cwd().joinpath("files/day3.txt")
diagnostic_bits = file_path.read_text(encoding="utf-8").split("\n")

"""
Find power consumption i.e. a multiplication of gamma_rate and epsilon_rate
gamma rate - find the most common bit in the corresponding location
epsilon rate - find the least common bit in the corresponding location

Idea - Finding the sum of the values at each position can help us find the most/least common number
eg - If it is 501/1000 then 1 is more common for that position and viz
"""


def convert_to_decimal(binary_num) -> int:
    return sum(
        [
            int(i) * (2 ** int(m))
            for i, m in zip(binary_num[::-1], range(0, len(binary_num)))
        ]
    )


position_df = (
    pd.Series(diagnostic_bits).str.split("", expand=True).drop([0, 13], axis=1)
)

sum_list = [sum(pd.to_numeric(position_df[i])) for i in position_df.columns]

most_common = "".join(["1" if i > 500 else "0" for i in sum_list])
least_common = "".join(["0" if i > 500 else "1" for i in sum_list])

gamma_rate = convert_to_decimal(most_common)
epsilon_rate = convert_to_decimal(least_common)

print(f"Power Consumption of the damn submarine - {gamma_rate*epsilon_rate}")

# Part 2
"""
The life_support_rating i.e. obtained from multiplying the 
oxygen generator rating by the CO2 scrubber rating.

For example, to determine the oxygen generator rating value using the same example diagnostic report from above:

Start with all 12 numbers and consider only the first bit of each number. There are more 1 bits (7) than 0 bits (5), so keep only the 7 numbers with a 1 in the first position: 11110, 10110, 10111, 10101, 11100, 10000, and 11001.
Then, consider the second bit of the 7 remaining numbers: there are more 0 bits (4) than 1 bits (3), so keep only the 4 numbers with a 0 in the second position: 10110, 10111, 10101, and 10000.
In the third position, three of the four numbers have a 1, so keep those three: 10110, 10111, and 10101.
In the fourth position, two of the three numbers have a 1, so keep those two: 10110 and 10111.
In the fifth position, there are an equal number of 0 bits and 1 bits (one each). So, to find the oxygen generator rating, keep the number with a 1 in that position: 10111.
As there is only one number left, stop; the oxygen generator rating is 10111, or 23 in decimal.
"""

# getting the oxygen generator rating
position_df_o2 = position_df.copy()
for i in position_df.columns:
    most_common = (
        "1"
        if sum(position_df_o2[i].astype("int")) / len(position_df_o2[1]) >= 0.5
        else "0"
    )
    position_df_o2 = position_df_o2[position_df_o2[i] == most_common]
    if len(position_df_o2) == 1:
        break

oxygen_generator_rating_binary = "".join(position_df_o2.values[0])
oxygen_generator_rating = convert_to_decimal(oxygen_generator_rating_binary)
print(f"{oxygen_generator_rating=}")

position_df_co2 = position_df.copy()
# getting the CO2 scrubber rating
for i in position_df.columns:
    least_common = (
        "0"
        if sum(position_df_co2[i].astype("int")) / len(position_df_co2[1]) >= 0.5
        else "1"
    )
    position_df_co2 = position_df_co2[position_df_co2[i] == least_common]
    if len(position_df_co2) == 1:
        break

co2_generator_rating_binary = "".join(position_df_co2.values[0])
co2_generator_rating = convert_to_decimal(co2_generator_rating_binary)
print(f"{co2_generator_rating=}")

print(f"Life support rating - {oxygen_generator_rating*co2_generator_rating}")
