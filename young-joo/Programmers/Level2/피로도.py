# 완전탐색 (https://school.programmers.co.kr/learn/courses/30/lessons/87946)

# 1. itertools 모듈 이용한 순열 풀이
from itertools import permutations


def solution(k, dungeons):
    max_dungeons = 0

    for case in permutations(dungeons, len(dungeons)):
        hp = k
        possible = 0

        for min_hp, delete_hp in case:
            if hp >= min_hp:
                hp -= delete_hp
                possible += 1
                if hp <= 0:
                    break

        max_dungeons = max(max_dungeons, possible)

    return max_dungeons

# 2. swap을 이용한 재귀 순열 풀이
# def solution(k, dungeons):
#     def explore(hp):
#         nonlocal max_dungeons
#         possible = 0
#
#         for min_hp, delete_hp in dungeons:
#             if hp >= min_hp:
#                 hp -= delete_hp
#                 possible += 1
#                 if hp <= 0:
#                     break
#
#         max_dungeons = max(max_dungeons, possible)
#
#     def permutations(depth):
#         if depth == len(dungeons):
#             explore(k)
#             return
#
#         for i in range(depth, len(dungeons)):
#             dungeons[depth], dungeons[i] = dungeons[i], dungeons[depth]
#             permutations(depth + 1)
#             dungeons[depth], dungeons[i] = dungeons[i], dungeons[depth]
#
#     max_dungeons = 0
#     permutations(0)
#     return max_dungeons
