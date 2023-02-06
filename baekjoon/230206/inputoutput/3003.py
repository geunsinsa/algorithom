import sys

chess = [1, 1, 2, 2, 2, 8]
my_chess = list(map(int, sys.stdin.readline().split(" ")))


for i in range(len(chess)):
    print(chess[i]-my_chess[i], end=' ')