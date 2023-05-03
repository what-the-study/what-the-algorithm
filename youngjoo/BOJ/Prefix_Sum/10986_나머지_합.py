# 골드 3

from collections import Counter

n, m = map(int, input().split())
a = list(map(int, input().split()))
prefix = [a[0]]

for i in range(1, n):
    prefix.append(prefix[-1] + a[i])

counter = Counter(p % m for p in prefix)
result = counter[0]

for i in counter.values():
    result += (i * (i - 1)) // 2

print(result)
