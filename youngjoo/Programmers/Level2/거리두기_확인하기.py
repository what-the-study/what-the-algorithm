# 거리두기 확인하기

def check(place):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    place = list(map(list, place))

    for x in range(5):
        for y in range(5):
            if place[x][y] == "P":
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]

                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if place[nx][ny] in "PV":
                            return 0

                        if place[nx][ny] == "O":
                            place[nx][ny] = "V"

    return 1


def solution(places):
    return list(map(check, places))
