x = "12321"	
y = '42531'

def solution(x, y):
    answer = ''
    x_dict = {}
    y_dict = {}
    num = []
    
    #x와 y 연속된 값 딕셔너리를 만듭니다
    for i in x:
        if(i not in x_dict):
            x_dict[i] = 1
        else:
            x_dict[i] += 1
    for i in y:
        if(i not in y_dict):
            y_dict[i] = 1
        else:
            y_dict[i] += 1
    
    # 둘중 작은 값으로 범위를 한정하여 공통된 값을 구합니다
    if(len(x) > len(y)):
        for i in y_dict:
            if(i in x_dict):
                result = min(x_dict[i],y_dict[i])
                num.extend([i] * result) 
    else:
        for i in x_dict:
            if(i in y_dict):
                result = min(x_dict[i],y_dict[i])
                num.extend([i] * result)             
    
    #갯수가 없으면 -1 있을때 0으로속해있으면 0 
    # 그 외에는 정렬하여 더해줍니다
    if(len(num) == 0):
        return '-1' 
    else:
        if all(char== '0' for char in num):
            return '0'
        
        num.sort(reverse = True)
        for i in num:
            answer += str(i)    
    
    return answer

print(solution(x,y))