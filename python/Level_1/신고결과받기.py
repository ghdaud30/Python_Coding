id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

def solution(id_list, report, k):

    answer = []
    report =  list(set(report))
    mine = {i : [] for i in id_list}
    declaration = {i : 0 for i in id_list}
    self_ban = {i : 0 for i in id_list}
    stop_user = []

    #딕셔너리에서 처음 신고된 값만 허용 되게 사용
    for user in report:     
        me,you = user.split(' ')

        #신고한 아이디와 신고당한 횟수 추가
        if(self_ban[me] != you):
            self_ban[me] = you
            mine[me].append(you)
            declaration[you] += 1
        else:
            continue

    print(mine)
    print(declaration)

    # 신고 횟수가 k번 이상인 아이디를 리스트에 추가
    for key,v in declaration.items():
        if(v >= k):
            stop_user.append(key)

    print(stop_user)

    # 신고한 아이디를 리스트와 비교하여 answer에 값 추가
    for key,v in mine.items():
        count = 0
        for value in v:
            if(value in stop_user):
                count += 1
        answer.append(count)
            
    return answer

print(solution(id_list, report, k))