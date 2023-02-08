# List

for t in range(1, int(input()) + 1):
    _ = input()
    a = list(map(int, input().split()))
    print(f"#{t} {max(a) - min(a)}")
