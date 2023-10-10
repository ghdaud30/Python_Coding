

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

def solution(players, callings):
    dic_players = { v : i for i , v in enumerate(players)}
    print(dic_players)

    for i in callings:
        num = dic_players[i]            #3
        dic_players[i] -= 1             #2
        dic_players[players[num - 1]] += 1      #
        players[num] = players[num - 1]
        players[num - 1] = i

    print(dic_players)

    return players

print(solution(players, callings))
