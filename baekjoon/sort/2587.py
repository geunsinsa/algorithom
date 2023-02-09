N_arr = []
for _ in range(5):
    a = int(input())
    N_arr.append(a)


average = int(sum(N_arr) / 5)
sort = sorted(N_arr)
print(average)
print(sort[2])