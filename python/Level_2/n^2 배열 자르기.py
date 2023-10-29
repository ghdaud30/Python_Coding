n = 4
left = 7
right = 14

def solution(n, left, right):
    answer = []
    
    # 배열의 각 값은 행과 열에서 제일 큰값 +1임
    # 이 문제는 n의 크기가 크므로 2차원 배열을 만들지 않고
    # left와 right 범위의 값만 구하여야함
    # 범위의 i 값을 n을 나눈 몫과 나머지 값으로 
    # 1차원배열에 행과 열을 알 수 있음
    for i in range(left,right+1):
        low = i // n
        col = i % n
        max(low+1,col+1)
        answer.append(max(low+1,col+1))
    
    return answer

print(solution(n,left,right))