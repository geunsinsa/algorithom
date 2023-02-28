import sys
from collections import Counter
arr = {}
N = int(sys.stdin.readline())

for _ in range(N):
    word = sys.stdin.readline().strip()
    arr[word] = len(word)
sort_arr = sorted(arr.items(), key=lambda x: (x[1], x[0]))

for i in range(len(sort_arr)):
    print(sort_arr[i][0])



