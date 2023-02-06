

n = int(input())

for _ in range(n):
    cnt, word = input().split()
    for i in word:
        print(i*int(cnt), end='')


'''n = int(input())

for _ in range(n):
    cnt, word = input().split()
    text = ''
    for i in word:
        text += i*int(cnt)
    print(text)
    '''''




