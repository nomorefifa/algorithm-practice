T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, m, k = map(int, input().split())
    nlist = list(map(int, input().split()))
    nlist.sort() # 각 초에 손님 1명씩 존재(인당 한개)
    klist = [0] * 11112 # 각 초에 몇개의 붕빵 있는지
    cnt = 0
    for sec in range(1, 11112):
        if sec % m == 0:
            cnt += k
        klist[sec] += cnt
    flag = True
    for i in range(n):
        cur_sec = nlist[i]
        if klist[cur_sec] > 0:
            for j in range(cur_sec, 11112):
                klist[j] -= 1
        else:
            flag = False
            break
    if flag:
    	print(f"#{test_case} Possible")
    else:
        print(f"#{test_case} Impossible")
    # ///////////////////////////////////////////////////////////////////////////////////
