# Two-dimensional lists

def counts(board):
    return sum(list(map(len, "".join(line).split("0"))).count(k) for line in board)


for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    puzzle = [input().split() for _ in range(n)]
    print(f"#{t} {counts(puzzle) + counts(list(zip(*puzzle)))}")
