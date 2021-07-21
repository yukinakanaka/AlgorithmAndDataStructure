if __name__ == '__main__':
    a: list[int] = [4, 5, 6, 8]
    m: list[int] = [2, 4, 1, 3]
    W: int = 13
    dp = [[False] * (W + 1) for i in range(len(a))]

    for k in range(0, m[0] + 1):
        if a[0] * k <= W:
            dp[0][a[0] * k] = True
        else:
            break

    for i in range(0, len(a) - 1):
        for w in range(0, W + 1):
            if dp[i][w]:
                for k in range(0, m[i] + 1):
                    if w + a[i + 1] * k <= W:
                        dp[i + 1][w + a[i + 1] * k] = True
                    else:
                        break

    [print(x, end="\t") for x in range(0, W + 1)]
    print("")
    for dpi in dp:
        [print(x, end="\t") for x in dpi]
        print("")

    # print(*dp, sep="\n")
