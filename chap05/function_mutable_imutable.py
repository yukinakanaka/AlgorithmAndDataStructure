from typing import Any


def chmin(a: Any, b: Any) -> None:
    # この時点でaは渡されたものと同じオブジェクトを参照している
    print(f"START\ta: {id(a)}, b: {id(b)}")
    if a > b:
        # イミュータブルな変数は、違うオブジェクトを参照する様になる=aの参照先は書き換えられない
        a = b
        print(f"FINISH\ta: {id(a)}, b: {id(b)}")


def chmin_l(A: Any, B: Any) -> None:
    # この時点でaは渡されたものと同じオブジェクトを参照している
    print(f"START\tA: {id(A)}, B: {id(B)}")
    print(f"{id(A[0])}")
    if A[0] > B[0]:
        # listの要素の参照先はは書き換えられる。ただ、list自体の参照先は書き換えられない。
        A[0] = B[0]
        print(f"{id(A[0])}")
        print(f"FINISH\tA: {id(A)}, B: {id(B)}")
        A = [999]


if __name__ == '__main__':
    a: int = 10
    b: int = 5
    print(f"BEFORE\ta: {id(a)}, b: {id(b)}")
    # intはイミュータブル。関数の中でintの中身が内容が書き換えられても、外側には反映されない。
    chmin(a, b)
    print(f"AFTER\ta: {id(a)}, b: {id(b)}")

    A: list[int] = [10]
    B: list[int] = [5]
    print(f"BEFORE\tA: {A} {id(A)}, B: {B} {id(B)} ")
    # listはミュータブル。関数の中でlistの中身が書き換えられたら、外側にも反映される。
    chmin_l(A, B)
    print(f"AFTER\tA: {A} {id(A)}, B: {B} {id(B)}")
