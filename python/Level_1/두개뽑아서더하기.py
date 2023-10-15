from itertools import combinations

numbers = [2,1,3,4,1]	

def solution(numbers):
    comb = list(combinations(numbers,2))
    result = []

    for i in comb:
        a = i[0]
        b = i[1]
        sum = a + b
        result.append(sum)

    result = sorted(list(set(result)))

    print(result)

    return result

print(solution(numbers))