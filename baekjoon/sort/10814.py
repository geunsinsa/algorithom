import sys
N = int(sys.stdin.readline())
dictionary = []

for _ in range(N):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    dictionary.append((age, name))

dictionary.sort(key=lambda x: x[0])
for i in dictionary:
    print(i[0], i[1])

'''
import sys
N = int(sys.stdin.readline())
dictionary = []

for _ in range(N):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    dictionary.append((age, name))

dictionary.sort(key=lambda x: x[0])
for i in dictionary:
    print(i[0], i[1])

'''