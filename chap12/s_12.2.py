import bisect

if __name__ == '__main__':
    a: list[int] = [5, 3, 4, 1, 2]
    b: list[int] = [8, 5, 2, 3, 5]

    M: int = 10

    ra = sorted(a)
    sum: int = 0
    count: int = 0
    for x in ra:
        i: int = a.index(x)
        for _ in range(b[i]):
            sum += x
            count += 1
            if count == M:
                break
        else:
            continue
        break
    print(f"{count}")
    print(f"{sum}")
