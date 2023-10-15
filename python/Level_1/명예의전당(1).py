k = 4
score = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]

def solution(k, score):
    lowest = []
    rank = []

    for i in score:
        if(len(rank) < k):
            rank.append(i)
            rank.sort(reverse=True)
            lowest.append(rank[-1])
        else:
            if(i > min(rank)):
                rank[-1] = i
                rank.sort(reverse=True)
                lowest.append(rank[-1])
            else:
                lowest.append(rank[-1])
    print(rank)
    


    return lowest

print(solution(k, score))