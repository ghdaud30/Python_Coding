s = "(()("

def solution(s):
    stack = []

    for i in s:   
        if(i == '('):       
            stack.append(i)
        else:
            if(len(stack) == 0):    #처음에 ')'로 시작하면 False
                return False
            else:
                final = stack.pop()    #스텍에서 마지막 요소를 빼주고 괄호 완성 ()
                if(final == i):
                    continue

    if(len(stack) == 0): # 루프들 다 돌고 나서 스텍이 비어있으면 True
        return True
    else:           # 스텍에 남아있으면 False
        return False

print(solution(s))