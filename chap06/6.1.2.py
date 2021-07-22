from typing import Callable
import math


def log(f: Callable) -> Callable:
    count: int = 0

    def inner(*args, **kwargs) -> Callable:
        nonlocal count
        count += 1
        print(f"START {f.__name__} {count} {args} {kwargs}")
        result = f(*args, **kwargs)
        print(f"FINISH {f.__name__} {count} {args} {kwargs} {result}")
        return result

    return inner


@log
def binary_search(a: list[int], key: int) -> int:
    left: int = 0
    right: int = len(a) - 1

    while right >= left:
        mid: int = left + math.ceil((right - left)/2)
        print(f"B {left} {mid} {right}")
        if a[mid] == key:
            return mid
        elif a[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
        print(f"A {left} {mid} {right}")
    return -1


if __name__ == '__main__':
    a: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    key: int = 2

    print(f"{binary_search(a, key)}")
