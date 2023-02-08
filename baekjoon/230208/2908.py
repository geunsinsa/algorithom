'''a, b = input().split()
a_reverse = ''
b_reverse = ''

for i in range(-1,-4,-1):
    a_reverse += a[i]
    b_reverse += b[i]

if int(a_reverse) > int(b_reverse):
    print(a_reverse)
else:
    print(b_reverse)'''

'''[참일 때 값 if 조건식 else 거짓일 때 값]
[::-1]'''


a, b = input().split()
a = int(a[::-1])
b = int(b[::-1])

print(a) if a > b else print(b)


