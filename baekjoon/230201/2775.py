test_case = int(input())

for i in range(test_case):
    floor = int(input())
    room = int(input())

    people = [i for i in range(1, room+1)]
    for i in range(floor):
        for j in range(1, room):
            people[j] += people[j-1]

    print(people[-1])
