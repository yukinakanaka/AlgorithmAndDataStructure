import math


def judge(threshold: int, a: int) -> bool:
    return a >= threshold


def lower_bound(a: list[int], key: int) -> int:
    left: int = 0
    right: int = len(a) - 1

    while right - left > 1:
        if judge(key, a[left]):
            return left

        mid: int = left + math.floor((right - left)/2)
        if judge(key, a[mid]):
            right = mid
        else:
            left = mid
    
    return right


if __name__ == '__main__':
    a: list[int] = [12, 43, 7, 15, 9]
    a_sorted: list[int] = sorted(a)

    result: list[int] = list()

    for i in a:
        result.append(lower_bound(a_sorted, i))

    print(a)
    print(a_sorted)
    print(result)
