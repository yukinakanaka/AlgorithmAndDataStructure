# ヒープは検索には適していない
from typing import Optional
import math

from typing import Optional


class Heap:
    heap: list[int]

    def __init__(self) -> None:
        self.heap = list()

    def push(self, x: int) -> None:
        self.heap.append(x)
        k: int = len(self.heap) - 1

        while k > 0:
            p: int = math.floor(((k - 1) / 2))
            if self.heap[p] < x:
                self.heap[k] = self.heap[p]
                k = p
            else:
                break
        self.heap[k] = x
        self.print_heap()

    def top(self) -> int:
        return self.heap[0]

    def pop(self) -> Optional[int]:
        if len(self.heap) == 0:
            return None

        top: int = self.heap[0]
        x: int = self.heap.pop()

        if len(self.heap) == 0:
            return x

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
        return top

    def print_heap(self) -> str:
        lf: int = 1
        for i, k in enumerate(self.heap):
            print(k, end='\t')
            if i + 1 == lf:
                print("")
                lf = lf * 2 + lf
        print("")
        print("-------------------------------")


def heap_sort(a: list[int]) -> list[int]:
    heap: Heap = Heap()
    for e in a:
        heap.push(e)

    result: list[int] = [-1] * len(a)
    for i in range(len(a)):
        result[len(a) - i - 1] = heap.pop()

    return result


if __name__ == '__main__':
    # h: Heap = Heap()
    # h.push(5)
    # h.push(3)
    # h.push(7)
    # h.push(1)
    # h.push(10)
    # h.push(12)
    # h.push(8)

    # h.pop()
    # h.print_heap()

    a: list[int] = [4, 6, 7, 3, 9, 2, 0]

    print(heap_sort(a))
