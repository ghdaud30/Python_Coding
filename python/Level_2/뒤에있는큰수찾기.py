from collections import deque

numbers = [2, 3, 3, 3, 5]

def solution(numbers):
    answer = []
    queue = deque()
    
    for i in range(len(numbers)):
        if(len(queue) == 0):
            queue.append(numbers[i])
            continue
        
        if(numbers[i] != queue[0]):
            first = queue.popleft()
        else:
            pass
                    
        if(first < numbers[i]):
            answer.append(numbers[i])
            queue.append(numbers[i])
        elif(first == numbers[i]):
            queue.append(numbers[i])
        else:
            answer.append(-1)

    return answer

print(solution(numbers))