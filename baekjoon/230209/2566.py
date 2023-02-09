arr = []

for i in range(9):
    row = list(map(int, input().split()))
    arr.append(row)

max_arr = []
for i in range(len(arr)):
    max_arr.append(max(arr[i]))
row = max_arr.index(max(max_arr))
column = arr[row].index(max(arr[row]))
print(max(max_arr))
print(row+1, column+1)

