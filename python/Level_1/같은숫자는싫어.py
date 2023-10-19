arr = [1,1,3,3,0,1,1]

def solution(arr):
    answer = []
    num = []
    
    num.append(arr[0])
    answer.append(arr[0])
    del arr[0]
    
    for i in arr:
        first = num.pop()
        if(first == i):
            num.append(i)
        else:
            num.append(i)
            answer.append(i)
            
    print(num)    
    
    return answer

print(solution(arr))