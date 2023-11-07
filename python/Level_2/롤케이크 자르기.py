from collections import Counter

topping = [1,2,3,4,5]

def solution(topping):
    answer = 0
    #처음에 철수가 토핑을 다 가진다고 가정하고
    # 동생이 하나씩 철수의 토핑을 가져갑니다
    chul = Counter(topping)
    bro = set()
    
    #토핑을 하나씩 철수의 딕셔너리에서 감소시켜주고
    # 동생 set에 더합니다
    for i in topping:
        if(chul[i] > 0):
            chul[i] -= 1
            bro.add(i)
        if(chul[i] == 0):
            del chul[i]
        #동생 토핑과 철수 토핑이 종류 갯수가 같은지 확인해줍니다
        if(len(bro) == len(chul.keys())):
            answer += 1

    return answer

print(solution(topping))