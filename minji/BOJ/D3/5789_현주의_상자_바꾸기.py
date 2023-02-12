"""
T = Test Case 갯수
N = 총 박스 갯수
Q = 총 작업 횟수
L, R = 변경하는 박스 시작번호, 끝번호
"""

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    boxes = [0] * N
    for i in range(1, Q+1): # 작업번호
        L, R = map(int, input().split())
        for j in range(L-1, R): #변경될 박스 번호 range
            boxes[j] = i

    print(f'#{tc} {" ".join(map(str,boxes))}')