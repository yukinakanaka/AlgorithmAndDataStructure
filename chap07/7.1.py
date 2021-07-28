import math
coin_value = (500, 100, 50, 10, 5, 1)

if __name__ == '__main__':
    X: int = 874
    # 枚数制限
    a: list[int] = [1, 5, 0, 8, 3, 9]

    # 結果
    result: list[int] = []

    # 貪欲法
    for i, v in enumerate(coin_value):
        add: int = math.floor(X / v)

        if (add > a[i]):
            add = a[i]

        X = X - v * add
        result.append(add)

    print(result)
