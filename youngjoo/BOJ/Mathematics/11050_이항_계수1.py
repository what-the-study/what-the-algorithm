# 브론즈 1

from itertools import combinations

n, k = map(int, input().split())
print(len(list(combinations(range(1, n + 1), k))))
