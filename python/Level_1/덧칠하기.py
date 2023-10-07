n = 8
m = 4 
section = [2,3,6] 


def 덧칠하기(n, m, section):
    answer = 0

    wall = [False for i in range(1,n+1)] # [False] * n
    for sec in section:
        wall[sec-1] = True
    # wall = [True if i in section else False for i in range(1,n + 1)]

    for i in range(len(wall)):
        if(wall[i]):
            for j in range(i,i+m):
                if j < len(wall):
                    wall[j] = False
                else:
                    pass
            answer += 1


    return answer

print(덧칠하기(n, m, section))