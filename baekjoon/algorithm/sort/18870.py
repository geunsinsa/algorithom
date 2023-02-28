'''import sys

N = int(sys.stdin.readline())
answer = [0] * N
arr = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    same = []
    for j in range(N):
        if arr[i] > arr[j]:

            same.append(arr[j])
        answer[i] = len(set(same))

for i in answer:
    print(i, end=' ')'''

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr2 = sorted(list(set(arr)))
dic1 = {arr2[i] : i for i in range(len(arr2))}
for i in arr:
    print(dic1[i], end=" ")


