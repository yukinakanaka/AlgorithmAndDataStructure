# 2重ループは、N^2
# 10,000^2 = 10^8 以下であればあまり問題ない
from typing import Final

SET1: set[int] = {1, 4, 5}
SET2: set[int] = {3, 4, 9}
INF: Final[int] = 999999999

if __name__ == '__main__':
    min = INF
    for num1 in SET1:
        for num2 in SET2:
            if num1 + num2 > 10 and min > num1 + num2:
                min = num1 + num2
    
    print("Result: {}".format(str(min)))
