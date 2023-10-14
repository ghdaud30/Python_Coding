number = 100000
limit = 3
power = 2

import math

def solution(number, limit, power):
    answer = 0
    measure = []

    for i in range(1,number+1):
        count = 0
        for j in range(1,int(math.sqrt(i))+1):
            if(i % j == 0):
                count += 1
                if(pow(j,2) != i):  
                    count += 1

        measure.append(count)
    print(measure)
    
    for i in range(len(measure)):
        if(measure[i] > limit):
            measure[i] = power
        answer += measure[i]

    print(measure)
    return answer

print(solution(number, limit, power))
