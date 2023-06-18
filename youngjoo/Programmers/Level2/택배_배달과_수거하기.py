def solution(cap, n, deliveries, pickups):
    total_dist = 0
    d_amount, p_amount = 0, 0

    for i in range(n - 1, -1, -1):
        d_amount += deliveries[i]
        p_amount += pickups[i]

        while d_amount > 0 or p_amount > 0:
            d_amount -= cap
            p_amount -= cap
            total_dist += (i + 1) * 2

    return total_dist
