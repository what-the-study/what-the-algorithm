from itertools import permutations


def solution(ability):
    n = len(ability)
    ability = list(zip(*ability))
    max_total = 0

    for people in permutations(range(n), len(ability)):
        sport, total = 0, 0

        for person in people:
            total += ability[sport][person]
            sport += 1

        max_total = max(total, max_total)

    return max_total
