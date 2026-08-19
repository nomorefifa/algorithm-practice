def solution(k, dungeons):
    visited = [False] * len(dungeons)
    answer = 0

    def dfs(k, cnt):
        nonlocal answer

        answer = max(answer, cnt)

        for i in range(len(dungeons)):
            if visited[i]:
                continue

            minimum, consume = dungeons[i]

            if k < minimum:
                continue

            visited[i] = True

            dfs(k - consume, cnt + 1)

            visited[i] = False

    dfs(k, 0)

    return answer