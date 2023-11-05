answers = [4,4,4,2,3]
def solution(answers):
    answer = []
    # 10000개를 만들어줌
    a = [1, 2, 3, 4, 5] * 2000
    b = [2, 1, 2, 3, 2, 4, 2, 5] * 1300
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    score = [0,0,0]
    
    # 각 학생 별로 점수 처리
    for z,x,v,an in zip(a,b,c,answers):
        if(z == an):
            score[0] += 1
        if(x == an):
            score[1] += 1
        if(v == an):
            score[-1] += 1
    
    # 점수를 확인하여 답에 넣어줌
    for idx , s in enumerate(score,1):
        if(s == max(score)):
            answer.append(idx)        
    
    return answer

print(solution(answers))