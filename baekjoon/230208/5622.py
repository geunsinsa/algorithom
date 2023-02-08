alpabet_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
time = 0
for i in word:
    for j in range(len(alpabet_list)):
        if i in alpabet_list[j]:
            time += (j+3)

print(time)


