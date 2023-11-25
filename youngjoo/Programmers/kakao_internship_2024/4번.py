# 4. 카드 게임

def solution(coin, cards):
    def recursion(rounds, hand_copy, i, coin):
        nonlocal max_rounds

        if rounds >= 1:
            flag = False

            for case in hand_copy:
                if case > n // 2 or (n + 1 - case) not in hand_copy:
                    continue

                flag = True

                card1, card2 = case, n + 1 - case
                temp = list(hand_copy)
                temp.remove(card1)
                temp.remove(card2)

                if i == n:
                    max_rounds = max(rounds + 1, max_rounds)
                    return

                card1, card2 = cards[i], cards[i + 1]
                recursion(rounds + 1, list(temp), i + 2, coin)
                if coin >= 1:
                    recursion(rounds + 1, temp + [card1], i + 2, coin - 1)
                    recursion(rounds + 1, temp + [card2], i + 2, coin - 1)
                if coin >= 2:
                    recursion(rounds + 1, temp + [card1, card2], i + 2, coin - 2)

            if not flag:
                max_rounds = max(rounds - 1, max_rounds)

            return

        card1, card2 = cards[i], cards[i + 1]
        recursion(rounds + 1, list(hand_copy), i + 2, coin)
        if coin >= 1:
            recursion(rounds + 1, hand_copy + [card1], i + 2, coin - 1)
            recursion(rounds + 1, hand_copy + [card2], i + 2, coin - 1)
        if coin >= 2:
            recursion(rounds + 1, hand_copy + [card1, card2], i + 2, coin - 2)

    n = len(cards)
    hand_count = n // 3
    hand = cards[:hand_count]
    max_rounds = 1

    recursion(0, hand, hand_count, coin)

    return max_rounds


print(solution(4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]))
