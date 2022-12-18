from typing import List

INPUT = "day_06_input.txt"


def read_data(file_path: str) -> List[str]:
    """Read the data from file"""
    with open(file_path, 'r') as fin:
        data = fin.readlines()
    return data


def signal_decoder(input: str, window: int = 4) -> int:
    for i in range(len(input) - window + 1):
        chunk = input[i: i + window]
        # Я задание не читал, но в целом это выглядит неоптимально, что ты на каждый отрезок создаёшь
        # `set`, это очень похоже не классические алгоритмические задачи и решаться должно
        # несколько иначе
        if len(set(chunk)) == window:
            return i + window


if __name__ == "__main__":
    data = read_data(INPUT)
    print(signal_decoder(data[0]))
