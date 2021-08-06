from math import floor


def quick_sort(a: list[int], left: int, right: int) -> None:
    if (right - left) <= 1:
        return
    pivot: int = floor((right - left) / 2)
    v: int = a[pivot]

    # 右端とpivotを入れ替え
    a[pivot], a[right-1] = a[right-1], a[pivot]

    i: int = left
    j: int = left
    for j in range(left, right):
        if a[j] < v:
            a[i], a[j] = a[j], a[i]
            i += 1

    a[i], a[right-1] = a[right-1], a[i]
    quick_sort(a, left, i)
    quick_sort(a, i + 1, right)

    return


if __name__ == '__main__':
    a: list[int] = [5, 7, 2, 10, 8, 9]

    quick_sort(a, 0, len(a))

    print(a)
