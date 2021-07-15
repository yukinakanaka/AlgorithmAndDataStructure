from typing import Callable, Any, Optional


def log(f: Callable) -> Callable:

    def wrapped(*args, **kwargs):
        print(f"START {args} {kwargs}")
        result = f(*args, **kwargs)
        print(f"FINISH {args} {kwargs} {result}")
        return result

    return wrapped


def fibo() -> Callable[[int], int]:
    memo: list[int] = [-1] * 100

    @log
    def inner(x: int) -> int:
        if memo[x] != -1:
            return memo[x]
        if x == 0:
            memo[0] = 0
            return 0
        if x == 1:
            memo[1] = 1
            return 1

        result: int = inner(x - 1) + inner(x - 2)

        return result

    return inner


if __name__ == '__main__':
    fibo_func: Callable = fibo()

    n: int = 4
    ans = fibo_func(n)
    print(f"Answer: {ans}")
