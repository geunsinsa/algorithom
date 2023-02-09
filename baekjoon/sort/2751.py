import sys
N = int(input())
arr = []
for _ in range(N):
    num = int(sys.stdin.readline())
    arr.append(num)

arr.sort()
for i in arr:
    print(i)

#오래 걸린 이유가 수가 커지면 input()으로 사용하면 오래 걸린다 그 이유가 input()은 개행문자를 rstrip()과 같으 함수를 수행하고 return
#sys.stdin.readline()을 사용한느 것이 현명하다