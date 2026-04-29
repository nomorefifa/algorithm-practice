

def solution(n, wires):
    ans = 1000000000000

    def dfs(node):
        nonlocal cnt
        visited[node] = True
        for k in cur_wires[node]:
            if not visited[k]:
                cnt += 1
                dfs(k)
    
    for i in range(n - 1):
        tmp_wires = wires[:i] + wires[i + 1:]
        cur_wires = [[] for _ in range(n + 1)]
        for tmp in tmp_wires:
            cur_wires[tmp[0]].append(tmp[1])
            cur_wires[tmp[1]].append(tmp[0])
        visited = [False] * (n + 1)
        cnt = 1
        
        dfs(1)
    
        rest = n - cnt
        if abs(rest - cnt) < ans:
            ans = abs(rest - cnt)
        
    return ans