X = '3403'
Y = '13203'

def 숫자_짝꿍(X, Y):
    answer = ''
    count = []
    for i in range(len(X)):
        for j in range(len(Y)):
            if(X[i] == Y[j]):
                if(X[i] not in count):
                    count.append(X[i])
                    continue
                else:
                    if(count.count(X[i]) != Y.count(Y[j])):
                        count.append(X[i])

    if(not count):
        return '-1'
    else:
        if all (item == '0' for item in count):
            count = list(set(count))
            return '0'
        else:
            count.sort(reverse=True)
            answer = ''.join(count)

    return answer

print(숫자_짝꿍(X, Y))