# List

for t in range(1, int(input()) + 1):
    n, q = map(int, input().split())
    box = [0] * (n + 1)

    for i in range(1, q + 1):
        l, r = map(int, input().split())
        box[l:r + 1] = [i] * (r - l + 1)

    print(f"#{t}", *box[1:])
