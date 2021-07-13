from typing import Final

FIND_NUMBER: Final[int] = 7
NUMBER_LIST: list[int] = [9, 2, 4, 5, 7]

INFINITY: Final[int] = 999999999999999

if __name__ == '__main__':
    print("START")

    exit: bool = False
    fount_id: int = -1
    min_value: int = INFINITY

    for i, number in enumerate(NUMBER_LIST):
        if min_value > number:
            min_value = number

        if number == FIND_NUMBER:
            fount_id = i
            exit = True

    print("RESULT")
    print("exit={}, found_id={}, min_value={}".format(exit, str(fount_id), str(min_value)))
    print("END")
