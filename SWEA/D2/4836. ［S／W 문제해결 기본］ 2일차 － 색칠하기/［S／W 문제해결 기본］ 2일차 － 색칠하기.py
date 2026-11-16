T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    nlist = [[0] * (10) for _ in range(10)]
    cnt = 0
    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                nlist[i][j] += 1
                if nlist[i][j] > cnt:
                    cnt = nlist[i][j]
    ans = 0
    for i in range(10):
        for j in range(10):
            if nlist[i][j] == cnt:
                ans += 1
    print(f"#{test_case} {ans}")
    # ///////////////////////////////////////////////////////////////////////////////////
