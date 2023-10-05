k = 3
m = 4
score = 	[1, 2, 3, 1, 2, 3, 1]	

def 과일장수(k,m,score):
    answer = 0
    apple = []
    apple2 = []
    count = len(score) // m
    min_value = k + 1
    score.sort(reverse = True)
    print(score)

    for i in range(count*m):
        apple2.append(score[i])
        if(len(apple2) == m):
            apple.append(apple2)
            apple2 = []
            continue
    
    # min 함수 이용하여 리스트의 최소값 구하기
    for i in range(len(apple)):
        answer +=  min(apple[i]) * m


    # for i in range(len(apple)):
    #     for j in range(len(apple[i])):
    #         if(apple[i][j] < min_value):
    #             min_value = apple[i][j]
    #     answer += min_value * m      

    print(apple)       

    return answer

print(과일장수(k,m,score))

