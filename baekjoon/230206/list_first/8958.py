n = int(input())

for i in range(n):
    ox = input()
    li = list(ox)
    total = 0
    c = 1

    for j in li:
        if j == 'O':
            total += c
            c += 1
        else:
            c = 1
    print(total)





