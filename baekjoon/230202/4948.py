n = 123456 * 2
primes = [False, False] + [True] * (n-1)

for i in range(2, n+1):
    if primes[i]:
        for j in range(2*i, n+1, i):
            primes[j] = False

while True:
    test = int(input())
    cnt = 0
    if test == 0:
        break
    for i in range(test+1, 2*test+1):
        if primes[i] == True:
            cnt += 1
    print(cnt)




