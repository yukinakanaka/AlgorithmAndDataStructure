from chap08.BiLinkedList import Node, BiLinkedList


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


if __name__ == '__main__':
    s: Stack = Stack()

    s.push("10")
    s.push("20")
    s.push("30")

    print(s)

    print(f"{s.pop()}")
    print(f"{s.pop()}")

    print(s)
