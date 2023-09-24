# 플래티넘 3

import sys

input = sys.stdin.readline
MAX_SUM = 2000
NOT_MATCHED = -1


def set_ab(a_set, b_set):
    for number in numbers:
        if number % 2 == 0:
            a_set.append(number)
        else:
            b_set.append(number)


def bipartite_match():
    def dfs(start):
        if visited[start]:
            return False

        visited[start] = True

        for end in graph[start]:
            if matching[end] == NOT_MATCHED:
                matching[end] = start
                return True

        for end in graph[start]:
            if dfs(matching[end]):
                matching[end] = start
                return True

        return False

    # 에라토스테네스의 체를 이용한 소수 집합 구하기
    prime_numbers = list(range(MAX_SUM))
    for i in range(2, int(MAX_SUM ** 0.5) + 1):
        if prime_numbers[i] > 0:
            for j in range(i + i, MAX_SUM, i):
                prime_numbers[j] = 0

    # 그래프 만들기
    graph = [[] for _ in range(n)]

    for i, number1 in enumerate(a_set):
        for j, number2 in enumerate(b_set):
            if prime_numbers[number1 + number2] > 0:
                graph[i].append(j)

    # 이분 매칭
    result = []

    for end in graph[0]:
        matching = [NOT_MATCHED] * len(b_set)
        matching[end] = 0
        temp = 1

        for start in range(len(a_set)):
            visited = [False] * len(a_set)
            visited[0] = True
            temp += int(dfs(start))

        if temp == len(b_set):
            result.append(b_set[end])

    print(*sorted(result)) if result else print(-1)


n = int(input())
numbers = list(map(int, input().split()))
a_set, b_set = [], []

if numbers[0] % 2 == 0:
    set_ab(a_set, b_set)
else:
    set_ab(b_set, a_set)

if len(a_set) == len(b_set):
    bipartite_match()
else:
    print(-1)
