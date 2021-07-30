from typing import Generic, TypeVar

T = TypeVar('T')


class Node(Generic[T]):
    value: str
    next: T
    prev: T

    def __init__(self, v: str) -> None:
        self.value = v
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return self.value


class BiLinkedList:
    zero: Node

    def __init__(self) -> None:
        self.zero = Node('nil')


    def insert(self, v: Node, p: Node=None) -> None:
        if p is None:
            p = self.zero

        # p → x
        # p → v → x
        if p.next is not None:
            p.next.prev = v
            v.next = p.next

        v.prev = p
        p.next = v

        print()

    def print_list(self):
        cur: Node = self.zero.next
        while True:
            print(cur.value)
            if cur.next is None:
                break
            cur = cur.next

    def delete(self, p: Node) -> None:
        # 削除はO(1)
        # x →　p → y
        # x → y
        if p.next is not None:
            p.next.prev = p.prev
        p.prev.next = p.next

    def __str__(self) -> str:
        cur: Node = self.zero.next
        if cur is None:
            return "[]"

        result: str = "[ "
        while True:
            result += f"{cur.value} "
            cur = cur.next
            if cur is None:
                break
        result += "]"
        return result

if __name__ == '__main__':
    one: Node = Node('one')
    two: Node = Node('two')
    three: Node = Node('three')

    bll: BiLinkedList = BiLinkedList()
    bll.insert(one)
    bll.insert(two, one)
    bll.insert(three, two)

    bll.print_list()

    bll.delete(two)
    bll.print_list()
