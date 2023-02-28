import sys

def fibonacci(a):
    if a == 1:
        return 1
    if a == 0:
        return 0

    return fibonacci(a-1) + fibonacci(a-2)

n = int(sys.stdin.readline())
print(fibonacci(n))