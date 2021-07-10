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


class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


def calc_dist(x1: float, y1: float, x2: float, y2: float):
    return math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)


if __name__ == "__main__":
    p1: Point = Point(0, 0)
    p2: Point = Point(3, 4)

    print(str(calc_dist(p1.x, p1.y, p2.x, p2.y)))
