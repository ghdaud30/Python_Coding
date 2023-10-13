id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

def solution(id_list, report, k):
    answer = []
    mine = {i : [] for i in id_list}
    declaration = {i : 0 for i in id_list}
    self_ban = {i : 0 for i in id_list}
    stop_user = []

    for user in report:
        me,you = user.split(' ')

        if(self_ban[me] != you):
            self_ban[me] = you
            mine[me].append(you)
            declaration[you] += 1
        else:
            continue

    print(mine)
    print(declaration)
    
    for key,v in declaration.items():
        if(v == k):
            stop_user.append(key)
    print(stop_user)

    for key,v in mine.items():
        count = 0
        for value in v:
            if(value in stop_user):
                count += 1
        answer.append(count)
            
    return answer

print(solution(id_list, report, k))