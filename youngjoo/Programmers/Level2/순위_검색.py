from bisect import bisect_left
from collections import defaultdict
from itertools import combinations


def solution(info, query):
    groups = defaultdict(list)
    answer = []

    for result in info:
        *items, score = result.split()
        score = int(score)

        for i in range(5):
            for case in combinations(items, i):
                groups[" ".join(case)].append(score)

    for group in groups:
        groups[group].sort()  # 이진탐색을 위한 정렬

    for q in query:
        *items, score = q.split()
        items = [item for item in items if item != "-" and item != "and"]
        scores = groups[" ".join(items)]

        answer.append(len(scores) - bisect_left(scores, int(score)))

    return answer
