import aoc_lube
import re 

LINES = aoc_lube.fetch(year=2023, day=2).splitlines()

condition = {
        "red": 12,
        "green": 13,
        "blue": 14
    }


def part_one():
    result = 0
    game_state = True
    for line in LINES:
        game_n, game_log = line[5:].split(":")
        game = re.findall(r"(\d+) (\w+)", game_log)
        for round_ in game:
            if condition[round_[1]] < int(round_[0]):
                game_state = False
                continue
        if game_state:
            result += int(game_n)
        game_state = True
    return result


if __name__ == "__main__":
    print(part_one())
