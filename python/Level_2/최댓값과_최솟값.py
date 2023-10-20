s = "1 2 3 4"


def solution(s):
    answer = ''
    s = list(map(int ,s.split()))
    print(s)
    answer += str(min(s))
    answer += ' '
    answer += str(max(s))

    return str(min(s)) + ' ' + str(max(s))

print(solution(s))