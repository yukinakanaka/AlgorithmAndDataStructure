from typing import Callable, Any, Final
import math

INF: Final[int] = 9999999


def chmax(a: int, b: int) -> int:
    if a < b:
        return b
    return a


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


def is_larger(threshold: int, a: int) -> bool:
    if threshold <= a:
        return True
    return False


@log
def lower_bounder(threshold: int, a: list[bool]) -> int:
    left: int = 0
    right: int = len(a) - 1

    while right - left > 1:
        if is_larger(threshold, a[left]):
            return left

        mid: int = left + math.floor((right - left)/2)
        print(f"{threshold} | {mid} | {left} - {right}")
        if is_larger(threshold, a[mid]):
            right = mid
        else:
            left = mid
    return right


if __name__ == '__main__':

    a: list[int] = [2, 4, 5]
    M: int = 17
    S: set[int] = set()
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            S.add(a[i] + a[j])

    S = sorted(S)
    print(S)
    ans: int = 0
    for i in range(len(S)):
        index = lower_bounder(M-S[i], S)
        ans = chmax(ans, S[i] + S[index])
        print(f"ANS {ans} | {index} | {S[i]} {S[index]}")
