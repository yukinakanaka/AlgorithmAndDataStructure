class UnionFind:
    par: list[int]
    siz: list[int]

    def __init__(self, x: int) -> None:
        """初期化
        全頂点の数を指定して初期化する。全ての頂点が別のグループに属している形で初期化する。

        Args:
            x (int): 頂点の数
        """
        self.par = [-1] * x
        self.siz = [1] * x

    def root(self, x: int) -> int:
        """頂点xが属する根付き木の根の番号を返す関数
        • 再帰的に探索する。
        • 圧縮処理も実行している。

        Args:
            x (int): 頂点xの番号

        Returns:
            int: 頂点xが属する根付き木の根の番号

        """
        if self.par[x] == -1:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def size(self, x: int) -> int:
        return self.siz[x]

    def issame(self, x: int, y: int) -> bool:
        if self.root(x) == self.root(y):
            return True
        else:
            return False

    def unite(self, x: int, y: int) -> bool:
        xr: int = self.root(x)
        yr: int = self.root(y)
        if xr == yr:
            return bool

        if self.size(xr) > self.size(yr):
            self.par[yr] = xr
            self.siz[xr] = self.size(xr) + self.size(yr)
        else:
            self.par[xr] = yr
            self.siz[yr] = self.size(xr) + self.size(yr)

        return True

    def get_connected_graph_count(self) -> int:
        count: int = 0
        for i, _ in enumerate(self.par):
            if self.root(i) == i:
                count += 1
        return count

    def print_groups(self):
        groups: dict = {}
        for i, _ in enumerate(self.par):
            if self.root(i) in groups:
                groups[self.root(i)].append(i)
            else:
                groups[self.root(i)] = [i]
        print(groups)


if __name__ == '__main__':

    cities_num: int = 8

    rails: list[tuple[int]] = [
        (1, 2),
        (2, 5),
        (3, 0)
    ]
    rail_cf: UnionFind = UnionFind(cities_num)
    for rail in rails:
        rail_cf.unite(*rail)

    roads: list[tuple[int]] = [
        (1, 5),
        (4, 3),
        (2, 1),
        (7, 2)
    ]
    road_cf: UnionFind = UnionFind(cities_num)
    for road in roads:
        road_cf.unite(*road)

    count_list: list = [0] * cities_num
    for i in range(cities_num):
        count: int = 0
        for j in range(cities_num):
            if i == j:
                pass
            if rail_cf.issame(i, j) and road_cf.issame(i, j):
                count += 1
        count_list[i] = count

    print(count_list)