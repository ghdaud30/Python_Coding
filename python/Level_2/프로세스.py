from collections import deque

priorities = [10, 1, 9, 1, 1, 1]
location = 0

def solution(priorities, location):
    count = 0
    # 힙 변수
    queue = deque(priorities)
    # location 추적 변수
    record = deque([i for i in range(len(priorities))])

    while(True):
        first = queue.popleft()       
        record1 = record.popleft()

        if(len(queue) != 0):  
            if(first < max(queue)):
                queue.append(first)
                record.append(record1)
            else:
                count += 1
                if(record1 == location):
                    return count
        else:
            if(record1 == location):
                count += 1
                return count


print(solution(priorities, location))



