
'''rest = [True] * 10
count = []
for i in range(10):
    num = int(input())
    rest[i] = num % 42


for i in rest:
    for j in rest:
        if i == j:
            count.append(i)

print(len(set(count)))'''

arr = []

for i in range(10):
    n = int(input())
    arr.append(n%42)
arr = set(arr)
print(len(arr))


