n = 45

def solution(n):
    answer = 0
    num = ''

    while(n > 0):
        n, mod = divmod(n,3)
        num += str(mod)
    
    num = num[::-1]

    num = num[::-1]

    answer = int(num,3)

    return answer

print(solution(n))