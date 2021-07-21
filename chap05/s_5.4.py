from pprint import pprint
from typing import Final
INF: Final[int] = 999


def chmin(a: int, b: int) -> int:
    if a > b:
        return b
    return a


if __name__ == '__main__':
    a: list[int] = [3, 4, 6, 8]
    W: int = 13
    k: int = 2
    dp: list[list[int]] = [[INF] * (W + 1) for i in range(len(a))]

    dp[0][0] = 0
    dp[0][a[0]] = 1

    for i in range(0, len(a) - 1):
        for w in range(0, W + 1):
            if dp[i][w] != INF:
                dp[i + 1][w] = chmin(dp[i + 1][w], dp[i][w])
                if w + a[i + 1] <= W:
                    if dp[i][w] + 1 <= k:
                        dp[i + 1][w + a[i + 1]] = chmin(dp[i + 1][w + a[i + 1]], dp[i][w] + 1)

    # print(*dp, sep="\n")
    pprint(dp, width=100)
