keymap = ["ABACD", "BCEFD"]
targets = ["ABCD","AABB"]	

def solution(keymap, targets):
    answer = []
    for i in targets: #ABCD
        count = 0
        for j in i:  # A B C D
            com = []
            for key in range(len(keymap)): # ABCAD BCEFD
                if j in keymap[key]:
                    com.append(keymap[key].index(j) + 1)
            if(len(com) == 0):
                answer.append(-1)
                break
            else:
                count += min(com)
        if(len(com) != 0):
            answer.append(count)

    return answer

print(solution(keymap, targets))