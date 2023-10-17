want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]


def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount)):
        count = 10
        discount_dic = {i : v for i , v in zip(want,number)}
        day = discount[i:i + count]

        for j in day:
            if(j in discount_dic):
                discount_dic[j] -= 1
                count -= 1
                if(discount_dic[j] <= -1):
                    break

            if(count == 0):
                answer += 1
                break

    return answer

print(solution(want, number, discount))