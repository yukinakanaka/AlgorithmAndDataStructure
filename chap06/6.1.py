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
def binary_search(start: int, a: list[int], key: int) -> int:
    if len(a) == 0:
        return -1

    mid: int = math.ceil(len(a)/2)
    print(f"mid: {mid}")

    if a[mid-1] == key:
        return mid + start
    elif mid > key:
        return binary_search(0, a[:mid-1], key) + start
    else:
        return binary_search(mid, a[mid:], key) + start


if __name__ == '__main__':
    a: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    key: int = 10

    print(f"{binary_search(0, a, key)}")
