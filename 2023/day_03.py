import re
from pprint import pprint
from typing import List

import aoc_lube

LINES = aoc_lube.fetch(year=2023, day=3).splitlines()
TEST_LINES = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]
PART_TWO_LINE = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]


def add_padding(arr):
    padding_length = len(arr[0]) + 2
    padding = '.' * padding_length
    new_array = [padding]
    for element in arr:
        new_array.append('.' + element + '.')
    new_array.append(padding)
    return new_array


def find_symbols(data):
    pattern = r"[^\d\.]"
    symbols = set()
    for item in data:
        matches = re.findall(pattern, item)
        symbols.update(matches)
    return symbols


def find_gears(data):
    coords = []
    for i in range(len(data[0])):
        for j in range(len(data)):
            if data[i][j] == "*":
                coords.append((i, j))
    return coords


def part_one(data: List[str], symbols: set) -> int:
    # keep curent number
    curr_n = ""
    # count sum
    result = 0
    # iterate over data
    is_part = False
    for i in range(len(data[0])):
        for j in range(len(data)):
            cur = data[i][j]
            if cur.isdigit():
                curr_n += str(cur)
                if any(data[ni][nj] in symbols for ni, nj in [
                    (i-1, j), (i-1, j-1), (i, j-1), (i-1, j+1),
                    (i, j+1), (i+1, j+1), (i+1, j), (i+1, j-1)
                    ]):
                    is_part = True
            else:
                if is_part:
                    result += int(curr_n)
                curr_n = ""
                is_part = False
    return result


def part_two():
    pass


if __name__ == "__main__":
    ##############
    #  PART ONE  #
    ##############
    # add padding
    test_data = add_padding(TEST_LINES)
    # find all symbols in the dataset    
    test_symbols = find_symbols(test_data)
    assert 4361 == part_one(test_data, test_symbols)

    # add padding
    data = add_padding(LINES)
    # find all symbols in the dataset
    symbols = find_symbols(data)
    # get results
    print(part_one(data, symbols))

        
        
    