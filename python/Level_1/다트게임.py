import re

dartResult = '1D2S3T*'
def solution(dartResult):
    answer = 0

    rank_dic = {'S' : 1 , 'D' : 2 , 'T': 3}
    cur = 0
    dart_index = []
    sum = []

    #정규 표현식을 사용하여 dartResult를 3묶음으로 나눔
    pattern = r'(\d+)([A-Z]+)([*,#]*)'
    dart_list = re.findall(pattern,dartResult)

    for dart in dart_list:
        # 묶음에서 0번은 숫자 1번은 문자
        num = int(dart[0])
        rank = dart[1]

        # *나 #를 확인하여 다른 로직을 처리함
        if(dart[-1] == '*' or dart[-1] == '#'):
            if(dart[-1] == '*'):
                cur = pow(num,rank_dic[rank]) * 2
                sum.append(cur)
                if(len(sum) >= 2):
                    sum[sum.index(cur) - 1] *= 2
            elif(dart[-1] == '#'):
                cur = pow(num,rank_dic[rank]) * (-1)
                sum.append(cur)
            else:
                cur = pow(num,rank_dic[rank])
                sum.append(cur)
        else:
            cur = pow(num,rank_dic[rank])
            sum.append(cur)

    print('sum',sum)
    for i in sum:
        answer += i
    
    return answer

print(solution(dartResult))