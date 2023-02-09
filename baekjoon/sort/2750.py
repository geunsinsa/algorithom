N = int(input())
arr = []

for _ in range(N):
    num = int(input())
    arr.append(num)

arr_reversed = sorted(arr)
for i in arr_reversed:
    print(i)