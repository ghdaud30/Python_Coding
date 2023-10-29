phone_number = "027778888"	

def solution(phone_number):
    answer = ''
    
    for i in range(len(phone_number) - 4):
        answer += '*'
    
    answer += phone_number[-4:]
    
    return answer

print(solution(phone_number))