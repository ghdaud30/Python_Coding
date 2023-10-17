n = 15

def solution(n):
    number = 0
    binary = bin(n)[2:]

    for i in binary:
        if(i == '1'):
            number += 1

    next = n + 1
    
    while(True):
        next_num = 0
        for i in bin(next)[2:]:
            if(i == '1'):
                next_num += 1
        if(next > n and next_num == number):
            return next
        next += 1
    
    return next

print(solution(n))