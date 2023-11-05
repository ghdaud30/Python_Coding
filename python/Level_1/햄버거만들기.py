ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]	

def solution(ingredient):
    answer = 0
    food = []
    i = 0
    food.append(ingredient[i])
    
    # ingredient를 순회하면서 마지막 4개에 값을 확인함
    # 1231 이면 그 값을 제거하고 갯수를 더해줌
    while(len(ingredient) - 1 > i):
        i += 1
        food.append(ingredient[i])
        if(food[-4:] == [1,2,3,1]):
            del food[-4:]
            answer += 1
    
    return answer

print(solution(ingredient))