n = 5
lost = [2,3,5,1]
reserve = [1]

def solution(n, lost, reserve):
    answer = 0
    num = []
    
    lost_set = set(lost)
    reserve_set = set(reserve)
    
    common = list(lost_set.intersection(reserve_set))
                
    for i in common:
        lost.remove(i)
        reserve.remove(i)
    
    for i in range(1, n + 1):
        if(i not in lost):
            answer += 1
        elif(i in lost and i in reserve):
            reserve.remove(i)
            answer += 1
        else:            
            if(i - 1 in reserve):
                reserve.remove(i-1)
                answer += 1
            elif(i + 1 in reserve):
                reserve.remove(i+1)
                answer += 1
        
    return answer

print(solution(n, lost, reserve))