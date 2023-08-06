# 쿼드 압축 후 개수 세기

def solution(arr):
    def recursion(x1, y1, x2, y2):
        if x2 - x1 == y2 - y1 == 1:
            result[arr[x1][y1]] += 1
            return arr[x1][y1]

        hx = (x1 + x2) // 2
        hy = (y1 + y2) // 2

        one = recursion(x1, y1, hx, hy)
        two = recursion(x1, hy, hx, y2)
        three = recursion(hx, y1, x2, hy)
        four = recursion(hx, hy, x2, y2)

        if one == two == three == four:
            result[one] -= 3
            return one

        return 2

    result = [0, 0, 0]
    recursion(0, 0, len(arr), len(arr))

    return result[:2]


print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
