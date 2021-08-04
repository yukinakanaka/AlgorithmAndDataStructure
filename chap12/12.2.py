# マージソート
# in-placeではない
from math import floor


def merge_sort(a: list[int]) -> list[int]:
    if len(a) == 1:
        return a

    mid: int = floor(len(a) / 2)
    left: list[int] = merge_sort(a[:mid]) # in-placeではない
    right: list[int] = merge_sort(a[mid:])
    right.reverse()

    left.extend(right)

    result: list[int] = []
    while len(left) > 0:
        if left[0] < left[-1]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(left[-1])
            left = left[:-1]

    return result


if __name__ == '__main__':
    a: list = [3, 4, 5, 2, 1]
    print(merge_sort(a))
