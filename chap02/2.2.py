if __name__ == '__main__':
    print("INPUT Number:")
    N: int = int(input())
    count: int = 0
    for i in range(N):
        for j in range(N):
            count += 1
    
    print("Relust:")
    print(count)
