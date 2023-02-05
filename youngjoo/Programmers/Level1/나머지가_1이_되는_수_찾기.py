# 월간 코드 챌린지 시즌3 (https://school.programmers.co.kr/learn/courses/30/lessons/87389)

def solution(n):
    for i in range(2, n // 2):
        if n % i == 1:
            return i

    return n - 1


print(solution(12))
