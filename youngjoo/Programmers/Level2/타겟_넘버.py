# 깊이/너비 우선 탐색 (https://school.programmers.co.kr/learn/courses/30/lessons/43165)

def solution(numbers, target):
    def dfs(depth, total):
        if depth == len(numbers):
            if total == target:
                nonlocal answer
                answer += 1
            return

        dfs(depth + 1, total + numbers[depth])
        dfs(depth + 1, total - numbers[depth])

    answer = 0
    dfs(0, 0)

    return answer
