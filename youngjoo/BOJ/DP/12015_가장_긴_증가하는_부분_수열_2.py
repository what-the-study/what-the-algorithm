# 골드 2

from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
numbers = [a[0]]

for i in range(1, n):
    if numbers[-1] < a[i]:
        numbers.append(a[i])
    else:
        index = bisect_left(numbers, a[i])
        numbers[index] = a[i]

print(len(numbers))
