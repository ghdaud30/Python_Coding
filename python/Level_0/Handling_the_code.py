code = "abc1abc1abc"

def Handling_the_code(code):
    answer = ''
    mode = 0
    for i in range(len(code)):
        if (mode == 0):
            if(code[i] != "1"):
                if(i % 2 == 0):
                    answer += code[i]
            if(code[i] == "1"):
                mode = 1
        else:
            if(code[i] != "1"):
                if(i % 2 == 1):
                    answer += code[i]
            if(code[i] == "1"):
                mode = 0
    if(answer == ""):
        return "EMPTY"
    else:
        return answer

print(Handling_the_code(code))