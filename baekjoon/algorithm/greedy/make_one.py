import sys

n, k = map(int, sys.stdin.readline().split())
counter = 0

while n != 1:
    if n % k == 0:
        n /= k
        counter += 1
    else:
        n -= 1
        counter += 1
print(counter)

#시간복잡도 줄이기 위한 코드

n, k = map(int, sys.stdin.readline().split())
result = 0

while True:
    target = (n // k) * k
    result = (n - target)
    n = target

    if n < k:
        break
    result += 1
    n // k

result += (n-1)