# https://school.programmers.co.kr/learn/courses/15007/lessons/121682

def solution(n, board, position):
    # 상/하/좌/우/대각
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    row, col = len(board), len(board[0])  # board 행, 열 크기
    answer = []

    for x, y in position:
        neighbors = 0  # 주변 이웃 개수

        # 8방향 델타 탐색
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col and board[nx][ny] == 1:
                neighbors += 1

        # 1. 살아 있는 칸 주변 이웃이 2명 이하 혹은 5명 이상 이면 다음 세대에 죽는다.
        if board[x][y] == 1 and (neighbors <= 2 or neighbors >= 5):
            answer.append(0)
        # 2. 죽어 있는 칸 주변 이웃이 2명 이면 다음 세대에 살아 난다.
        elif board[x][y] == 0 and neighbors == 2:
            answer.append(1)
        # 3. 그 외의 경우는 상태가 유지 된다.
        else:
            answer.append(board[x][y])

    return answer
