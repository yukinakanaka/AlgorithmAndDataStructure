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


def is_higher(threshold: int, a:int) -> bool:
    if threshold < a:
        return True
    return False

@log
def lower_bound(a: list[int], threshold: float) -> int:
    left: int = 0
    right: int = len(a) - 1

    while right - left > 1:
        mid: int = left + math.ceil((right - left)/2)
        print(f"{threshold} | {mid} | {left} - {right}")
        if is_higher(threshold, a[mid]):
            right = mid
        else:
            left = mid
    return left


if __name__ == '__main__':
    a: list[int] = range(0, 37)
    threshold: float = 20
    print(f"{lower_bound(a, threshold)}")
