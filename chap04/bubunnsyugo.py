if __name__ == '__main__':
    a = ['a', 'b', 'c', 'd']
    for i in range(pow(2, len(a))):
        print("{:d}--------".format(i))
        for j in range(len(a)):
            if i & 1 << j:
                print(a[j])
