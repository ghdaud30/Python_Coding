import math
n = 437674
k = 3

def solution(n, k):
    answer = 0
    new_n = ''

    #n을 k진수로 변환하는 과정 
    while(n >= 1):
        n , mod = divmod(n,k)
        new_n += str(mod)    
    new_n = new_n[::-1]
    #그후 0을 기준으로 리스트로 분리함 이때 00같은 겹치는 경우 
    # 빈문자열이 들어오므로 조건문을 통해 처리 해줌
    new_n = [i for i in new_n.split('0') if i]
    
    # 소수 처리
    for i in new_n:
        is_prime = True
        if(int(i) == 1):
            continue
        
        for j in range(2, int(math.sqrt(int(i))) + 1):
            if(int(i) % j == 0):
                is_prime = False
                break
            
        if(is_prime):
            answer += 1
            
    print(new_n)
    return answer

print(solution(n,k))