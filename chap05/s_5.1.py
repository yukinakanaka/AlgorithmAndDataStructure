
def chmax(a: int, b: int) -> int:
    if a < b:
        return b
    return a


if __name__ == '__main__':
    N: int = 10
    a: list[int] = [3, 6, 3, 5, 7, 8, 1, 3, 4, 7, 8]
    b: list[int] = [1, 6, 3, 4, 3, 9, 1, 1, 4, 6, 3]
    c: list[int] = [6, 2, 3, 5, 4, 8, 2, 3, 2, 6, 9]

    dpa = [0] * N
    dpb = [0] * N
    dpc = [0] * N

    dpa[0] = a[0]
    dpb[0] = b[0]
    dpc[0] = c[0]

    for i in range(0, N - 1):
        dpa[i+1] = chmax(dpa[i+1], dpb[i] + a[i+1])
        dpa[i+1] = chmax(dpa[i+1], dpc[i] + a[i+1])

        dpb[i+1] = chmax(dpa[i+1], dpa[i] + b[i+1])
        dpb[i+1] = chmax(dpc[i+1], dpc[i] + b[i+1])

        dpc[i+1] = chmax(dpa[i+1], dpa[i] + c[i+1])
        dpc[i+1] = chmax(dpb[i+1], dpb[i] + c[i+1])

    max(dpa[N-1], dpb[N-1], dpc[N-1])
