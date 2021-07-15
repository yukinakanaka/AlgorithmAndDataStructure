# 分割当時法 divide-and-conquer method
# 部分問題に文化し、各部分問題を再起的に解き、それらの解を組み合わせて元の問題の解の構成するアルゴリズム
# →再帰的アルゴリズムになる
# →メモ化は動的計画法の一種

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
        print("{} FINISH.\targs: {}, kwargs: {}, reulst: {}".format(
            f.__name__, args, kwargs, result))
        return result

    return inner


@log
def func(w: int, num_set: list[int]) -> bool:
    if w > sum(num_set):
        return False
    if len(num_set) == 0:
        if w == 0:
            return True
        else:
            return False
    return func(w - num_set[-1], num_set[:-1]) or func(w, num_set[:-1])

if __name__ == '__main__':
    # num_set: list[int] = [3, 2, 6, 5]
    # w: int = 14

    # result: bool = func(w, num_set)
    # print(f"Result: {result}")

    num_set: list[int] = [6, 5, 2, 3]
    w: int = 14

    result: bool = func(w, num_set)
    print(f"Result: {result}")