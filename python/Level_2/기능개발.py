progresses = [93, 30, 55]
speeds = [1, 30 , 5]

def solution(progresses, speeds):
    answer = []
    process = []
    count1 = 1

    for idx , progress in enumerate(progresses):
        count = 0
        while(progress < 100):
            progress += speeds[idx] 
            count += 1
        process.append(count)
    
    first = process[0]

    for i in range(1,len(process)):
        if(first >= process[i]):
            count1 += 1
        else:
            answer.append(count1)
            count1 = 1
            first = process[i]

    answer.append(count1)

    print(process)

    return answer

print(solution(progresses, speeds))