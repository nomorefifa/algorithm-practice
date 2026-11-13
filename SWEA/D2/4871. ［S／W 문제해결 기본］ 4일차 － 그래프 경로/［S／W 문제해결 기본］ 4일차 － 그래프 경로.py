T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def dfs(node):
    global flag
    visited[node] = True
    if node == g:
        flag = True
        return
    for next_node in vlist[node]:
        if not visited[next_node]:
            dfs(next_node)
            
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    v, e = map(int, input().split())
    vlist= [[] for _ in range(v + 1)]
    for i in range(e):
        v1, v2 = map(int, input().split())
        vlist[v1].append(v2)
        # vlist[v2].append(v1)
    s, g = map(int, input().split())
    visited = [False] * (v + 1)
    flag = False
    dfs(s)
    if flag:
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")
    # ///////////////////////////////////////////////////////////////////////////////////
