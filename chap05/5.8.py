from pprint import pprint


def get_2d_array(i: int, j: int, default: int) -> list[list[int]]:
    return [[default] * j for i in range(0, i)]


def chmin(current: int, challenger: int) -> int:
    if current > challenger:
        return challenger
    return current


if __name__ == '__main__':
    S: str = "logistic"
    T: str = "algorithm"

    INF = 9999999999
    result: list[list[int]] = get_2d_array(len(S) + 1, len(T) + 1, INF)

    result[0][0] = 0

    for i in range(0, len(S) + 1):
        for j in range(0, len(T) + 1):

            # 変更
            if i > 0 and j > 0:
                if S[i - 1] == T[j - 1]:
                    result[i][j] = chmin(result[i][j], result[i - 1][j - 1])
                else:
                    result[i][j] = chmin(result[i][j], result[i - 1][j - 1] + 1)

            # 削除
            if i > 0:
                result[i][j] = chmin(result[i][j], result[i - 1][j] + 1)

            # 追加
            if j > 0:
                result[i][j] = chmin(result[i][j], result[i][j - 1] + 1)

    pprint(result)
