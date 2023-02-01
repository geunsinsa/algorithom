sugar_weight = int(input())
max_num = sugar_weight // 3
min_num = sugar_weight // 5
num_case = []

for i in range(0, max_num+1):
    for j in range(0, min_num+1):
        if (3*i)+(5*j) == sugar_weight:
            num_case.append(i+j)
if len(num_case) != 0:
    print(min(num_case))
else:
    print(-1)

"""num = int(input())
count = 0

while num >= 0:
    if num % 5 == 0:
        count += int(num // 5)
        print(count)
        break

    num -= 3
    count += 1

else:
    print(-1)"""
