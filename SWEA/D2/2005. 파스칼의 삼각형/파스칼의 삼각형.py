T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    nlist = [[1]]
    for i in range(n - 1):
        tmp = []
        for j in range(i + 2):
            if j - 1 < 0:
                left = 0
            else:
                left = nlist[i][j - 1]
            if j < len(nlist[i]):
                right = nlist[i][j]
            else:
                right = 0
            tmp.append(left + right)
        nlist.append(tmp)
    print(f"#{test_case}")            
    for i in range(n):
        print(" ".join(map(str, nlist[i])))
    # ///////////////////////////////////////////////////////////////////////////////////