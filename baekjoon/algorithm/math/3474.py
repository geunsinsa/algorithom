import sys
def ten_stay(a):
    cnt = 5
    total = 0
    while cnt <= a:
        total += (a // cnt)
        cnt *= 5
    return total

n = int(sys.stdin.readline())

for _ in range(n):
    A = int(sys.stdin.readline())
    print(ten_stay(A))



