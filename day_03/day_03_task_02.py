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


def split_elves_by_groups(data):
    n = 3  # num of Elves for a group
    return [data[i:i + n] for i in range(0, len(data), n)]


def get_a_group_of_elves(data):
    return [set(_) for _ in data]


def find_common_bage(group):
    return next(iter(group[0].intersection(group[1], group[2])))


def get_score(meal, cook_book):
    return cook_book[meal]


def get_final_score(data):
    score = 0
    for item in data:
        group = get_a_group_of_elves(item)
        score += get_score(find_common_bage(group), cook_book)
    return score


if __name__ == "__main__":
    data = read_data(INPUT)
    splitted_data = split_elves_by_groups(data)
    print(get_final_score(splitted_data))
