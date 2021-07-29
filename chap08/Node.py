from typing import Generic, Optional, TypeVar

T = TypeVar('T')

class Node(Generic[T]):
    value: str
    next: T

    def __init__(self, value: str, next: Optional[T] = None) -> None:
        self.value = value
        self.next = next