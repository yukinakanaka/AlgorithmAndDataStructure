def func(num: int) -> None:
    print("{:d}".format(num))
    if num > 1:
        func(num - 1)


def sum_func(num: int):
    if num == 0:
        return 0
    return num + sum_func(num - 1)


if __name__ == '__main__':
    func(3)
    print("{:d}".format(sum_func(3)))
