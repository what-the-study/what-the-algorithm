# 모의 SW 역량테스트

# 2x2 영역에서 칩 생산이 가능한 지 확인하는 함수 (영역이 비었는지 확인)
def is_clean(x, y):
    if y >= w - 1:  # 열의 마지막 인덱스로 시작하는 영역은 칩 생산 불가능
        return False

    if wafer[x][y] + wafer[x + 1][y] + wafer[x][y + 1] + wafer[x + 1][y + 1] > 0:
        return False

    if visited[x][y] + visited[x + 1][y] + visited[x][y + 1] + visited[x + 1][y + 1] > 0:
        return False

    return True


# 2x2 영역에서 칩 생산을 하도록 칠하는 함수 (시작점은 2로 칠함)
def set_chip(x, y):
    visited[x][y] = 2
    visited[x + 1][y] = visited[x][y + 1] = visited[x + 1][y + 1] = 1


# 칩 생산을 했던 2x2 영역을 깨끗하게 만드는 함수
def clear_chip(x, y):
    visited[x][y] = visited[x + 1][y] = visited[x][y + 1] = visited[x + 1][y + 1] = 0


# 최대 칩 생산 갯수를 계산하는 함수
def get_max_chips(stage):
    x, y = divmod(stage, w)  # 몫 -> 행 번호, 나머지 -> 열 번호

    # 더이상 칩 생산이 불가능한 칸에 도달한 경우 0개 반환
    if x == h - 2 and y == w - 1:
        return 0

    x_status = 0  # x행에서 칩 생산에 사용되는 영역 기록(bitmasking)

    # 마지막 열 번호에서
    if y == w - 1:
        # 0 ~ w-2 중에서 칩 생산의 시작점(== 2)가 있다면 비트에 표시
        for i in range(w - 1):
            if visited[x][i] == 2:
                x_status |= 1 << (w - i - 1)  # 왼쪽부터 표시해야 하므로 w - i - 1 만큼 shift

        if dp[x][x_status] > 0:
            return dp[x][x_status]  # 이미 dp 배열에 값이 있다면 해당 값을 반환

    # dp 배열이 아직 채워지지 않았다면 최대 개수 구하기 (처음 탐색하는 경우)
    max_chips = 0

    # 현재 영역에 칩 생산이 가능하다면 생산 하고, 최대 개수 갱신
    if is_clean(x, y):
        set_chip(x, y)  # 칩 생산 영역 표시
        max_chips = get_max_chips(stage + 1) + 1  # 다음 칸가서 최대 개수 구하고 + 1
        clear_chip(x, y)  # 칩 생산 영역 표시 지우기

    # 현재 영역에 칩 생산을 안했을 때의 개수와 비교하여 최대 개수 갱신
    max_chips = max(max_chips, get_max_chips(stage + 1))

    # 마지막 열 번호인 경우, 현재 행 상태에 대해 dp 배열에 상태를 등록할 수 있으므로, 최대 개수 등록
    if y == w - 1:
        dp[x][x_status] = max_chips

    return max_chips


for t in range(1, int(input()) + 1):
    w, h = map(int, input().split())  # h, w를 swap 해서 입력
    wafer = list(map(list, zip(*[list(map(int, input().split())) for _ in range(w)])))  # 원래 입력에서 가로, 세로를 바꿈
    visited = [[0] * w for _ in range(h)]  # 현재 칩 생산에 사용되는 영역을 표시하는 배열
    dp = [[0] * (1 << w) for _ in range(h)]  # dp[행][현재 행에서 칩 생산에 사용되는 영역 기록]

    # 각 격자에 번호를 순서대로 부여하여 탐색함 (ex. (0, 0)을 0번 ~ (2, 2)를 9번)
    print(f"#{t} {get_max_chips(0)}")
