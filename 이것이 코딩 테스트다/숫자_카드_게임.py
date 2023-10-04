n,m = map(int,input().split())

def 숫자_카드_게임(n,m):
    answer = 0
    for i in range(n):
        data = list(map(int,input().split()))
        min_value = min(data)
        answer = max(min_value,answer)

    return answer

print(숫자_카드_게임(n,m))