import sys

chess = [1, 1, 2, 2, 2, 8]
my_chess = list(map(int, sys.stdin.readline().split(" ")))
answer = []

for i in range(len(chess)):
    answer.append(chess[i]-my_chess[i])

print(answer)

