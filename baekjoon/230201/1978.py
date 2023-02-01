import sys

test_num = int(sys.stdin.readline()) #숫자의 개수
num = list(map(int, sys.stdin.readline().split(' '))) #입력 받은 숫자
rescnt = 0
for i in num:
    cnt = 0
    if i == 1:
        continue
    for j in range(2, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 1:
        rescnt += 1

print(rescnt)







