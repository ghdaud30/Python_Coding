s = "1 2 3 4"


def solution(s):
    s = list(map(int ,s.split()))
    print(s)

    return str(min(s)) + ' ' + str(max(s))

print(solution(s))