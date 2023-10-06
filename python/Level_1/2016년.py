import datetime

a = 5
b = 24

def solution(a, b):
    answer = ''
    now = datetime.datetime(2016,a,b)

    day_week = now.strftime('%a')
    answer = day_week.upper()

    return answer

print(solution(a,b))