# List

for t in range(1, 11):
    n = int(input())
    box = sorted(map(int, input().split()))

    for _ in range(n):
        if box[-1] - box[0] <= 1:
            break
        box[-1] -= 1
        box[0] += 1
        box.sort()

    print(f"#{t} {box[-1] - box[0]}")
