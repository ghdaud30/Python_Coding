from collections import Counter

k = 2
tangerine = [1, 1, 1, 1, 2, 2, 2, 3]

def solution(k, tangerine):
    count = 0
    orange_list = Counter(tangerine).most_common()
    print(orange_list)
    for i in orange_list:
        k -= i[1]
        count += 1
        if(k <= 0):
            break
    
    return count

print(solution(k,tangerine))