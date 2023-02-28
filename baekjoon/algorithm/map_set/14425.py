import sys

m, n = map(int, sys.stdin.readline().split())
cnt = 0

S = set()
for _ in range(m):
    S.add(sys.stdin.readline())
for _ in range(n):
    word = sys.stdin.readline()
    if word in S:
        cnt += 1
print(cnt)


