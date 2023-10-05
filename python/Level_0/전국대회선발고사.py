rank = [3, 7, 2, 5, 4, 6, 1]
attendance = [False, True, True, True, True, False, False]	

def 전국대회선발고사(rank,attendance):
    answer = 0
    top = {}
    top3 = []

    for idx, (i , v) in enumerate(zip(rank,attendance)):
        if(v == True):
            top[idx] = i
            
    top_sort = dict(sorted(top.items(), key=lambda item: item[1]))

    for i in top_sort:
        top3.append(i)

    top3 = top3[:3]
    for i in range(len(top3)):
        if(i == 0): answer += 10000 * top3[i]
        elif(i == 1): answer += 100 * top3[i]
        elif(i == 2): answer += top3[i]

    return answer

print(전국대회선발고사(rank,attendance))