from array import array

if __name__ == '__main__':
    N: int = 5
    A: array = array('i', [4, 6, 8, 3, 4])
    B: array = array('i', [3, 4, 2, 3, 2])

    C: array = array('i')
    D: array = array('i')
    R: array = array('i')
    push_count: int = 0

    for (a, b) in zip(A, B):
        current_a = a + push_count
        r: int = current_a % b
        R.append(r)
        current_push: int = b - r if r != 0 else 0
        push_count = push_count + current_push
        C.append(a + push_count)
        D.append(current_push)

    print(f"{push_count: 3d}")
    
    print(f"A:{A}")
    print(f"R:{R}")
    print(f"P:{D}")
    print(f"L:{C}")
    print(f"B:{B}")