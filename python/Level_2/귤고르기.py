from itertools import combinations

k = 2
tangerine = [1, 1, 1, 1, 2, 2, 2, 3]

def solution(k, tangerine):
    answer = 0
    orange_dic = {}

    for i in tangerine:
        if(i not in orange_dic):
            orange_dic[i] = 1
        else:
            orange_dic[i] += 1

    print(list(orange_dic.items()))
    
    # for i in range(k):



    return answer

print(solution(k,tangerine))