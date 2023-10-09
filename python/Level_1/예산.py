d = [1,3,2,5,4]
budget = 9

def solution(d, budget):
    answer = 0
    d = sorted(d)
    print(d)

    for dep in d:
        if(dep <= budget):
            budget -= dep
            answer += 1
    
    return answer

print(solution(d,budget))