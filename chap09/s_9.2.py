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

if __name__ == '__main__':
    formula: list = [3, 4, "+", 1, 2, "-", "*"]
    stack: Stack = Stack()
    for e in formula:
        if e == '+':
            right = stack.pop()
            left = stack.pop()
            stack.push(left + right)
        elif e == '-':
            right = stack.pop()
            left = stack.pop()
            stack.push(left - right)
        elif e == '*':
            right = stack.pop()
            left = stack.pop()
            stack.push(left * right)
        else:
            stack.push(e)
    
    print(f"ans: {stack.pop()}")
    

