# 골드 4

n, s = map(int, input().split())
a = list(map(int, input().split()))

i, j = 0, 0
total = a[0]
min_length = n + 1

while i <= j:
    if total < s:
        j += 1
        if j >= n:
            break
        total += a[j]
    else:
        min_length = min(min_length, j - i + 1)
        total -= a[i]
        i += 1

print(0 if min_length == n + 1 else min_length)
