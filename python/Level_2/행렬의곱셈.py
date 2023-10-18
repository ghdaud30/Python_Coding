import numpy as np

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]	

def solution(arr1, arr2):

    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    answer = np.dot(arr1,arr2)
    answer = answer.tolist()

    return answer

print(solution(arr1,arr2))