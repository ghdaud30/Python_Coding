babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]	

def solution(babbling):
    answer = 0 
    pro = ['aya','ye','ma','woo']

    # for i in babbling:
    #     for j in pro:
    #         if j * 2 not in i:
    #             i = i.replace(j,'')
    #     if(len(i.strip()) == ''):
    #         answer += 1

    for i in babbling:
        new_i = []

        #각 단어별로 발음을 확인을 합니다
        while(True):
            if(i == ''):
                break
            if(i.startswith('aya')):
                new_i.append('aya')
                i = i.replace('aya','',1)
            elif(i.startswith('ye')):
                new_i.append('ye')
                i = i.replace('ye','',1)
            elif(i.startswith('woo')):
                new_i.append('woo')
                i = i.replace('woo','',1)
            elif(i.startswith('ma')):
                new_i.append('ma')
                i = i.replace('ma','',1)
            else:
                break
        
        #while 루프를 돌고난이후에 i값이 사라져서 공백일때
        # 리스트에 넣어준 값 new_i을 순환해서 
        # 연속적으로 단어가 나오는지 확인합니다
        if(i == ''):
            count = 0
            for j in range(1, len(new_i)):
                try:
                    if(new_i[j] == new_i[j-1]):
                        count = 1
                        break
                except:
                    pass
            #count 변수를 이용해서 연속된 단어가 나오면
            #다음으로 넘어갑니다
            if(count == 1):
                continue
            else:
                answer += 1
                   
    return answer

print(solution(babbling))