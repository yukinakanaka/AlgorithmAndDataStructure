# ソートしてバイナリーサーチ

import bisect

if __name__ == "__main__":
    a: list[int] = [0, 3, 4, 1, 2]
    i: int = bisect.bisect_left(a, 3)
    print(f"{i}")

    a.reverse()
    j: int = bisect.bisect_left(a, 3)
    print(f"{j}")

