def solution(d, budget):
    d.sort()
    cost = 0
    answer = 0
    
    for c in d:
        cost += c
        if cost <= budget:
            answer += 1
        else:
            break
        
    return answer