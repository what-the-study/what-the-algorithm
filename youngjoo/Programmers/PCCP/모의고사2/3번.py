from collections import deque


def solution(menu, order, k):
    queue = deque([(0, menu[order[0]])])
    temp = k
    max_answer = 1

    for each_order in order[1:]:
        while queue and queue[0][1] <= temp:
            queue.popleft()

        start = queue[-1][1] if queue else temp
        queue.append((temp, start + menu[each_order]))

        max_answer = max(max_answer, len(queue))
        temp += k

    return max_answer