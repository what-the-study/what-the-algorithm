def solution(command):
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = 0, 0
    direction = 0

    for op in command:
        if op == "R":
            direction = (direction + 1) % 4
        elif op == "L":
            direction -= 1
            if direction < 0:
                direction = 3
        elif op == "G":
            x += dxy[direction][0]
            y += dxy[direction][1]
        else:
            x -= dxy[direction][0]
            y -= dxy[direction][1]

    return [x, y]