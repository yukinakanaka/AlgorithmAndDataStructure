# 特殊メソッド https://docs.python.org/ja/3/reference/datamodel.html

import sys

if __name__ == '__main__':
    # 同じアドレスを指している=数字のオブジェクトは事前?に定義されている
    # 0は24bit, 1,2は28bit
    # idはアドレスを表している。1のアドレス+28=2のアドレスではなく、1のアドレス+32=2のアドレスとなっているのは、
    # 3byte=16bit < 28bit < 4byte=32bitと、byte単位で切り上げているため?
    print(f"{id(0)} {0} {sys.getsizeof(0)}")

    # 変数に数字が代入されるとそのオブジェクトのアドレスを参照する様になる
    a: int = 0
    print(f"{id(a)} {a} {sys.getsizeof(a)}")
    b: int = 0
    print(f"{id(b)} {b} {sys.getsizeof(b)}")

    # aの参照先が、1のオブジェクトに変わる
    # なお、0と1のアドレスの差は32
    a = 1
    print(f"{id(a)} {a} {sys.getsizeof(a)}")

    a = 2
    print(f"{id(a)} {a} {sys.getsizeof(a)}")
