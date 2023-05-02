# 실버 3

n, k = map(int, input().split())
temps = list(map(int, input().split()))
prefix = [0]

for temp in temps:
    prefix.append(prefix[-1] + temp)

print(max(prefix[i] - prefix[i - k] for i in range(k, n + 1)))
