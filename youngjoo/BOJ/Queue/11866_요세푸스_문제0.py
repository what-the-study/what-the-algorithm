# 실버 5

n, k = map(int, input().split())
queue = list(range(1, n + 1))
index = k - 1
result = []

while queue:
    result.append(queue.pop(index))
    index += k - 1
    if queue and index >= len(queue):
        index %= len(queue)

print(f"<{', '.join(map(str, result))}>")
