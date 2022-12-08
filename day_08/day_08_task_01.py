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


def get_inner_visible_trees(data: List) -> int:
    visible_trees: int = 0
    visible: List = []
    for row in range(1, len(data[0]) - 1):
        for column in range(1, len(data) - 1):
            data_above = [data[key][column] for key in range(row)]
            data_below = [data[key][column]
                          for key in range(row + 1, len(data))]

            # check left
            if data[row][column] > max(data[row][:column]):
                visible.append((row, column))
                visible_trees += 1

            # ckeck right
            elif data[row][column] > max(data[row][column + 1:]):
                visible.append((row, column))
                visible_trees += 1

            # check above
            elif data[row][column] > max(data_above) and (row, column) not in visible:
                visible.append((row, column))
                visible_trees += 1

            # check below:
            elif data[row][column] > max(data_below) and (row, column) not in visible:
                visible.append((row, column))
                visible_trees += 1
    return visible_trees


if __name__ == "__main__":
    data = read_data(INPUT)
    visible_trees = get_inner_visible_trees(data)
    result = len(data) * 2 + len(data[0][2:]) * 2
    print(result + visible_trees)
