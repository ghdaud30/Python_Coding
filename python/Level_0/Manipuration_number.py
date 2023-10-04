a = 2
b = 2
c = 2
d = 2


def Manipuration_number(a, b, c, d):
    answer = 0
    if(a == b == c == d):
        answer = 1111 * a
        return answer
    elif( a == c == d and b != a ):
        answer = (10 * a + b)**2
        return answer
    
print(Manipuration_number(a,b,c,d))