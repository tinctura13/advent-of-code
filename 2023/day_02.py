import re
from collections import Counter
from math import prod

import aoc_lube

LINES = aoc_lube.fetch(year=2023, day=2).splitlines()

condition = Counter({
        "red": 12,
        "green": 13,
        "blue": 14
    })


def part_one():
    result = 0
    for line in LINES:
        game_n, game_log = line[5:].split(":")
        game_cubes = Counter()
        for n, color in re.findall(r"(\d+) (\w+)", game_log):
            if int(n) > game_cubes[color]:
                game_cubes[color] = int(n)
        if game_cubes <= condition:
            result += int(game_n)
    return result


def part_two():
    result = 0
    for line in LINES:
        game_n, game_log = line[5:].split(":")
        game_cubes = Counter()
        for n, color in re.findall(r"(\d+) (\w+)", game_log):
            if int(n) > game_cubes[color]:
                game_cubes[color] = int(n)
        result += prod(game_cubes.values())
    return result


if __name__ == "__main__":
    print(f"part one answer is {part_one()}")
    print(f"part two answer is {part_two()}")
