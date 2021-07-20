from typing import Final
from pprint import pprint

INF: Final[int] = 9999999999


def get_1d_array(i: int, default: int) -> list[list[int]]:
    return [default] * i


def chmin(a: int, b: int) -> int:
    if a > b:
        return b
    return a


if __name__ == '__main__':
    N: int = 5
    scores: list[list[int]] = [
        [0, 1, 2, 3, 4, 5, 6],
        [0, 0, 2, 3, 4, 5, 6],
        [0, 0, 0, 3, 4, 5, 6],
        [0, 0, 0, 0, 4, 5, 6],
        [0, 0, 0, 0, 0, 5, 6],
        [0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0],
    ]

    dp: list[list[int]] = get_1d_array(N, INF)
    dp[0] = 0

    for i in range(N):
        for j in range(i):
            print(f"{i},{j}")
            dp[i] = chmin(dp[i], dp[j] + scores[j][i])

    pprint(dp)
