# 組み合わせの全探索
# N個の数の部分集合の数は、2^Nある
# 2 ^ 20 = 1024 * 1024 = 1,048,576が10^9の限界

# pythonでの2進数の表現方法
# 1. fomatでbを使う, 2. bin(x)とする
# for i in range(8):
#      print('{:02d}, {:08b}, {:3d}'.format(i, 1<<i, 1<<i))
 
# 00, 00000001,   1
# 01, 00000010,   2
# 02, 00000100,   4
# 03, 00001000,   8
# 04, 00010000,  16
# 05, 00100000,  32
# 06, 01000000,  64
# 07, 10000000, 128

# 4つの組み合わせ
# 計算量: 2^N * N　
# fruits: list[str] = ['apple', 'orage', 'banana', 'cherry']
# for i in range(pow(2,len(fruits))):
#     contains: list[str] = list()
#     for j in range(len(fruits)):
#         if i & 1<<j > 0:                                              # AND演算
#             contains.append(fruits[j])
#     print('{:02d}, {:04b}, {:25s}'.format(i, i, ','.join(contains)))
# 
# 00, 0000,                          
# 01, 0001, apple                    
# 02, 0010, orage                    
# 03, 0011, apple,orage              
# 04, 0100, banana                   
# 05, 0101, apple,banana             
# 06, 0110, orage,banana             
# 07, 0111, apple,orage,banana       
# 08, 1000, cherry                   
# 09, 1001, apple,cherry             
# 10, 1010, orage,cherry             
# 11, 1011, apple,orage,cherry       
# 12, 1100, banana,cherry            
# 13, 1101, apple,banana,cherry      
# 14, 1110, orage,banana,cherry      
# 15, 1111, apple,orage,banana,cherry

from typing import Final

FIND_SUM: Final[int] = 10
NUMBER_LIST: tuple[int, ...] = (1, 2, 4, 5, 11)

INFINITY: Final[int] = 999999999999999

if __name__ == '__main__':
    print("START")

    exit: bool = False
    exit_set: list[int] = list()

    for i in range(pow(2,len(NUMBER_LIST))):
        current_set: list[int] = list()
        for j in range(len(NUMBER_LIST)):
            if i & 1<<j > 0: 
                current_set.append(NUMBER_LIST[j])

        if sum(current_set) == FIND_SUM:
            exit = True
            exit_set = current_set
            
    print("RESULT:")
    print("{}: {}".format(exit, exit_set))
    print("END")



