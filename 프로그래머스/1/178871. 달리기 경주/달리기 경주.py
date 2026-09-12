def solution(players, callings):
    ans = players.copy()
    players_dict = {}
    for i in range(len(players)):
        players_dict[players[i]] = i
    for i in range(len(callings)):
        prev = ans[players_dict[callings[i]] - 1]
        cur = ans[players_dict[callings[i]]] # 호출된 선수
        ans[players_dict[callings[i]] - 1], ans[players_dict[callings[i]]] = cur, prev
        players_dict[cur] -= 1
        players_dict[prev] += 1
    return ans