from typing import Final
MAX: Final[int] = 10


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
        return f'[{", ".join([str(x) for x in self.stack])}] top:{self.top: d}'


class Pair:
    start: int
    end: int

    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        return f"{self.start:d}-{self.end:d}"


class Parser:
    stack: Stack

    def __init__(self) -> None:
        self.stack = Stack()

    def analyze(self, formula: str) -> dict:
        pairs: list[Pair] = list()

        for i, s in enumerate(formula):
            if s == "(":
                self.stack.push(i)
            else:
                pairs.append(Pair(self.stack.pop(), i))

        if self.stack.top == 0:
            return {
                "valid": True,
                "pairs": pairs
            }
        else:
            return {
                "valid": False,
                "pairs": None
            }


if __name__ == '__main__':
    formula: str = "(()(())())(()())"

    parser = Parser()
    print(parser.analyze(formula))
