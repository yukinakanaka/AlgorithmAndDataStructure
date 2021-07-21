if __name__ == '__main__':
    a: list[int] = [4, 5, 6, 8]
    W: int = 13
    dp = [[False] * (W + 1) for i in range(len(a))]

    k: int = 0
    while True:
        if a[0] * k <= W:
            dp[0][a[0] * k] = True
            k += 1
        else:
            break

    for i in range(0, len(a) - 1):
        for w in range(0, W + 1):
            if dp[i][w]:
                k: int = 0
                while True:
                    if w + a[i + 1] * k <= W:
                        dp[i + 1][w + a[i + 1] * k] = True
                        k += 1
                    else:
                        break

    [print(x, end="\t") for x in range(0, W + 1)]
    print("")
    for dpi in dp:
        [print(x, end="\t") for x in dpi]
        print("")

    # print(*dp, sep="\n")
