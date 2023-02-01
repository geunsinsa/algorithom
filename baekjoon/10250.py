import sys
test_num = int(sys.stdin.readline())
cnt = 0

for i in range(test_num):
    h, w, n = map(int, sys.stdin.readline().split())
    room = (n // 6) + 1
    floor = n % 6
    if w > 9:
        print(f"{floor}{room}")
    else:
        print(f"{floor}{room}")
