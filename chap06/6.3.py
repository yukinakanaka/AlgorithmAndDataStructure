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
    ans = 30
    if a < ans:
        return True
    return False

@log
def binary_search(a: list[bool]) -> int:
    left: int = 0
    right: int = len(a) - 1

    while right - left > 1:
        mid: int = left + math.ceil((right - left)/2)
        print(f"B {left} {mid} {right}")
        if check(a[mid]):
            left = mid
        else:
            right = mid
    return left


if __name__ == '__main__':
    a: list[int] = range(20, 37)

    print(f"{binary_search(a)}")
