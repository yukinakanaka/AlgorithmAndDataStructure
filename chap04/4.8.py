import typing


def log(f: typing.Callable) -> typing.Callable:
    """ログを出力するデコレーター

    Args:
        f (typing.Callable): [description]

    Returns:
        typing.Callable: [description]
    """
    def inner(*args, **kwargs):
        print("{} START.\targs: {}, kwargs: {}".format(f.__name__, args, kwargs))
        result = f(*args, **kwargs)
        print("{} FINISH.\targs: {}, kwargs: {}, reulst: {:d}".format(f.__name__, args, kwargs, result))
        return result

    return inner


@log
def fibo(n: int, memo: list[int]) -> int:
    if memo[n-1] is not None:
        print(f"{n} already calc")
        return memo[n-1]
    if n == 1:
        memo[1] = 1
        return 1
    if n == 0:
        memo[0] = 0
        return 0
    return fibo(n-1, memo) + fibo(n-2, memo)


if __name__ == '__main__':
    n: int = 5
    memo: list[typing.Optional[int]] = [None] * n

    result: int = fibo(n, memo)
    print(f"Result: {result}")
