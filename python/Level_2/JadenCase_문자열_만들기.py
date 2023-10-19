s = "3people            unFollowed me"


def solution(s):
    answer = ''
    new_s = s.split(' ')
    
    for v , i in enumerate(new_s):
        if(i.isdigit()):
            if(v == len(new_s) - 1):
                answer += i
                break
            answer += i + ' '
            continue
        else:
            i = i.capitalize()
            if(v == len(new_s) - 1):
                answer += i
                break
            answer += i + ' '
            
    return answer

print(solution(s))