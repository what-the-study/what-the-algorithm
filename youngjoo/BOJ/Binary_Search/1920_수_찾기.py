# 실버 4

import sys

input = sys.stdin.readline


def binary_search(x):
    start, end = 0, n - 1

    while start <= end:
        mid = (start + end) // 2

        if a[mid] == x:
            return 1

        if a[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

    return 0


n = int(input())
a = sorted(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
    print(binary_search(number))
