# 플래티넘 3

import sys

input = sys.stdin.readline
NOT_MATCHED = -1


class Shark:
    def __init__(self, size, speed, intelligence):
        self.__size = size
        self.__speed = speed
        self.__intelligence = intelligence

    def __ge__(self, other_shark):
        size, speed, intelligence = other_shark.get_info()
        return self.__size >= size and self.__speed >= speed and self.__intelligence >= intelligence

    def get_info(self):
        return self.__size, self.__speed, self.__intelligence


def dfs(predator):
    if visited[predator]:
        return False

    visited[predator] = True

    for prey in graph[predator]:
        if matching[prey] == NOT_MATCHED:
            matching[prey] = predator
            return True

    for prey in graph[predator]:
        if dfs(matching[prey]):
            matching[prey] = predator
            return True

    return False


n = int(input())
sharks = [Shark(*map(int, input().split())) for _ in range(n)]
graph = [[] for _ in range(n)]
matching = [NOT_MATCHED] * n
result = n

for i, shark1 in enumerate(sharks):
    for j, shark2 in enumerate(sharks):
        if (i != j) and (shark1 >= shark2) and (i not in graph[j]):
            graph[i].append(j)

for predator in range(n):
    visited = [False] * n
    result -= int(dfs(predator))

    visited = [False] * n
    result -= int(dfs(predator))

    if result == 0:
        break

print(result)
