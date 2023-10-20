n = 2
m = 5

def solution(n, m):
    answer = []
    
    # 최대공약수
    for i in range(min(n , m), 0 , -1):
        if (n % i == 0 and m % i == 0):
            answer.append(i)
            break
    
    # # 최소공배수    
    # for j in range(max(n,m), (n * m) + 1, 1):
    #     if (j % n == 0 and j % m == 0):
    #         answer.append(j)
    #         break
    
     #최소공배수 공식( n*m / n와m의 최대공약수)
    lcm = (n*m) // answer[-1] # = int(n*m / gcd)      
    answer.append(lcm)
    return answer

print(solution(n, m))