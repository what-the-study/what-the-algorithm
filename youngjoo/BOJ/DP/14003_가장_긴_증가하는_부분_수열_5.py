# 플래티넘 5

from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
numbers = [a[0]]
counts = [1] * n

for i in range(1, n):
    if numbers[-1] < a[i]:
        numbers.append(a[i])
        counts[i] = len(numbers)
    else:
        index = bisect_left(numbers, a[i])
        numbers[index] = a[i]
        counts[i] = index + 1

max_count = max(counts)
i = n - 1
result = []

while max_count > 0:
    if counts[i] == max_count:
        result.append(a[i])
        max_count -= 1
    i -= 1

print(len(result))
print(*result[::-1])
