import sys

n = int(sys.stdin.readline())
mass_arr = []

for _ in range(n):
    mass_arr.append(list(map(int, sys.stdin.readline().split())))

for i in mass_arr:
    rank = 1
    for j in mass_arr:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')





