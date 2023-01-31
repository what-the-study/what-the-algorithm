def solution(lottos, win_nums):
    # rank[i]는 i개 숫자를 맞췄을때의 순위
    rank = [6, 6, 5, 4, 3, 2, 1]
    # 당첨 번호에 중복이 없으니 시간 복잡도를 고려하여 set으로 변환
    win_nums = set(win_nums)
    zero_cnt = 0
    match = 0
    
    for l in lottos:
        if l == 0:
            zero_cnt += 1
        elif l in win_nums:
            match += 1
        
    answer = [rank[match+zero_cnt], rank[match]]
    return answer