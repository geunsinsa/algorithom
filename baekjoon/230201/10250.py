import sys
test_num = int(sys.stdin.readline())

for i in range(test_num):
    h, w, n = map(int, sys.stdin.readline().split())
    room = (n // h) + 1
    floor = n % h
    if n % h == 0:
        room = n // h
        floor = h
    print(f"{floor*100 + room}")

