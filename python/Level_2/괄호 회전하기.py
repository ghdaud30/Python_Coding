s = "}}}"	

def solution(s):
    answer = 0
    rule = [ ')', ']', '}']
    
    for x in range(len(s)):
        part = []
        new_s = s[x:] + s[:x]
        # print(new_s)
        
        for j in range(len(s)):               
            
            if(len(part) >= 3):
                if(part[-2] == '(' and part[-1] == rule[0]):
                    part.pop()
                    part.pop()
                if(part[-2] == '[' and part[-1] == rule[1]):
                    part.pop()
                    part.pop()            
                if(part[-2] == '{' and part[-1] == rule[2]):
                    part.pop()
                    part.pop()                  
            
            if(len(part) == 0):
                part.append(new_s[j])
                if(part[0] in rule):
                    break
            else:             
                if(part[0] == '(' and new_s[j] == rule[0]):
                    part.pop(0)
                elif(part[0] == '[' and new_s[j] == rule[1]):
                    part.pop(0)
                elif(part[0] == '{' and new_s[j] == rule[2]):
                    part.pop(0) 
                else:
                    part.append(new_s[j])
     

        # for i in range(len(part)):
        #     if(part[i] in rule):
                    
        print(part)
                 
        
        if(len(part) == 0):
            answer += 1
                    
        
    
    return answer

print(solution(s))