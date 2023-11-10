cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]

def solution(cards1, cards2, goal):
    
    for i in goal:
        # 단어가 카드뭉치1에 있거나 카드뭉치2에 있으면
        # 그 요소를 삭제하고 없으면 No 를 반환
        if(cards1 and i in cards1[0]):
                cards1.remove(i)
        elif(cards2 and i in cards2[0]):
                cards2.remove(i)
        else:
            return 'No'
    # for 문을 완전히 종료하면
    # Yes를 반환
    else:
        return 'Yes'
    
print(solution(cards1, cards2, goal))