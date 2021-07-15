from typing import Callable


def wrap_func(func: Callable[[int], int]) -> None:
    print("start")
    func()
    print("end")


def fibo(n: int):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fibo(n - 1) + fibo(n - 2)


if __name__ == '__main__':
    print("{:d}".format(wrap_func(fibo(5))))
