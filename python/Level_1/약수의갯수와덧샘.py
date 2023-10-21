left = 24
right = 27

def solution(left, right):
    answer = 0
    
    for i in range(left, right + 1):
        num = 0
        
        for j in range(1, int(i ** 0.5) + 1):
            if(i % j == 0):
                num += 1
                if(j ** 2 != i):
                    num += 1
        if(num % 2 == 0):
            answer += i
        else:
            answer -= i
                
    return answer

print(solution(left,right))