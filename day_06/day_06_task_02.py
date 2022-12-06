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
    mark_len: int = 14
    for character in input.strip():
        result.append(character)
        if len(set(result)) == mark_len:
            counter += 1
            return counter
        elif len(result) == mark_len:
            result = result[1:]
        counter += 1
    return counter


if __name__ == "__main__":
    data = read_data(INPUT)
    assert signal_decoder('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 19
    assert signal_decoder('bvwbjplbgvbhsrlpgdmjqwftvncz') == 23
    assert signal_decoder('nppdvjthqldpwncqszvftbrmjlhg') == 23
    assert signal_decoder('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 29
    assert signal_decoder('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26
    print(signal_decoder(data[0]))
