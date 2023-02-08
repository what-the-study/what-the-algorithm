# List

for t in range(1, 2):
    n = int(input())
    buildings = list(map(int, input().split()))
    result = 0
    i = 2

    while i < n - 2:
        l1, l2, m, r1, r2 = buildings[i - 2:i + 3]
        max_height = max(l1, l2, r1, r2)
        if m > max_height:
            result += m - max_height
            i += 3
            continue
        i += 1

    print(f"#{t} {result}")
