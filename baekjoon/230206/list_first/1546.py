n = int(input())
point = list(map(int, input().split(' ')))
max_point = max(point)

for i in range(len(point)):
    point[i] = point[i] / max_point * 100

total = sum(point)/n
print(total)
