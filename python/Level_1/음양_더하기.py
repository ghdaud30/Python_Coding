absolutes = [1,2,3]	
signs = [False,False,True]	

def solution(absolutes, signs):
    answer = 0
    
    for i , v in zip(absolutes,signs):
        if(v == True):
            answer += i
        else:
            answer += (-i)
            
    
    return answer

print(solution(absolutes, signs))