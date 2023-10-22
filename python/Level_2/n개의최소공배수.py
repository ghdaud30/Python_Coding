import math

arr = [2,6,8,14]

def solution(arr):
    answer = 0

    for i in range(1 ,  len(arr)):
        gcd = math.gcd(arr[i - 1], arr[i])
        lcd = int(arr[i - 1] * arr[i] / gcd)
        arr[i] = lcd

    
    return arr[-1]  
    

print(solution(arr))