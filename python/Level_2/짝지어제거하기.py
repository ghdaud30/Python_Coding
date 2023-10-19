s = 'aaccdeedbgg'

def solution(s):
    word = []
    
    for idx , i in enumerate(s):
        
        if(len(word) == 0):
            word.append(i)
            continue
        
        if(word[-1] != i):
            word.append(i)
        else:
            word.pop()
            
    if(len(word) == 0):
        return 1
    else:
        return 0
    
    


    

print(solution(s))