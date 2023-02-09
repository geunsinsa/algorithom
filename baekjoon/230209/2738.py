
row, column = map(int, input().split())
a, b = [], []

for i in range(column):
    i = list(map(int, input().split()))
    a.append(i)
for j in range(column):
    j = list(map(int, input().split()))
    b.append(j)

for i in range(row):
    for j in range(column):
        print(a[i][j]+b[i][j], end=' ')
    print()

