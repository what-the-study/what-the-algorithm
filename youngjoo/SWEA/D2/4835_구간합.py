# List

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a[:m])
    totals = [total]

    for i in range(n - m):
        total += a[i + m] - a[i]  # sliding window
        totals.append(total)

    totals.sort()

    print(f"#{t} {totals[-1] - totals[0]}")
