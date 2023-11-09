N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]	

def solution(N, stages):
    fail_rate = {}
    total_user = len(stages)
    #각 단계별로 도전하고 있는 유저와 성공한 유저를 구합니다
    for i in range(1, N + 1): 
        under_stage = stages.count(i)        
        try:
            fail_rate[i] = under_stage / total_user
        # 도전하고 있는 유저가 없으면 에러 처리해서 0으로 만듬
        except ZeroDivisionError:
            fail_rate[i] = 0
        total_user -= under_stage
    
    #방금 구한 각 스테이지별 실패율을 기준으로 내림차순 해주고
    # 같은 실패율일 경우 스테이지별로 오름차순 해줍니다
    sorted_items = sorted(fail_rate, key=lambda x : (fail_rate[x],-x), reverse=True)

    print(fail_rate)
    
    return sorted_items

print(solution(N, stages))