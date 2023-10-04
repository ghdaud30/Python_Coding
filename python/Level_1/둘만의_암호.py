s = "aukks"	
skip = 'wbqd'
index = 5

def 둘만의_암호(s,skip,index):
    answer =''
    alphabet = []
    
    for letter in range(ord('a'), ord('z')+1):
        if(chr(letter) not in skip):
            alphabet.append(chr(letter))

    for i in s:
        change = alphabet.index(i) + index
        if change < len(alphabet):
            answer += alphabet[change]
        else:
            change %= len(alphabet)
            answer += alphabet[change]

    return answer

print(둘만의_암호(s,skip,index))