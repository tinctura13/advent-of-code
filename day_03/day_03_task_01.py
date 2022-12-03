INPUT = "day_03_input.txt"

lower = {chr(i + 96): i for i in range(1, 27)}
upper = {chr(i + 64): i + 26 for i in range(1, 27)}
cook_book = lower | upper


def read_data(file):
    """Read the data from file"""
    data = []
    with open(file, 'r') as fin:
        data = fin.readlines()
    return [_.strip() for _ in data]


def split_rucksack(rucksack):
    half = int(len(rucksack) / 2)
    first = set(rucksack[:half])
    second = set(rucksack[half:])
    return first, second


def find_common_items(l, r):
    return next(iter(l.intersection(r)))


def get_score(meal, cook_book):
    return cook_book[meal]


def get_final_score(data):
    score = 0
    for rucksack in data:
        l, r = split_rucksack(rucksack)
        score += get_score(find_common_items(l, r), cook_book)
    return score


if __name__ == "__main__":
    data = read_data(INPUT)
    print(get_final_score(data))
