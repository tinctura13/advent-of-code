from typing import List

INPUT = "day_06_input.txt"


def read_data(file_path: str) -> List[str]:
    """Read the data from file"""
    with open(file_path, 'r') as fin:
        data = fin.readlines()
    return data


def signal_decoder(input: str) -> int:
    result: List = []
    counter: int = 0
    mark_len = 4
    for character in input.strip():
        result.append(character)
        if len(result) == mark_len and len(set(result)) == mark_len:
            print(f'start-of-packet marker is: {"".join(result)}')
            return counter
        elif len(result) == mark_len:
            result = result[3:]
        counter += 1
    return counter


if __name__ == "__main__":
    data = read_data(INPUT)
    print(signal_decoder(data[0]))
