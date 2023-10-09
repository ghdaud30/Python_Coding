price = 3
money = 20
count = 4

def solution(price, money, count):
    answer = -1
    total = 0

    answer = max((sum([price * i for i in range(1,count+1)]) - money),0)

    # for i in range(1, count+1):
    #     total += price * i
    # answer = total - money

    # if(answer < 0):
    #     answer = 0

    return answer

print(solution(price, money, count))