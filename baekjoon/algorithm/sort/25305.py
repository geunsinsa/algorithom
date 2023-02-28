N , k = map(int, input().split())
score = list(map(int, input().split()))
score.sort(reverse=True)
print(score[k-1])

'''sort()는 이자체가 변수 원형을 정렬을 하고
    sorted()는 변수 원형은 그대로 있고 다른 변수로 새로운 변수 = sorted(원형 변수) 지정 해줘야한다 '''