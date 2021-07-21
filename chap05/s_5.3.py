if __name__ == '__main__':
    a: list[int] = [3, 4, 6, 8]
    W: int = 22
    dp = [[False] * (W + 1) for i in range(len(a))]

    dp[0][0] = True
    dp[0][a[0]] = True

    results: set = set()

    for i in range(0, len(a) - 1):
        for w in range(0, W + 1):
            if dp[i][w]:
                dp[i + 1][w] = True
                results.add(w)
                if w + a[i + 1] <= W:
                    dp[i + 1][w + a[i + 1]] = True
                    results.add(w + a[i + 1])

    print(results)
