from typing import Callable, Any
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


def check(a: Any) -> bool:
    return a

@log
def binary_search(a: list[bool]) -> int:
    left: int = 0
    right: int = len(a) - 1

    while right - left > 1:
        mid: int = left + math.ceil((right - left)/2)
        print(f"B {left} {mid} {right}")
        if check(a[mid]):
            right = mid
        else:
            left = mid
    return right


if __name__ == '__main__':
    a: list[bool] = [False, False, False, True, True, True, True, True, True, True, True, True]

    print(f"{binary_search(a)}")
