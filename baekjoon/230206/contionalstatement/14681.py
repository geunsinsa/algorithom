x_point = int(input())
y_point = int(input())

if (x_point*y_point) > 0:
    if x_point > 0:
        print(1)
    else:
        print(3)
else:
    if x_point > 0:
        print(4)
    else:
        print(2)