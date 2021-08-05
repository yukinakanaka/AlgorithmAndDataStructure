from typing import Final

MAX: int = 100


def bucket_sort(a: list[int]) -> None:
    bucket: list[int] = [0] * MAX

    # 各数の個数を数える
    for i in range(len(a)):
        bucket[a[i]] += 1

    # 累計の場合の個数を数える≒index
    cum: list[int] = [0] * MAX
    sum: int = 0
    for i in range(MAX):
        sum += bucket[i]
        cum[i] = sum

    # cumを元にindexを決めて詰めていく
    result: list[int] = [0] * len(a)
    for e in a:
        cum[e] -= 1
        index = cum[e]
        result[index] = e

    return result


if __name__ == '__main__':
    a: list[int] = [5, 3, 2, 5, 6, 7, 10, 4]
    print(bucket_sort(a))

