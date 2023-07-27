# 교점에 별 만들기

def get_intersection_points(line):
    points = []

    for i in range(len(line) - 1):
        a, b, e = line[i]

        for j in range(i + 1, len(line)):
            c, d, f = line[j]
            standard = a * d - b * c

            if standard == 0:
                continue

            x = ((b * f) - (e * d)) / standard
            y = ((e * c) - (a * f)) / standard

            if int(x) == x and int(y) == y:
                points.append((int(x), int(y)))

    return points


def solution(line):
    points = get_intersection_points(line)

    x_list, y_list = map(sorted, zip(*points))
    x_max, x_min = x_list[-1], x_list[0]
    y_max, y_min = y_list[-1], y_list[0]

    board = [["."] * (x_max - x_min + 1) for _ in range(y_max - y_min + 1)]

    for x, y in points:
        board[abs(y_max - y)][abs(x_min - x)] = "*"

    return ["".join(line) for line in board]
