# 골드 2

n, k = int(input()), int(input())
start, end = 1, n * n
answer = 0

while start <= end:
    mid = (start + end) // 2
    counts = 0

    for i in range(1, n + 1):
        counts += min((mid - 1) // i, n)

    if counts <= k - 1:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
