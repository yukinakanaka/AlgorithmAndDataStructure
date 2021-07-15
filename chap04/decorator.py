import typing

# クロージャー
# 関数の定義時の自分のスコープの情報を記憶する


def function1(x: int) -> typing.Callable:
    z: int = 10

    def inner(y: int) -> None:
        print("{:d}".format(x + y + z))
    return inner

# デコレーター
# 関数の定義時の自分のスコープの情報を記憶する


def log(f: typing.Callable) -> typing.Callable:
    def inner(*args, **kwargs):
        print("{} START.".format(f.__name__))
        result = f(*args, **kwargs)
        print("{} END.".format(f.__name__))
        return result

    return inner


def add(x: int, y: int) -> int:
    return x + y


@log
def sub(x: int, y: int) -> int:
    return x - y


if __name__ == '__main__':
    inner1 = function1(1)
    print(inner1.__closure__)
    inner1(2)

    add_log = log(add)
    res1 = add_log(3, 4)
    print("{:d}".format(res1))

    print("{:d}".format(sub(10, 2)))
