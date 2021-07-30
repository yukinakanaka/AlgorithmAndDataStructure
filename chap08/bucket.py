class Bucket:
    bucket: list[bool]

    def __init__(self, M: int) -> None:
        self.bucket = [False] * (M+1)

    def insert(self, a: int) -> None:
        self.bucket[a] = True

    def erase(self, a: int) -> None:
        self.bucket[a] = False

    def lookup(self, a: int) -> bool:
        return self.bucket[a]

    def __repr__(self) -> str:
        return self.bucket.__repr__()


if __name__ == '__main__':
    b: Bucket = Bucket(6)

    # 挿入 O(1)
    b.insert(5)
    b.insert(2)

    print(b)

    # 削除 O(1)
    b.erase(2)
    print(b)

    # 検索 O(1)
    print(b.lookup(5))
