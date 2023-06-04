def solution(queries):
    child = ["RR", "Rr", "Rr", "rr"]
    result = []

    for n, p in queries:
        if n == p == 1:
            result.append("Rr")
            continue

        temp_n, temp_p = n - 1, p - 1
        orders = [(temp_n, temp_p)]

        while temp_n > 1:
            temp_p //= 4
            temp_n -= 1
            orders.append((temp_n, temp_p))

        for i in range(len(orders) - 1, -1, -1):
            now_n, now_p = orders[i]
            now_p %= 4

            if child[now_p] in ["RR", "rr"]:
                result.append(child[now_p])
                break
        else:
            result.append(child[now_p])

    return result