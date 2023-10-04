def 옹알이(babbling):
    answer = 0
    key = ["aya", "ye", "woo", "ma" ]

    for i in range(len(babbling)):
        c = babbling[i]
        for j in key:
            if(j in c):
                c = c.replace(j,"-")

        result = all(x == '-' for x in c)
        if(result):
            answer += 1

    return answer
