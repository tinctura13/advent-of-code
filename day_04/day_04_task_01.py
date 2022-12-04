from typing import List, Tuple

INPUT = "day_04_input.txt"


def read_data(file_path: str) -> List[str]:
    """Read the data from file"""
    with open(file_path, 'r') as fin:
        data = fin.readlines()
    return data


def get_clean_pair(raw_pair: str) -> Tuple:
    clean_pair = [_.split("-") for _ in raw_pair.strip().split(",")]
    return [int(_) for _ in clean_pair[0]], [int(_) for _ in clean_pair[1]]


def count_full_pairs(all_pairs: List[str]) -> int:
    counter = 0
    for pair in all_pairs:
        l, r = get_clean_pair(pair)
        if l[0] <= r[0] and l[1] >= r[1] or l[0] >= r[0] and l[1] <= r[1]:
            counter += 1
    return counter


if __name__ == "__main__":
    data = read_data(INPUT)
    print(count_full_pairs(data))
