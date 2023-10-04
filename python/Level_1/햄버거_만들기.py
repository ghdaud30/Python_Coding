ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]	

def 햄버거_만들기(ingredient):
    answer = 0
    ing = ''.join(map(str, ingredient)) 
    while True:
        if '1231' in ing:
            answer += ing.count('1231') 
            ing = ing.replace('1231','')
        else: 
            break
    return answer




print(햄버거_만들기(ingredient))



