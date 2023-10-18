land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]


def solution(land):
    answer = 0
    next = -1
    big = 0

    for part in land:
        if(next == -1):
            max_part = max(part)
            next = part.index(max_part)
            answer += max_part
        else:
            if(next != part.index(max(part))):
                max_part = max(part)
                next = part.index(max_part)
                answer += max_part
            else:
                max_part = max(part)
                for i in part:
                    if(big < i and i != max_part):
                        big = i
                answer += big
                max_part = big
                next = part.index(max_part)


    return answer

print(solution(land))