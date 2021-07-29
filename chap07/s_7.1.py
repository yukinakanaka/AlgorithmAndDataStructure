from array import array


class Pair:
    a: int
    b: int

    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def __repr__(self) -> str:
        return f"({self.a:2d}, {self.b:2d})"


if __name__ == '__main__':
    A: array = array("i", [4, 7, 8, 2, 5, 9, 10])
    B: array = array("i", [2, 5, 3, 9, 10, 4, 5])

    A_sorted = sorted(A)
    B_sorted = sorted(B)

    result: list[Pair] = list()
    print(A_sorted)
    print(B_sorted)
    for a in A_sorted:
        for b in B_sorted:
            if b > a:
                result.append(Pair(a, b))
                B_sorted.remove(b)
                break
        else:
            continue

    for pair in result:
        print(pair)

