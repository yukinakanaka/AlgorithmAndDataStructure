from chap08.BiLinkedList import Node, BiLinkedList
from typing import Final


class Stack:
    top: Node
    array: BiLinkedList

    def __init__(self) -> None:
        self.array = BiLinkedList()
        self.top = self.array.zero

    def push(self, a: str) -> None:
        node: Node = Node(a)
        self.array.insert(node, self.top)
        self.top = node

    def pop(self) -> str:
        result: Node = self.top
        self.array.delete(result)
        self.top = self.top.prev

        return result.value

    def __str__(self) -> str:
        return self.array.__str__()


class Queue:
    MAX: Final[int] = 5
    head: Node
    tail: Node

    queue: BiLinkedList

    def __init__(self) -> None:
        self.queue = BiLinkedList()
        self.head = self.queue.zero
        self.tail = self.queue.zero

    def enqueue(self, a: str) -> None:
        n: Node = Node(a)
        self.queue.insert(n, self.tail)
        self.tail = n
        if self.head == self.queue.zero:
            self.head = n

    def dequeue(self) -> None:
        if self.head == self.queue.zero:
            raise Exception("There is no node.")
        result: Node = self.tail
        self.tail = self.tail.prev
        self.queue.delete(result)

        return result

    def __repr__(self) -> str:
        return f"head:{self.head}, tail:{self.tail}, {self.queue}]"


if __name__ == '__main__':
    # s: Stack = Stack()

    # s.push("10")
    # s.push("20")
    # s.push("30")

    # print(s)

    # print(f"{s.pop()}")
    # print(f"{s.pop()}")

    # print(s)

    # print("################")

    queue: Queue = Queue()
    queue.enqueue("0")
    queue.enqueue("1")
    queue.enqueue("2")
    queue.enqueue("3")
    print(queue)

    print(f"{queue.dequeue()}")
    print(f"{queue.dequeue()}")
    print(f"{queue.dequeue()}")
    print(f"{queue.dequeue()}")
    print(queue)

    queue.enqueue("0")
    queue.enqueue("1")
    queue.enqueue("2")
    queue.enqueue("3")
    print(queue)
