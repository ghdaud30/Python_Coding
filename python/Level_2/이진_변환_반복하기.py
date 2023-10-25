s = "110010101001"

def solution(s):
    trans = 0
    count = 0

    while(True):
        if(s == '1'):
            return [trans,count]
        
        s_count = s.count('0')
        s = s.replace('0','')
        length = len(s)
        count += s_count

        s = bin(length)[2:]
        trans += 1
        
print(solution(s))