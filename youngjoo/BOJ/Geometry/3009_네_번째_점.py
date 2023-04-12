# 브론즈 3

points = list(zip(*[input().split() for _ in range(3)]))

for point in points:
    for i in point:
        if point.count(i) == 1:
            print(i, end=" ")
