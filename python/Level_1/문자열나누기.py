s = "abracadabraab"	

def solution(s):
    answer = 0
    
    first = ''
    count1 = 0
    count2 = 0
    num = 0   
     
    for idx , v in enumerate(s):
        
        #처음 시작하는 글자
        if(idx == num):
            first = v
            count1 += 1
        elif(v == first):
            count1 += 1
        #두번째 시작하는 글자
        else:
            count2 += 1
            
        # 두 글자에 갯수가 같으면 1을 더하고 초기화
        if(count1 == count2):
            answer += 1
            num = idx + 1
            first = ''
            count1 = 0
            count2 = 0
    
    # 다 끝난후 짝이 맞지 않으면 1을 추가        
    if(count1 != count2):
        answer += 1
            
    return answer

print(solution(s))