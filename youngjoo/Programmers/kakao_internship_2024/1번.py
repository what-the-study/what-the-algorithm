# 1. 선물 예측

from collections import defaultdict


def solution(friends, gifts):
    friends_count = len(friends)
    name_to_index = {friend: i for i, friend in enumerate(friends)}
    gift_table = [[0] * friends_count for _ in range(friends_count)]

    for gift in gifts:
        from_name, to_name = gift.split()
        from_index, to_index = name_to_index[from_name], name_to_index[to_name]
        gift_table[from_index][to_index] += 1

    gift_table_zip = list(zip(*gift_table))
    gift_point = {i: sum(gift_table[i]) - sum(gift_table_zip[i]) for i in range(friends_count)}

    next_month_gifts = defaultdict(int)

    for i in range(friends_count):
        for j in range(i + 1, friends_count):
            i_give_count, j_give_count = gift_table[i][j], gift_table[j][i]

            if i_give_count == j_give_count:
                if gift_point[i] > gift_point[j]:
                    next_month_gifts[i] += 1
                elif gift_point[i] < gift_point[j]:
                    next_month_gifts[j] += 1
            elif i_give_count > j_give_count:
                next_month_gifts[i] += 1
            else:
                next_month_gifts[j] += 1

    return max(next_month_gifts.values()) if next_month_gifts else 0


result = solution(["muzi", "ryan", "frodo", "neo"],
                  ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan",
                   "neo muzi"])
print(result)
