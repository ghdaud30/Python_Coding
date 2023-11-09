x = 10
y = 60
n = 7

def solution(x, y, n):
    answer = 0
    
    if(x + n == y):
        return 1
    elif(x * 2 == y):
        return 1
    elif(x * 3 == y):
        return 1
    elif(x == y):
        return 0
    
    while(x < y):
        if(x + n > x * 2 or x + n > x * 3):
            y -= n
            answer += 1
        else:
            if(y % 2 == 0):
                y //=2
                answer += 1
            else:
                y //=3
                answer += 1
                
    if(x != y):
        return -1
    
    return answer

print(solution(x, y, n))
