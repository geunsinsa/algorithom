total = int(input())
item = int(input())

for _ in range(item):
    price, num = map(int, input().split())
    total -= price * num

if total == 0:
    print("Yes")
else:
    print("No")