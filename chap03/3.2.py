from typing import Final

FIND_NUMBER: Final[int] = 7
NUMBER_LIST: list[int] = [9, 2, 4, 5, 7]

if __name__ == '__main__':
    print("START")

    fount_id: int = -1

    exit: bool = False
    for i, number in enumerate(NUMBER_LIST):
        if number == FIND_NUMBER:
            fount_id = i
            exit = True

    print("RESULT")
    print("exit={}, found_id={}".format(exit, str(fount_id)))
    print("END")
