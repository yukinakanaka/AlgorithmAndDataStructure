from typing import Generic, Optional, TypeVar

T = TypeVar('T')


class Node(Generic[T]):
    value: str
    next: T

    def __init__(self, value: str, next: Optional[T] = None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    nil: Node

    def __init__(self) -> None:
        self.nil = Node('nil')

    def insert(self, v: Node, p: Node = None):
        if p is None:
            p = self.nil

        # p→x
        # p→v→x
        v.next = p.next
        p.next = v

    def printList(self):
        cur: Node = self.nil.next
        while True:
            print(cur.value)
            cur = cur.next
            if cur is None:
                break

    def get_node(self, n: int) -> Node:
        # アクセス O(N)
        cur: Node = self.nil
        for _ in range(1, n + 1):
            cur = cur.next

        return cur


if __name__ == '__main__':
    one: Node = Node('one')
    two: Node = Node('two')
    three: Node = Node('three')

    ll: LinkedList = LinkedList()
    ll.insert(one)
    ll.insert(two, one)
    ll.insert(three, two)

    ll.printList()

    # アクセス O(N)
    print(f"3: {ll.get_node(3).value}")

    # 挿入 O(1)
    new_two = Node('new two')
    ll.insert(new_two, two)
    ll.printList()

    # 単方向リストでは削除はできない
