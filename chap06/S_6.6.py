from math import floor, sin, pi

A: int = 4
B: int = 5
C: int = 7

INF: float = 1000000


class Result:
    is_ans: bool
    is_pos: bool

    def __init__(self, is_ans, is_pos) -> None:
        self.is_ans = is_ans
        self.is_pos = is_pos


def judge(t: float) -> Result:
    v: float = A * t + B * sin(C * t * pi) - 100
    print(f"V: {t} | {v} ")
    is_ans: bool = False
    if abs(v) <= pow(10, -12):
        is_ans = True

    if v > 0:
        return Result(is_ans, True)
    else:
        return Result(is_ans, False)


if __name__ == '__main__':
    left: float = 0
    right: float = INF

    while right - left > 0:
        mid: int = left + (right - left)/2
        if judge(mid).is_ans:
            print(f"{left} - {right}\t|\t{mid}\t|\tANS")
            break

        if judge(mid).is_pos:
            print(f"{left} - {right}\t|\t{mid}\t|\tPOS")
            right = mid
        else:
            print(f"{left} - {right}\t|\t{mid}\t|\tNEG")
            left = mid

    print(f"answer: {mid}")