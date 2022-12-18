INPUT = "day_02_input.txt"

# 0 if you lost, 3 if the round was a draw, and 6 if you won
# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# 1 for Rock, 2 for Paper, and 3 for Scissors
scores = {
    # Это конечно так работает, но это неправильно в качестве ключа использовать
    # строковое представление списка или любой другой фигни,
    # вместо этого можно было использовать tuple:
    # ("A", "X"), ("A", "Y") и т.п.
    # Строковые представления нужны только для целей отладки/отображения,
    # на них нельзя строить логику, потому что они могут меняться в зависимости от версии
    # или ещё чего
    "['A', 'X']": 4,  # draw 3 + 1 = 4
    "['A', 'Y']": 8,  # won  6 + 2 = 8
    "['A', 'Z']": 3,  # lost 0 + 3 = 3
    "['B', 'X']": 1,  # lost 0 + 1 = 1
    "['B', 'Y']": 5,  # draw 3 + 2 = 5
    "['B', 'Z']": 9,  # won  6 + 3 = 9
    "['C', 'X']": 7,  # won  6 + 1 = 7
    "['C', 'Y']": 2,  # lost 0 + 2 = 2
    "['C', 'Z']": 6,  # draw 3 + 3 = 6
}


def read_data(file):
    """Read the data from file"""
    result = []
    with open(file, 'r') as fin:
        data = fin.readlines()
    for item in data:
        # Тут надо обернуть `item.strip().split()` в `tuple`
        result.append(item.strip().split())
    return result


def calculate_points(data):
    points = 0
    for item in data:
        # `str` тут надо убрать, а в data уже должны быть таплы
        points += scores[str(item)]
    return points


if __name__ == "__main__":
    data = read_data(INPUT)
    print(calculate_points(data))
