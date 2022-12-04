from typing import List

INPUT = "day_04_input.txt"


def read_data(file_path: str) -> List[str]:
    """Read the data from file"""
    with open(file_path, 'r') as fin:
        data = fin.readlines()
    return data
