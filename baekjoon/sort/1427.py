import sys
N = int(sys.stdin.readline())

arr = []
for i in str(N):
    arr.append(int(i))

arrange = sorted(arr, reverse=True)
for j in arrange:
    print(j, end='') #문자열 변수를 선언해서 바꾸지 않아도 리스트안에 있는 것들을 한번에 연결 시킬수 있다.
'''answer = ''
for i in arrange:
    answer += str(i)
print(int(answer))'''