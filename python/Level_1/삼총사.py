import itertools

number =[-2, 3, 0, 2, -5]
number2 = [-3, -2, -1, 0, 1, 2, 3]
number3 = [-1, 1, -1, 1]
result = 0

def examine_musketeers(number):
    answer = 0
    npr = list(itertools.combinations(number,3))

    # for i in npr:
    #     sum = 0
    #     for j in i:
    #         sum += j
    #     if(sum == 0):
    #         answer += 1
    return len([i for i in npr if sum(i) == 0])
    #return answer

print(examine_musketeers(number))

