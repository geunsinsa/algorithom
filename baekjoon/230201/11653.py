import sys

num = int(sys.stdin.readline())
i = 2
while num != 1:
    if num % i == 0:
        print(i)
        num /= i
    else:
        i += 1
