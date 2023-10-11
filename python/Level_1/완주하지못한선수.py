participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

def solution(participant, completion):
    answer = ''
    winner = {}

    for player in completion:
        if player not in winner:
            winner[player] = 1
        else:
            winner[player] += 1

    print(winner)

    for i in participant:
        if(i in winner):
            winner[i] -= 1
    for i in participant:
        if(i not in winner or winner[i] != 0):
            answer = i

    return answer

print(solution(participant, completion))