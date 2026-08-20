def solution(k, dungeons):
    visited = [False] * len(dungeons)
    def dfs(k, cnt):
        ans = cnt
        for i in range(len(dungeons)):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                ans = max(ans, dfs(k - dungeons[i][1], cnt + 1))
                visited[i] = False
        return ans
    return dfs(k, 0)