from pprint import pprint


class Edge:
    to: int
    w: float

    def __init__(self, to: int, w: float) -> None:
        self.to = to
        self.w = w

    def __repr__(self) -> str:
        return f"({self.to}, {self.w})"


class DirectedGraph:
    v: list[list[Edge]]
    v_num: int

    def __init__(self, v_num: int) -> None:
        self.v = [list() for _ in range(v_num)]

    def __repr__(self) -> str:

        return [x.__repr__() for x in self.v].__repr__()

    def add(self, vi: int, vj: int, weight: float) -> None:
        self.v[vi].append(Edge(vj, weight))


if __name__ == '__main__':
    G: DirectedGraph = DirectedGraph(8)
    G.add(0, 5, 1.5)
    G.add(1, 3, 2.5)
    G.add(1, 6, 3.5)
    G.add(2, 5, 4.5)
    G.add(2, 7, 5.5)
    G.add(3, 0, 6.5)
    G.add(3, 7, 7.5)
    G.add(4, 1, 8.5)
    G.add(4, 2, 9.5)
    G.add(4, 6, 10.5)
    G.add(6, 7, 11.5)
    G.add(7, 0, 12.5)

    pprint(G)
