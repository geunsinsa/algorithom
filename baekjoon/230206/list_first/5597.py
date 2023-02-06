'''
a = [1] * 30
empty = []

for _ in range(28):
    b = int(input()) - 1
    a[b] = 0

for i in range(len(a)):
    if a[i] == 1:
        empty.append(i+1)

print(empty[0])
print(empty[1])'''

student = [i for i in range(1,31)]

for _ in range(28):
    num = int(input())
    student.remove(num)

print(min(student))
print(max(student))