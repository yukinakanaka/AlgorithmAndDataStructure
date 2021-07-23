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

@log
def judge(a: list[int], min_dist: int, count: int) -> bool:
    """リストから、count数の小屋を選ぶ時、min_dist以上を保てるかどうか？
    min_dist以上になったら選ぶ操作を行い、count数を超えた次点でTrueを返す

    Args:
        a (list[int]): [description]
        min_dist (int): [description]
        count (int): [description]

    Returns:
        bool: [description]
    """
    for start_index in range(len(a) - count + 1):
        current: int = a[start_index]
        choosed_count: int = 1
        for i in range(start_index + 1, len(a)):
            # print(f"START {a[i]} {count}")
            if a[i] - current >= min_dist:
                current = a[i]
                choosed_count += 1
                if choosed_count >= count:
                    # print(f"FINISH {a[i]} {count} {True}")
                    return True
    # print(f"FINISH {a[i]} {count} {False}")
    return False


def higher_bounder(a: list[int], count: int) -> int:
    left: int = 0
    right: int = a[-1] - 1
    if judge(a, right, count):
        return right

    while right - left > 1:
        mid: int = left + math.floor((right - left)/2)
        
        if judge(a, mid, count):
            print(f"{mid} | {True} | {left} - {right}")
            left = mid
        else:
            print(f"{mid} | {False} | {left} - {right}")
            right = mid
    return left


if __name__ == '__main__':

    a: list[int] = [2, 4, 5, 6, 8]
    M: int = 2

    print(f"{higher_bounder(a, M)}")
