import sys
sys.setrecursionlimit(10**6)
def solution(n, wires):
    ans = 1000000000000000
    def dfs(v):
        cnt = 1
        visited[v] = True
        for next in x[v]:
            if not visited[next]:
                cnt += dfs(next)
        return cnt
    for i in range(len(wires)):
        visited = [False] * (101)
        tmp = []
        x = [[] for _ in range(101)]
        for j in range(len(wires)):
            if i == j:
                continue
            x[wires[j][0]].append(wires[j][1])
            x[wires[j][1]].append(wires[j][0])
        for k in range(1, 101):
            if not visited[k]:
                tmp_cnt = dfs(k)
                tmp.append(tmp_cnt)
        if ans > abs(tmp[0] - tmp[1]):
            ans = abs(tmp[0] - tmp[1])
    return ans