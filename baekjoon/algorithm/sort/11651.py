import sys
arr = []
N = int(sys.stdin.readline())

for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))

arr.sort(key=lambda x: (x[1],x[0]))
for i in arr:
    print(i[0], i[1])
