n = 15

def solution(n):
    answer = 0
    sum = 0

    for i in range(1, n + 1):
        sum += i
        if( sum == n ):
            answer += 1
            break 
        for j in range(i + 1 ,n+1):
            sum += j

            if(sum == n):
                answer += 1
                sum = 0
                break
            elif (sum > n):
                sum = 0
                break

    return answer

print(solution(n))