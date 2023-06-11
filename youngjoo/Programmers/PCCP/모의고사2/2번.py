from heapq import heappop, heappush, heapify


def solution(ability, number):
    heapify(ability)

    for _ in range(number):
        total = heappop(ability) + heappop(ability)
        heappush(ability, total)
        heappush(ability, total)

    return sum(ability)