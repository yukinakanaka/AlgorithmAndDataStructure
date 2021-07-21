from statistics import mean


def chmax(a: int, b: int) -> int:
    if a < b:
        return b
    return a


def get_2d_array(i: int, j: int) -> list[list[int]]:
    return [[0] * j for x in range(0, i)]


if __name__ == '__main__':
    a: list[int] = [4, 5, 6, 7, 2, 3, 4, 5]
    M: int = 4

    dp: list[list[int]] = get_2d_array(len(a), M)

    for n in range(0, len(a)):
        for m in range(1, M + 1):
            if m == 1:
                dp[n][0] = mean(a[0:n+1])
            if m >= 2:
                # N番目が1つで1区間の場合
                dp[n][m - 1] = chmax(dp[n][m - 1], dp[n - 1][m - 2] + a[n])
            if m > 0:
                for i in range(m - 1, n):
                    dp[n][m - 1] = chmax(dp[n][m - 1], dp[i]
                                         [m - 2] + mean(a[i:n+1]))

    for array in dp:
        [print(f"{num}", end="\t") for num in array]
        print()
