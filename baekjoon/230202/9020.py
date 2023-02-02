'''import sys
import math

def gold(a):
    so_list = []
    diff = []
    for i in range(2, a):
        if i == 1:
            continue
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            so_list.append(i)

    for i in so_list:
        for j in so_list:
            if i + j == a:
                diff.append(abs(i - j))
    small_num =  int((a - min(diff)) / 2)
    big_num = int(small_num + min(diff))
    print(f"{small_num} {big_num}")

test = int(sys.stdin.readline())
for i in range(test):
    num = int(input())
    gold(num)'''


is_prime = [False, False] + [True] * 100000
for i in range(2, 100000):
    if is_prime[i]:
        for j in range(2*i, 100000, i):
            is_prime[j] = False

for i in range(int(input())):
    num = int(input())
    a = num // 2

    while a > 0:
        if is_prime[a] and is_prime[num-a]:
            print(a, num-a)
            break
        else:
            a -= 1











