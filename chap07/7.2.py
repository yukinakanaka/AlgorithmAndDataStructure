import array


class Pair:
    start: int
    end: int

    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return f"{self.start:2d} - {self.end:2d}"

    def __repr__(self) -> str:
        return f"{self.start:2d} - {self.end:2d}"


def sort_pairs(pairs: list[Pair]) -> list[Pair]:
    results: list[Pair] = [pairs[0]]

    for pair in pairs[1:]:
        for i, p in enumerate(results):
            if p.end > pair.end:
                results.insert(i, pair)
                break
        else:
            results.append(pair)
            print(f"{pair} {i} continue")
            continue
        print(f"{pair} {i} breaked")

    return results


if __name__ == '__main__':
    pairs: list[Pair] = [Pair(0, 5), Pair(2, 4), Pair(4, 7), Pair(9, 10), Pair(5, 6), Pair(10, 15)]
    sorted_pairs = sort_pairs(pairs)

    for i in sorted_pairs:
        print(i)

    result: list[Pair] = [sorted_pairs[0]]
    for pair in pairs[1:]:
        if result[-1].end <= pair.start:
            result.append(pair)

    print("-------")
    for i in result:
        print(i)
