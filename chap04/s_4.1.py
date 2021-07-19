import typing


def log(f: typing.Callable) -> typing.Callable:
    """ログ出力用のデコレータ

    Args:
        f (typing.Callable): [description]

    Returns:
        typing.Callable: [description]
    """
    called_count: int = 0

    def wrapped(*args, **kwargs):
        nonlocal called_count
        called_count += 1
        print(f"START\t{f.__name__}\t{args}\t{kwargs}\tcount:\t{called_count}")
        result = f(*args, **kwargs)
        print(f"FINISH\t{f.__name__}\t{args}\t{kwargs}\tresult:\t{result}")
        return result

    return wrapped


@log
def tri(n: int, memo: list[int]) -> int:
    """トリボナッチ数列の関数

    Args:
        n (int): [description]
        memo (list[typing.Optional[int]]): [description]

    Returns:
        int: [description]
    """
    if memo[n] is not None:
        return memo[n]
    elif n == 0:
        memo[0] = 0
        return 0
    elif n == 1:
        memo[1] = 0
        return 0
    elif n == 2:
        memo[2] = 1
        return 1

    result = tri(n - 1, memo) + tri(n - 2, memo) + tri(n - 3, memo)
    memo[n] = result
    return result


if __name__ == '__main__':
    n: int = 5
    memo: list[typing.Optional[int]] = [None] * (n + 1)
    tri(n, memo)
