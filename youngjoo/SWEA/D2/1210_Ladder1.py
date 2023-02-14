# Two-dimentional lists

dy = [-1, 1]

for _ in range(1, 11):
    t = input()
    ladder = [input().split() for _ in range(100)]
    x = 99
    y = ladder[x].index("2")

    while x > 0:
        for i in range(2):
            ny = y + dy[i]
            if 0 <= ny < 100 and ladder[x][ny] == "1":
                ladder[x][y] = "0"
                y = ny
                break
        else:
            x -= 1

    print(f"#{t} {y}")
