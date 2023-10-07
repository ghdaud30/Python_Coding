s = "banana"

def solution(s):
    answer = []
    char = []
    char_com = []

    for i in s:
        if(i not in char):
            char.append(i)
            answer.append(-1)
        else:
            char.append(i)
            
            # for j in range(len(char)):
            #     if(char[j] == i):
            #         char_com.append(j)
            # answer.append(char_com[-1] - char_com[-2])

    return answer

print(solution(s))