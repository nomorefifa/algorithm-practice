from collections import deque
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    v, e = map(int, input().split())
    vlist = [[] for _ in range(v + 1)]
    visited = [False] * (v + 1)
    for i in range(e):
        x, y = map(int, input().split())
        vlist[x].append(y)
        vlist[y].append(x)
    s, g = map(int, input().split())
    ans = 51
    visited[s] = True
    q = deque()
    q.append((s, 0))
    while q:
        node, cnt = q.popleft()
        if node == g:
            ans = cnt
            break
        for next_node in vlist[node]:
            if not visited[next_node]:
                q.append((next_node, cnt + 1))
                visited[next_node] = True
    if ans == 51:
        print(f"#{test_case} 0")
    else:
    	print(f"#{test_case} {ans}")
    # ///////////////////////////////////////////////////////////////////////////////////
