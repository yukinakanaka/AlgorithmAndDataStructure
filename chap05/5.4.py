from util.logging import log
from pprint import pprint


class Stuff:
    weight: int
    value: int

    def __init__(self, weight: int, value):
        self.weight = weight
        self.value = value


def get_2d_array(i: int, j: int) -> list[list[int]]:
    # result: list[list[int]] = []
    # for i in range(0, i):
    #     result.append([0] * j)

    # return result

    return [[0] * j for i in range(0, i)]


@log
def knapsack(stuffs: list[Stuff], values: list[list[int]]) -> int:
    for i in range(1, len(values)):
        for j in range(1, len(values[0])):
            # i番目のスタッフを選ばなかった場合
            values[i][j] = chmax(values[i][j], values[i - 1][j])

            # i番目のスタッフを選ぶ場合
            if j - stuffs[i - 1].weight >= 0:
                values[i][j] = chmax(values[i][j], values[i - 1][j - stuffs[i - 1].weight] + stuffs[i - 1].value)

    return values


def chmax(default: int, challenger: int) -> int:
    if default < challenger:
        return challenger
    return default


if __name__ == '__main__':
    stuffs: list[Stuff] = [
        Stuff(2, 3),
        Stuff(1, 2),
        Stuff(3, 6),
        Stuff(2, 1),
        Stuff(1, 3),
        Stuff(5, 85)
    ]

    values: list[list[int]] = get_2d_array(len(stuffs) + 1, 20 + 1)

    result: int = knapsack(stuffs, values)
