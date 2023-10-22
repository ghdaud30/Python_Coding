import sys

n = 10000
sys.setrecursionlimit(1000000)

def solution(n):
    answer = 0
    
    d = [0] * (n + 1)
    
    def pibo(n):
        print(n , end=' ')
        
        if(n == 1 or n == 2):
            return 1
        
        if(d[n] != 0):
            return d[n]
        
        d[n] = pibo(n-1) + pibo(n-2)
        
        return d[n]
            
           
    answer = pibo(n)
    answer %= 1234567
    
    return answer

print(solution(n))