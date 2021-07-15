import traceback
def sum_func(num: int) -> int:
    print("Call {:d}".format(num))
    
    if num == 0:
        traceback.print_stack(limit=10)
        return 0

    result: int = num + sum_func(num - 1)

    print("{:d}までの和: {:d}".format(num, result))
    
    return result


if __name__ == '__main__':
    sum_func(5)
