my_string = "He11oWor1d"
overwrite_string ="lloWorl"
s = 2

def overwriting_Strings(my_string, overwrite_string,  s):
    answer = ''
    str1 = ''
    str2 = ''
    str3 = ''
    for i in range(s):
        str1 += my_string[i]

    for i in range(s , s + len(overwrite_string)):
        str2 += my_string[i]
    str2 = overwrite_string
    
    for i in range(s + len(overwrite_string), len(my_string)):
        str3 += my_string[i]

    answer = str1 + str2 + str3
    #answer =my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]
    
    return answer
answer = overwriting_Strings(my_string, overwrite_string,  s)
print(answer)
