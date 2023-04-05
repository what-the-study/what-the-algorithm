# 실버 3

from collections import Counter

n = int(input())
numbers = sorted(int(input()) for _ in range(n))
commons = Counter(numbers).most_common()
sorted_commons = sorted(commons, key=lambda x: (x[1], -x[0]), reverse=True)
counts = 0

for number, fre in sorted_commons:
    if fre == commons[0][1]:
        most_common = number
        counts += 1
    if counts == 2:
        break

print(round(sum(numbers) / n))
print(numbers[n // 2])
print(most_common)
print(numbers[-1] - numbers[0])
