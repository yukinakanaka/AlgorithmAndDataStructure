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
def judge(x: int, K: int, a: list[int], b: list[int]) -> bool:
    for i in a:
        count: int = 0
        for j in b:
            if i * j <= x:
                count += 1
        if count >= K:
            return True

    return False


if __name__ == '__main__':
    a: list[int] = [3, 5, 6, 8]
    b: list[int] = [2, 3, 5, 6]

    K: int = 2

    left = 0
    right = a[-1] * b[-1]
    while right - left > 1:
        mid: int = math.floor(left + (right - left) / 2)
        if judge(mid, K, a, b):
            print(f"{mid} is True | {left} - {right}")
            right = mid
        else:
            print(f"{mid} is False | {left} - {right}")
            left = mid
    print(f"{right}")
