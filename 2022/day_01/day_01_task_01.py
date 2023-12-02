from typing import List

INPUT = "day_01_input.txt"


def read_data(file_path: str) -> List[str]:
    """Read the data from file"""
    with open(file_path, 'r') as fin:
        data = fin.readlines()
    return data


def get_list_of_elves(data: List[str]) -> List[List[str]]:
    return [_.split("\n") for _ in "".join(data).strip().split("\n\n")]


def get_total_for_each_elve(arr: List[List[str]]) -> List[int]:
    return [sum([int(item) for item in _]) for _ in arr]


if __name__ == "__main__":
    data = read_data(INPUT)
    list_of_elves = get_list_of_elves(data)
    total_cal_for_each_elve = get_total_for_each_elve(list_of_elves)
    print(max(total_cal_for_each_elve))
