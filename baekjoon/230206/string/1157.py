word = input().upper()
remove = list(set(word))
cnt = []

for x in remove:
    cnt.append(word.count(x))

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(remove[cnt.index(max(cnt))])


#list and dict difference
















