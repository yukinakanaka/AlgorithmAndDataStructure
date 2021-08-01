Graph = list[list[int]]

if __name__ == '__main__':
    G: Graph = list()
    G.append([5])
    G.append([3, 6])
    G.append([5, 7])
    G.append([0, 7])
    G.append([1, 2, 6])
    G.append([])
    G.append([7])
    G.append([0])

    print(G)
