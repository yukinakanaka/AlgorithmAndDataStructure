from util import logging
from typing import Callable


def calc_min() -> Callable[[int, list[int]], int]:
    memo: list[int] = [-1] * 100

    @logging.log
    def func(n: int, heights: list[int]) -> int:
        if memo[n] != -1:
            print("memo")
            return memo[n]
        if n == 0:
            memo[0] = 0
            return memo[0]
        if n == 1:
            memo[1] = abs(heights[1] - heights[0])
            return memo[1]

        t1: int = func(n - 1, heights) + abs(heights[n] - heights[n-1])
        t2: int = func(n - 2, heights) + abs(heights[n] - heights[n-2])

        memo[n] = min(t1, t2)
        print(memo[:len(heights)])
        return memo[n]

    return func


if __name__ == '__main__':
    f = calc_min()

    heights: list[int] = [2, 9, 4, 5, 1, 6, 10]
    ans = f(len(heights) - 1, heights)
    print(f"Answer: {ans}")
