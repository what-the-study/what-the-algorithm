# List

for t in range(1, int(input()) + 1):
    stations = [0] * 5001

    for _ in range(int(input())):
        s, e = map(int, input().split())
        for i in range(s, e + 1):
            stations[i] += 1

    print(f"#{t}", *[stations[int(input())] for _ in range(int(input()))])
