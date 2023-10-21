import math

n = 5

def solution(n):
    answer = 0
    
    prime = [True] * (n + 1)
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if(prime[2]):
            j = 2
            while (i * j <= n):
                prime[i * j] = False
                j += 1
    
    for i in range(2,len(prime)):
        if(prime[i]):
            answer += 1
    
    return answer

print(solution(n))
