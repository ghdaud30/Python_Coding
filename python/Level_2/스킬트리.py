skill = "CBD"	
skill_trees = ["BACDE", "CBADF", "AECB", "BDA",'ACB']

def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    record = []
    
    # 각 단어에서 skill에 포함된 
    # 글자가 있으면 리스트에 넣어줍니다 
    for tree in skill_trees:
        word = ''
        for i in tree:
            if(i in skill):
                word += i
        record.append(word)
    
    #리스트 각 단어에서 skill 글자 순서대로 
    # 시작하는지 확인해줍니다 순서대로 시작하지않으면
    # 다음 단어로 넘어갑니다
    for v in record:
        for j in range(len(skill)):
            try:
                if(v[j] == skill[j]):
                    continue
                else:
                    break
            except IndexError:
                answer += 1
                break
        else:
            answer += 1
        
    return answer

print(solution(skill, skill_trees))