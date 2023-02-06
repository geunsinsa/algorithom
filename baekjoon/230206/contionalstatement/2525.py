H, M = map(int, input().split())
T = int(input())

if M + T >= 60:
    add_hour = (M + T) // 60
    add_min = (M+T) % 60
    if H + add_hour >= 24:
        print(H+add_hour-24, add_min)
    else:
        print(H+add_hour, add_min)
else:
    add_hour = 0
    add_min = M + T
    print(H, add_min)

