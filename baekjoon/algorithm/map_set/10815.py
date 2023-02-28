import sys

n = int(sys.stdin.readline())
having_card = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
guess_card = list(map(int, sys.stdin.readline().split()))

for i in guess_card:
    if i in having_card:
        print(1, end=' ')
    else:
        print(0, end=' ')




