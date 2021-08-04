# insertion sort（挿入ソート）

def insertion_sort(a: list[int]) -> None:
    for i in range(1, len(a)):
        v: int = a[i]

        # 挿入する場所jを探す
        j: int = i
        while j > 0:
            if a[j - 1] > v:
                a[j] = a[j - 1]  # vより大きいものは1つ後ろに移す
            else:
                break
            j -= 1
        a[j] = v
        print(a)


if __name__ == '__main__':
    a: list[int] = [5, 9, 2, 0, 4]

    insertion_sort(a)

    print(a)
