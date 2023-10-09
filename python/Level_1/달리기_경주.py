

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

def solution(players, callings):
    answer = []
    dic_players = { players.index(i) : i for i in players}
    print(dic_players)
    
    for i in callings:
        player = dic_players[players.index(i)]
        dic_players[players.index(i) - 1] = i 
        dic_players[players.index(i)] = player

    return dic_players

print(solution(players, callings))
