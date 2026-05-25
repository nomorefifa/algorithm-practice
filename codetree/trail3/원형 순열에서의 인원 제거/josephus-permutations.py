from collections import deque
n, k = map(int, input().split())

ans = []
q = deque([i for i in range(1, n + 1)])
while q:
    for i in range(k):
        tmp = q.popleft()
        if i == k - 1:
            ans.append(str(tmp))
        else:
            q.append(tmp)
print(" ".join(ans))