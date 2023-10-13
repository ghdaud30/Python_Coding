import datetime

today =  "2020.12.17"
terms =  ["A 12"]
privacies =  ["2010.01.01 A", "2019.12.17 A"]

def solution(today, terms, privacies):
    answer = []
    terms_dic = {term[0] : term[2:] for term in terms}
    print(terms_dic)

    today_year , today_month , today_days = map(int, today.split("."))
    today = '.'.join([str(today_year), str(today_month), str(today_days)])

    for idx , i in enumerate(privacies):

        expire_date = []
        first = i[:-2]
        last = i[-1]

        expire = first.split('.')
        year = int(expire[0])
        month = int(expire[1])
        days = int(expire[-1])

        extra = int(terms_dic[last]) * 28 
        print('extra',extra)
        add_month = extra // 28
        print('add_month',add_month)
        add_days = extra % 28
        print('add_days',add_days)
        print(extra)
        
        days += add_days
        days -= 1
        if(days == 0):
            days = 28
            month -= 1
        elif(days > 28):
            month += days // 28
            days %= 28

        month += add_month
        if(month > 12):
            year += month // 12
            month %= 12
        elif(month == 12):
            year += 1
            month = 1

        print(year)
        print(month)
        print(days)

        expire_date.append(str(year))
        expire_date.append(str(month))
        expire_date.append(str(days))

        expire_period = '.'.join(expire_date)

        # date_today = datetime.datetime.strptime(today,"%Y.%m.%d")
        # date_expire = datetime.datetime.strptime(expire_period,"%Y.%m.%d")

        # if(date_today > date_expire):
        #     answer.append(idx+1)

        print(today)
        print(expire_period)

    return answer

print(solution(today, terms, privacies))