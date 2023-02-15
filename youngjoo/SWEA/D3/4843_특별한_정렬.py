# Sorting

for t in range(1, int(input()) + 1):
    n = int(input())
    a = sorted(map(int, input().split()))
    result = []

    for i in range(n // 2):
        result.extend([a[n - i - 1], a[i]])

    if n % 2 == 1:
        result.append(a[n // 2])

    print(f"#{t}", *result[:10])
