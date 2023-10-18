A = [1, 2]
B = [3, 4]

def solution(A,B):
    A.sort()
    B.sort(reverse = True)
    print(A)
    print(B)
    sum = 0

    for i , v in zip(A,B):
        sum += i * v    

    return sum

print(solution(A,B))