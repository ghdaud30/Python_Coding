n = 16
a = 1
b = 13

def solution(n,a,b):
    answer = 1
    
    while(True):
        
        # 처음 시작할때 a와 b가 한조에있으면 1을 리턴
        for i in range(1,n+1,2): 
            if((a == i and b == i+1) or b == i and a == i+1):
                return 1    
        
        # a를 절반으로 나눔
        if(a % 2 == 0):
            a //= 2
            answer += 1
        else:
            a += 1
            a //= 2
            answer += 1
        
        # b를 절반으로 나눔
        if(b % 2 == 0):
            b //= 2
        else:
            b += 1
            b //= 2

        # 각 각 나눈 다음 a 와 b가 한조가 되면 리턴
        if(a + 1 == b or b + 1 == a):
            return answer

    


print(solution(n,a,b))