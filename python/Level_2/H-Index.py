citations = [8,7,7,7,7,7,7,7,7,2,1]

def solution(citations):
    answer = 0
    citations.sort(reverse = True)

    for i in range(len(citations), -1 , -1):
        if(citations[i] >= answer):
            answer += i
            


print(solution(citations))