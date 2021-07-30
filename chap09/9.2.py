from typing import Final

class Queue:
    MAX: Final[int] = 5
    head: int
    tail: int

    queue: list[int]

    def __init__(self) -> None:
        self.queue = [99] * self.MAX
        self.head = 0
        self.tail = 0

    def enqueue(self, a: int) -> None:
        self.queue[self.tail] = a
        if self.tail == self.MAX -1:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self) -> None:
        result: int = self.queue[self.head]
        if self.head == self.MAX -1:
            self.head = 0
        else:
            self.head += 1
        return result

    def __repr__(self) -> str:
        return f"head:{self.head:d}, tail:{self.tail:d}, [{', '.join([str(x) for x in self.queue])}]"


if __name__ == '__main__':
    queue: Queue = Queue()
    queue.enqueue(0)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)

    print(f"{queue.dequeue():d}")
    print(f"{queue.dequeue():d}")
    print(f"{queue.dequeue():d}")
    print(f"{queue.dequeue():d}")
    print(queue)

    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    print(queue)

    print(f"{queue.dequeue():d}")
    print(f"{queue.dequeue():d}")
    print(f"{queue.dequeue():d}")
    print(queue)
