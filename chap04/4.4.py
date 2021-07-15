
def GCD(x: int, y: int) -> int:
    print("{: 4d}, {: 4d} の公約数を調査します".format(x, y))
    r: int = x % y
    if r == 0:
        print("{: 4d}, {: 4d} の公約数は{: 4d}です".format(x, y, y))
        return y
    if r == 1:
        raise Exception("{:d}, {:d}の公約数はありません".format(x, y))

    result: int = GCD(y, r)
    print("{: 4d}, {: 4d} の公約数は{: 4d}です".format(x, y, result))
    return result


if __name__ == '__main__':
    GCD(100, 97)
