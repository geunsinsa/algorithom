m = int(input())
n = int(input())

num_list = []
for i in range(m, n+1):
    cnt = 0
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            cnt += 1
            break
    if cnt == 0:
        num_list.append(i)
if len(num_list) > 0:
    print(sum(num_list))
    print(min(num_list))
else:
    print(-1)

'''start_num = int(input())
last_num = int(input())

sosu_list = []
for num in range(start_num, last_num + 1):
    error = 0
    if num > 1:
        for i in range(2, num):  # 2부터 num-1까지
            if num % i == 0:
                error += 1
                break  # 2부터 num-1까지 나눈 몫이 0이면 error가 증가하고 for문을 끝냄
        if error == 0:
            sosu_list.append(num)  # error가 없으면 소수리스트에 추가

if len(sosu_list) > 0:
    print(sum(sosu_list))
    print(min(sosu_list))
else:
    print(-1)'''
