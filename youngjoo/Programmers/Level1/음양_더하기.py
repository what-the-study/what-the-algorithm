# 월간 코드 챌린지 시즌2 (https://school.programmers.co.kr/learn/courses/30/lessons/76501)

def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        answer += absolutes[i] if signs[i] else -absolutes[i]

    return answer
