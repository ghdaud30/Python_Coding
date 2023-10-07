s = "FHAAXZ"
n = 4

def 시저암호(s, n):
    answer = ''
    
    for i in range(len(s)):
        if(s[i] == ' '):
            answer += s[i] 
            continue

        if ord(s[i]) in range(ord('a') , ord('z') + 1):
            if(ord(s[i]) + n > ord('z')):
                new_char = (ord(s[i]) + n) % ord('z')
                answer +=  chr(new_char + ord('a'))
                continue
            else:
                answer += chr(ord(s[i]) + n)
                continue

        if ord(s[i]) in range(ord('A') , ord('Z') + 1):
            if ord(s[i]) + n > ord('Z'):
                new_char = (ord(s[i]) + n) % ord('Z')
                answer +=  chr(new_char + ord('A'))
                continue
            else:
                answer += chr(ord(s[i]) + n)
                continue

    return answer

print(시저암호(s, n))