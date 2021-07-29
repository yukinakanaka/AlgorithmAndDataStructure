
class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


if __name__ == '__main__':
    red_points = list[
        Point(1, 10),
        Point(4, 2),
        Point(8, 3),
        Point(10, 8),
        Point(2, 6),
        Point(9, 4)
    ]

    blue_points = list[
        Point(3, 8),
        Point(8, 1),
        Point(2, 2),
        Point(11, 7),
        Point(6, 2),
        Point(5, 6)
    ]

    pass
