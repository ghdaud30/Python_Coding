s = "}]()[{"	

def solution(s):
    answer = 0
    word = [']',')','}']
    new_s = []
    
    # 왼쪽으로 회전 시킨 새로운 s를 만들어서 리스트에 담아둡니다.
    for x in range(len(s)):
        if(x == 0):
            new_s.append(s)
            continue
        else:
            s = s[1:] + s[0]
            new_s.append(s)
    print(new_s)
    
    # 담아둔 리스트를 순환합니다.
    for i in new_s:
        bracket = []
        for j in i:
            #처음 괄호가 닫는 괄호일 경우 break를 합니다.
            if(len(bracket) == 0 and j in word):
                bracket.append(j)
                break
            # 그렇지 않으면 스텍에 넣어줍니다.
            elif(len(bracket) == 0):
                bracket.append(j)
            #그 후 쌍이 맞으면 pop을 하고 맞지 않으면 스텍에 넣어줍니다.
            else:
                if(bracket[-1] == '[' and j == ']'):
                    bracket.pop(-1)
                elif(bracket[-1] == '{' and j == '}'):
                    bracket.pop(-1)
                elif(bracket[-1] == '(' and j == ')'):
                    bracket.pop(-1)
                else:
                    bracket.append(j)
        #순환을 돌고난 후에 스택이 비어져있으면 올바른 괄호 문자열이고
        #남아 있다면 올바르지 않는 괄호 문자열 입니다.
        if(len(bracket) == 0):
            answer += 1

    return answer

print(solution(s))