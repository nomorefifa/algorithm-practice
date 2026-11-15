T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    nlist = list(input().split())
    if n % 2 == 0:
        l = nlist[:n // 2]
        r = nlist[n//2:]
    else:
        l = nlist[:n // 2 + 1]
        r = nlist[n // 2 + 1:]
    ans = []
    for i in range(n // 2):
        ans.append(l[i])
        ans.append(r[i])
    if n % 2 != 0:
        ans.append(l[-1])
    print(f"#{test_case} {' '.join(ans)}")
    # ///////////////////////////////////////////////////////////////////////////////////
