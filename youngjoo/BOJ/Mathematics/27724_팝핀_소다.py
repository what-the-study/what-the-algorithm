# 실버 2

from math import log

n, m, k = map(int, input().split())
numbers = [k] + list(range(1, k)) + list(range(k + 1, n + 1))
winnings = 0

while len(numbers) > 1 and numbers[0] > numbers[1]:
    numbers = [max(numbers[i], numbers[i + 1]) for i in range(0, len(numbers) - 1, 2)]
    winnings += 1

remaining_battles = int(log(len(numbers), 2))
print(winnings + min(m, remaining_battles))
