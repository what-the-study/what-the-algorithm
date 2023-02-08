# List

for t in range(1, int(input()) + 1):
    n = int(input())
    carrots = list(map(int, input().split()))
    result = [1] * n

    for i in range(1, n):
        if carrots[i - 1] < carrots[i]:
            result[i] += result[i - 1]

    print(f"#{t} {max(result)}")
