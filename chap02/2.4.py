# 残念なことに、ほとんどの小数は 2 進法の分数として正確に表わすことができません。
# その結果、一般に、入力した 10 進の浮動小数点数は、 2 進法の浮動小数点数で近似された後、実際にマシンに記憶されます。

# 近年の殆どのコンピュータでは float 型は、最上位ビットから数えて最初の 53 ビットを分子、2 の冪乗を分母とした、二進小数で近似されます。

# >>> 0.1 + 0.1 + 0.1
# 0.30000000000000004
# >>> 0.1 + 0.1 + 0.1 == 0.3
# False

# 正確な10進数表現が必要となるような場合には、 decimal モジュールを利用してみてください。
# このモジュールは会計アプリケーションや高精度の計算が求められるアプリケーションに適した、10進数の計算を実装しています。

# >>> Decimal(0.1) + Decimal(0.1) + Decimal(0.1)
# Decimal('0.3000000000000000166533453694')

import math
from typing import Final

MAX_VALUE: Final[float] = 99999999999999

class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

def calc_dist(p1: Point, p2: Point):
    return math.sqrt((p1.x-p2.x) ** 2 + (p1.y-p2.y) ** 2)

if __name__ == "__main__":
    point_list: list[Point] = []
    point_list.append(Point(0, 0))
    point_list.append(Point(3, 4))
    point_list.append(Point(1, 1))
    point_list.append(Point(10, 2))

    min_distance: float = MAX_VALUE

    for i in range(len(point_list)):
        for j in range(i + 1, len(point_list)):
            print("{},{}".format(str(i), str(j)))
            if min_distance > calc_dist(point_list[i], point_list[j]):
                min_distance = calc_dist(point_list[i], point_list[j])

    print(min_distance)
