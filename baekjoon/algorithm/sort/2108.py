import sys
from collections import Counter
N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    num = int(sys.stdin.readline())
    arr.append(num)

arr.sort()
average = round(sum(arr)/N) # 산술평균
center = arr[N//2]  # 중앙값
arr_range = arr[-1] - arr[0] # 범위

mode = Counter(arr).most_common()
mode_value = 0
#counter 함수는 각원소별 개수를 표현함
#most_common 빈도수가 높은 것부터 하는데 빈도수가 같다면 원소 순서대로 표현하기 때문에 sort, sorted로 정렬한후 사용하는걸 추천
if len(mode) == 1:
    mode_value = mode[0][0]
elif mode[0][1] == mode[1][1]:
    mode_value = mode[1][0]
else:
    mode_value = mode[0][0]

print(average)
print(center)
print(mode_value)
print(arr_range)


