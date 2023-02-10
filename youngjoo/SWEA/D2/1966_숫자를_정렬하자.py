# List

for t in range(1, int(input()) + 1):
    _ = input()
    print(f"#{t}", *sorted(map(int, input().split())))