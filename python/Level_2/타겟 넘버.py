numbers = [1, 1, 1, 1, 1]	
target = 3

def solution(numbers, target):
    global answer
    answer = 0

    def num (idx,sum):
        global answer
        
        if(len(numbers) == idx):
            if(sum == target):
                print(f'합계 : {sum}')
                answer += 1
            return    
        
        # 각 dfs 함수마다 
        # 플러스값 마이너스값으로 재귀를 해줍니다
        num(idx + 1, sum + numbers[idx])
        num(idx + 1, sum - numbers[idx])
        
    num(0,0)
    
    return answer

print(solution(numbers,target))