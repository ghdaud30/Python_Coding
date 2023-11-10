a = 2
b = 1
n = 20

def solution(a, b, n):
    answer = 0
    get_coke = 0
    
    while(n >= a):
        get_coke = (n // a) * b
        n = (n % a) + get_coke
        answer += get_coke

    return answer

print(solution(a,b,n))