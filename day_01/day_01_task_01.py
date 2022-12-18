from typing import List

INPUT = "day_01_input.txt"


def read_data(file_path: str) -> List[str]:
    """Read the data from file"""
    with open(file_path, 'r') as fin:
        data = fin.readlines()
    return data


def get_list_of_elves(data: List[str]) -> List[List[str]]:
    # Использовать `_` для малозначительных переменных неверно
    # обычно `_` именуются неиспользуемые вещи, а для таких вещей либо `x`
    # либо первая буква полного слова по смыслу, 
    # либо полное слово (особенно актуально, когда несколько пременных)
    return [_.split("\n") for _ in "".join(data).strip().split("\n\n")]


def get_total_for_each_elve(arr: List[List[str]]) -> List[int]:
    # Эта функция по идее уже выполняет непосредственную работу со смысловой нагрузкой
    # aka бизнес логика / доменная логика, поэтому принимать сюда список строк
    # и приводить строки в числу здесь неверно, это должно делаться в функции чтения данных
    # То есть логика такая, что есть внешняя среда для программы и есть внутренняя логика
    # и внутри должны быть правильные типы, а все преобразования происходить при получении
    # из внешнего мира или при передаче в него, то есть в строго изолированных местах
    # в данном случае это должно было быть в `get_list_of_elves`
    return [sum([int(item) for item in _]) for _ in arr]


if __name__ == "__main__":
    data = read_data(INPUT)
    list_of_elves = get_list_of_elves(data)
    total_cal_for_each_elve = get_total_for_each_elve(list_of_elves)
    print(max(total_cal_for_each_elve))
