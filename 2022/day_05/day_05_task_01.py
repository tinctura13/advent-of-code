from typing import List

INPUT = "day_05_input.txt"


def read_data(file_path: str) -> List[str]:
    """Read the data from file"""
    with open(file_path, 'r') as fin:
        data = fin.readlines()
    return data


def get_list_of_crates(data: List[str]) -> List[List[str]]:
    result = []
    n = 4  # chunk length
    for line in data[:8]:
        result.append([line[i:i+n].strip() for i in range(0, len(line), n)])
    all_crates = list(map(" ".join, zip(*reversed(result))))
    return [_.split() for _ in all_crates]


def make_action(command: str, crates: List[List[str]]) -> List[List[str]]:
    task = command.split()
    amount, from_, to = int(task[1]), int(task[3]), int(task[5])
    n = len(crates[from_ - 1]) - amount
    to_take = crates[from_ - 1][n:]
    crates[to - 1] += to_take[::-1]
    crates[from_ - 1] = crates[from_ - 1][:n]
    return crates


def get_top_crates(crates: List[List[str]]) -> str:
    return "".join([_[-1] for _ in crates]).replace("[", "").replace("]", "")


if __name__ == "__main__":
    data = read_data(INPUT)

    # get crates
    crates = get_list_of_crates(data[:9])

    # get commands
    commands = data[10:]

    # rearragne crates
    for command in commands:
        crates = make_action(command, crates)

    print(get_top_crates(crates))
