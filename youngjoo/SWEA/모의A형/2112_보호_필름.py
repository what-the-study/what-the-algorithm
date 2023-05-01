# 모의 SW 역량테스트

from itertools import combinations


def is_same_all_cells(cell, start, end):
    for i in range(start, end - 1):
        if cell[i] != cell[i + 1]:
            return False

    return True


def pass_all_columns(film):
    for column in zip(*film):
        for start in range(d - k + 1):
            if is_same_all_cells(column, start, start + k):
                break
        else:
            return False

    return True


def test():
    film = [list(map(int, input().split())) for _ in range(d)]

    if pass_all_columns(film):
        return 0

    for i in range(1, d + 1):
        for combi in combinations(range(0, d), i):
            for case in range(2 ** i):
                outcomes = map(int, format(case, "b").zfill(i))
                memory = {}

                for index, status in zip(combi, outcomes):
                    memory[index] = film[index]
                    film[index] = [status] * w

                if pass_all_columns(film):
                    return i

                for index, original in memory.items():
                    film[index] = original


for t in range(1, int(input()) + 1):
    d, w, k = map(int, input().split())  # 두께, 가로, 합격기준
    print(f"#{t} {test()}")
