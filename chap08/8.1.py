

if __name__ == '__main__':
    a: list[int] = [4, 5, 6, 1, 3, 5, 6]
    
    # アクセス O(1)
    print(f"{a[0]}")
    print(f"{a[2]}")
    a[2] = 3
    print(f"{a[2]}")

    # 挿入 O(N)
    a.insert(2, 9)
    print(f"{a}")

    # 削除 O(N)
    a.remove(4)
    print(f"{a}")
