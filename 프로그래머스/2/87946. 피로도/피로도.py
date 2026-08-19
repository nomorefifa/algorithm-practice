def solution(k, dungeons):
    visited = [False] * (len(dungeons))
    case = []
    def dfs(tmp_case):
        for i in range(len(dungeons)):
            if visited[i] == True:
                continue
            tmp_case.append(i)
            visited[i] = True
            if len(tmp_case) == len(dungeons):
                case.append(tmp_case.copy())
            dfs(tmp_case)
            visited[i] = False
            tmp_case.pop()
    dfs([])
    ans = 0
    for i in range(len(case)):
        cnt = 0
        tmp_k = k
        for j in range(len(case[i])):
            if dungeons[case[i][j]][0] <= tmp_k:
                tmp_k -= dungeons[case[i][j]][1]
                cnt += 1
        if cnt > ans:
            ans = cnt
    return ans