from typing import Final

FIND_NUMBER: Final[int] = 7
NUMBER_LIST: list[int] = [9, 2, 4, 5]

if __name__ == '__main__':
    print("START")

    exit: bool = False
    for i in NUMBER_LIST:
        if i == FIND_NUMBER:
            exit = True

    print("RESULT: {}".format(exit))
    print("END")
