s = "banana"

def solution(s):
    answer = []
    char = []
    char_com = []
    char2 = {}

    for i in range(len(s)):
        if(s[i] not in char2):
            answer.append(-1)
        else:
            answer.append(i-char2[s[i]])
        char2[s[i]] = i

    # for i in s:
    #     if(i not in char):
    #         char.append(i)
    #         answer.append(-1)
    #     else:
    #         char.append(i)

    #         for j in range(len(char)):
    #             if(char[j] == i):
    #                 char_com.append(j)
    #         answer.append(char_com[-1] - char_com[-2])

    return answer

print(solution(s))