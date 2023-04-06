# 실버 3

from collections import deque

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
queue = deque(range(1, n + 1))
result = 0

for number in numbers:
    index = queue.index(number)
    if index > len(queue) // 2:
        while queue[0] != number:
            queue.appendleft(queue.pop())
            result += 1
    else:
        while queue[0] != number:
            queue.append(queue.popleft())
            result += 1
    queue.popleft()

print(result)
