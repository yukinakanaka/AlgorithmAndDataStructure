from typing import Final

MAX: Final[int] = 5


class Stack:
    top: int
    stack: list

    def __init__(self) -> None:
        self.top = 0
        self.stack = [99] * MAX

    def push(self, a: int) -> None:
        self.stack[self.top] = a
        self.top += 1

    def pop(self) -> int:
        result: int = self.stack[self.top - 1]
        self.top -= 1

        return result

    def __repr__(self) -> str:
        return f'top:{self.top: d}: {", ".join([str(x) for x in self.stack])}'


if __name__ == '__main__':
    s: Stack = Stack()

    s.push(10)
    s.push(20)
    s.push(30)

    print(s)

    print(f"{s.pop():d}")
    print(f"{s.pop():d}")

    print(s)
