INPUT = "day_02_input.txt"

# 0 if you lost, 3 if the round was a draw, and 6 if you won
# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# 1 for Rock, 2 for Paper, and 3 for Scissors

scores = {
    "['A', 'X']": 3,  # lost  0 + 3 = 3
    "['A', 'Y']": 4,  # draw  3 + 1 = 4
    "['A', 'Z']": 8,  # won   6 + 2 = 8
    "['B', 'X']": 1,  # lost  0 + 1 = 1
    "['B', 'Y']": 5,  # draw  3 + 2 = 5
    "['B', 'Z']": 9,  # won   6 + 3 = 9
    "['C', 'X']": 2,  # lost  0 + 2 = 2
    "['C', 'Y']": 6,  # draw  3 + 3 = 6
    "['C', 'Z']": 7,  # won   6 + 1 = 7
}


def read_data(file):
    """Read the data from file"""
    result = []
    with open(file, 'r') as fin:
        data = fin.readlines()
    for item in data:
        result.append(item.strip().split())
    return result


def calculate_points(data):
    points = 0
    for item in data:
        points += scores[str(item)]
    return points


if __name__ == "__main__":
    data = read_data(INPUT)
    print(calculate_points(data))
