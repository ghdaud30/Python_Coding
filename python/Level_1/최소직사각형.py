sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

def solution(sizes):
    first = []
    second = []

    for i , size in enumerate(sizes):
        size.sort()
        first.append(size[0])
        second.append(size[1])

    print(first)
    print(second)
    
    return max(first) * max(second)

print(solution(sizes))