# food = [1, 3, 4, 6]
# result = "1223330333221"
list2 = [0]
food = [1, 7, 1, 2]
result = "111303111"


def food_Fight(food):
    answer = ''
    list2 = [0]
    for i,v in reversed(list(enumerate(food))):
        while(True):
            if(v % 2 == 0):
                if(v <= 0):
                    break
                list2.insert(0,i)
                list2.insert(len(list2),i)
                v -= 2
            elif(v == 1):
                 break
            elif( v % 2 == 1):
                if(v <= 0):
                    break 
                list2.insert(0,i)
                list2.insert(len(list2),i)
                v -= 3
    answer = ''.join(str(s) for s in list2)
    return answer

print(food_Fight(food))

# for i,v in reversed(list(enumerate(food))):
#     while(True):
#             if(v % 2 == 0):
#                 if(v <= 0):
#                     break
#                 list2.insert(0,i)
#                 list2.insert(len(list2),i)
#                 v -= 2
#             elif(v == 1):
#                  break
#             elif( v % 2 == 1):
#                 if(v <= 0):
#                     break 
#                 list2.insert(0,i)
#                 list2.insert(len(list2),i)
#                 v -= 3

# answer = ''.join(str(s) for s in list2)
# print(answer)