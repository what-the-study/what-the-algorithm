# 완전탐색 (https://school.programmers.co.kr/learn/courses/30/lessons/86491)

def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]

    max_width, max_height = map(max, zip(*sizes))
    return max_width * max_height
