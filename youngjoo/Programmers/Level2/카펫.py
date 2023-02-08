# 완전탐색 (https://school.programmers.co.kr/learn/courses/30/lessons/42842)

def solution(brown, yellow):
    divisors = [[i, yellow // i] for i in range(1, int(yellow ** 0.5) + 1) if yellow % i == 0]

    for h, w in divisors:
        if brown == h * 2 + w * 2 + 4:
            return [w + 2, h + 2]
