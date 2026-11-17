T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, m = map(int, input().split())
    nlist = list(map(int, input().split()))
    max_s = 1e-9
    min_s = 1e9 
    for i in range(n - m + 1):
        tmp_s = 0
        for j in range(i, i + m):
            tmp_s += nlist[j]
        if tmp_s > max_s:
            max_s = tmp_s
        if tmp_s < min_s:
            min_s = tmp_s
    print(f"#{test_case} {max_s - min_s}")
    # ///////////////////////////////////////////////////////////////////////////////////
