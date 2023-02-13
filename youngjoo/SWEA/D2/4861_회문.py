# String

def find_palindrome(board):
    for line in board:
        for i in range(n - m + 1):
            word = line[i: i + m]
            if word == word[::-1]:
                return word
    return ''


for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]
    palindrome = find_palindrome(board)
    if palindrome:
        print(f'#{t} {palindrome}')
        continue
    rotated_board = [''.join(line) for line in zip(*board)]
    palindrome = find_palindrome(rotated_board)
    if palindrome:
        print(f'#{t} {palindrome}')

