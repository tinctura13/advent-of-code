from typing import List, TextIO

INPUT = "day_04_input.txt"


def read_data(file: TextIO) -> List:
    """Read the data from file"""
    data = []
    with open(file, 'r') as fin:
        data = fin.readlines()
    return data
