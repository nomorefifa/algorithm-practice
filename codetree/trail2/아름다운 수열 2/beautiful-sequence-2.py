N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
if N < M:
    print(0)
    exit(0)

m_dict = {}
for i in range(M):
    if B[i] in m_dict:
        m_dict[B[i]] += 1
    else:
        m_dict[B[i]] = 1

ans = 0
for i in range(N - M + 1):
    n_dict = {}
    for j in range(M):
        if A[i + j] in n_dict:
            n_dict[A[i + j]] += 1
        else:
            n_dict[A[i + j]] = 1

    cnt = 0
    for k in m_dict.keys():
        if k in n_dict and m_dict[k] == n_dict[k]:
            cnt += 1
    if cnt == len(m_dict.keys()):
        ans += 1
print(ans)