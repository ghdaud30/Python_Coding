str = input()
str1 = ''
if(1<= len(str) <=20):
    for i in str:
        if(i.isupper()):
            str1 += i.lower()
        else:
            str1 += i.upper()
    str = str1
    print(str)
else:
    print("Try Again")