import aoc_lube

LINES = aoc_lube.fetch(year=2023, day=1).splitlines()


def part_one():
    result = 0
    for line in LINES:
        number = "".join([char if char.isdigit() else "" for char in line])
        result += int(f"{number[0]}{number[-1]}")
    return result


if __name__ == "__main__":
    print(part_one())
