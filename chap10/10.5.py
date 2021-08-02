import math


class Heap:
    heap: list[int]

    def __init__(self) -> None:
        self.heap = list()

    def push(self, x: int) -> None:
        self.heap.append(x)
        k: int = len(self.heap) - 1

        while k > 0:
            p: int = math.floor(((k-1)/2))
            if self.heap[p] < x:
                self.heap[k] = self.heap[p]
                k = p
            else:
                break
        self.heap[k] = x
        self.print_heap()

    def top(self) -> int:
        return self.heap[0]

    def pop(self) -> None:
        x: int = self.heap.pop()

        k: int = 0
        left: int = 2 * k + 1
        right: int = 2 * k + 2
        while left < len(self.heap):
            child: int
            if right < len(self.heap) and self.heap[left] < self.heap[right]:
                child = right
            else:
                child = left

            if self.heap[child] < x:
                break

            self.heap[k] = self.heap[child]
            k = child
            left = 2 * k + 1
            right = 2 * k + 2
        self.heap[k] = x

    def print_heap(self) -> str:
        lf: int = 1
        for i, k in enumerate(self.heap):
            print(k, end='\t')
            if i + 1 == lf:
                print("")
                lf = lf * 2 + lf
        print("")
        print("-------------------------------")

if __name__ == '__main__':
    h: Heap = Heap()
    h.push(5)
    h.push(3)
    h.push(7)
    h.push(1)
    h.push(10)
    h.push(12)
    h.push(8)

    h.pop()
    h.print_heap()