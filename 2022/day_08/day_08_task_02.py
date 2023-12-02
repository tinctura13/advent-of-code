from typing import List

INPUT = "day_08_input.txt"


def read_data(file_path: str) -> List[List[int]]:
    """Read the data from file"""
    result: List = []
    with open(file_path, 'r') as fin:
        data = fin.readlines()
    for item in data:
        result.append([int(_) for _ in item.strip()])
    return result


def process_all_data(data: List) -> List[List[int]]:
    all_views: List = []
    for row in range(len(data[0])):
        for column in range(len(data)):
            cool_view: List = []
            data_above = [data[key][column] for key in range(row)][::-1]
            data_below = [data[key][column]
                          for key in range(row + 1, len(data))]
            data_left = data[row][:column][::-1]
            data_right = data[row][column + 1:]

            cool_view.append(process_direction(data, data_above, row, column))
            cool_view.append(process_direction(data, data_below, row, column))
            cool_view.append(process_direction(data, data_left, row, column))
            cool_view.append(process_direction(data, data_right, row, column))

            all_views.append(cool_view)
    return all_views


def process_direction(data: List, direction: List, row: int, column: int) -> int:
    cntr: int = 0
    for tree in direction:
        if data[row][column] > tree:
            cntr += 1
        else:
            cntr += 1
            return cntr
    return cntr


def process_view(data: List[int]) -> int:
    result = 1
    for item in data:
        result *= item
    return result


if __name__ == "__main__":
    data = read_data(INPUT)
    all_views = process_all_data(data)
    # get result
    print(max([process_view(_) for _ in all_views]))
