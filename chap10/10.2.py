class UndirectedGraph:
    v: list[set[int]]
    v_num: int

    def __init__(self, v_num: int) -> None:
        self.v = [set() for _ in range(v_num)]

    def __repr__(self) -> str:

        return [x.__repr__() for x in self.v].__repr__()

    def add(self, vi: int, vj: int) -> None:
        self.v[vi].add(vj)
        self.v[vj].add(vi)


class DirectedGraph:
    v: list[set[int]]
    v_num: int

    def __init__(self, v_num: int) -> None:
        self.v = [set() for _ in range(v_num)]

    def __repr__(self) -> str:

        return [x.__repr__() for x in self.v].__repr__()

    def add(self, vi: int, vj: int) -> None:
        self.v[vi].add(vj)


if __name__ == '__main__':
    G: UndirectedGraph = UndirectedGraph(8)
    G.add(0, 5)
    G.add(1, 3)
    G.add(1, 6)
    G.add(2, 5)
    G.add(2, 7)
    G.add(3, 0)
    G.add(3, 7)
    G.add(4, 1)
    G.add(4, 2)
    G.add(4, 6)
    G.add(6, 7)
    G.add(7, 0)

    print(G)

    G: DirectedGraph = DirectedGraph(8)
    G.add(0, 5)
    G.add(1, 3)
    G.add(1, 6)
    G.add(2, 5)
    G.add(2, 7)
    G.add(3, 0)
    G.add(3, 7)
    G.add(4, 1)
    G.add(4, 2)
    G.add(4, 6)
    G.add(6, 7)
    G.add(7, 0)

    print(G)
