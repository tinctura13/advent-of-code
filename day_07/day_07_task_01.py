from typing import List, Dict

INPUT = "day_07_input.txt"


def read_data(file_path: str) -> List[str]:
    """Read the data from file"""
    with open(file_path, 'r') as fin:
        data = fin.readlines()
    return data


def parse_commands(logs: List[str]) -> Dict:
    dirs_size: Dict = {}
    all_dirs: List = []

    for command in logs:
        command = command.split()
        if command[0] == "$":
            if command[1] == "cd":
                if command[2] == "..":
                    all_dirs = all_dirs[:-1]
                elif command[2] == "/":
                    all_dirs = ["/"]
                else:
                    all_dirs.append(command[2])
        else:
            if command[0] != "dir":
                current_path = ""
                for folder in all_dirs:
                    if current_path != "/" and folder != "/":
                        current_path += "/"
                    current_path += folder
                    dirs_size[current_path] = dirs_size.get(
                        current_path, 0) + int(command[0])
    return dirs_size


if __name__ == "__main__":
    data = read_data(INPUT)
    data = [_.strip() for _ in data]

    dirs_size = parse_commands(data)

    print(
        f"Part 1 solution: {sum(v for k, v in dirs_size.items() if v < 100000)}")

    required_space = 30000000 - (70000000 - dirs_size.get("/"))
    print(
        f"Part 2 solution: {min(v for k, v in dirs_size.items() if v >= required_space)}")
