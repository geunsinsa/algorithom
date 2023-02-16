import sys

n = int(sys.stdin.readline())
total = 0
for i in range(1,n+1):
    '''total = i
    str_i = str(i)
    for j in str_i:
        total += int(j)'''
    A = list(map(int, str(i)))
    total = i + sum(A)
    if total == n:
        print(i)
        break
    if i == n:
        print(0)


    
    
    
    

