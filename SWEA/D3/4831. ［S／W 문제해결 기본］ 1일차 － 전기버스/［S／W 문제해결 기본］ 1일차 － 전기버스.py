T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    k, n, m = map(int, input().split())
    mlist = list(map(int, input().split()))
    cur_dis = k + 1 # 현재 갈 수 있는 정류장 수
    flag = False
    cnt = 0
    for i in range(n + 1):
        if cur_dis -1 < 0:
            break
        cur_dis -= 1
        if i in mlist: # 현재가 주유소 일때만 검사
            rest_n = n - i # 종점까지 남은 정류장 수
            if cur_dis >= rest_n: # 종점까지 충전없이 갈 수있으면 종료.
                flag = True
                break
            else: # 종점까지 충전없이 못가면 현재 주유소에서 충전 해야될 지, 아니면 다음 주유소에서 해도 될지 검증
                if mlist.index(i) < m - 1:
                    next_m = mlist[mlist.index(i) + 1]
                else: # 현재가 마지막 주유소면 다음 주유소는 없음(현재로 유지), 현재 넣고 종점까지 갈 수 있으면 True, 못가면 False
                    if k >= rest_n:
                        cnt += 1
                        flag = True
                        break
                    else:
                        break
                    next_m = i
                rest_m = next_m - i # 다음 주유소까지 남은 정류장 수
                if cur_dis < rest_m: # 다음 주유소까지 못가면 현재 정류장에서 주유
                    cur_dis = k
                    cnt += 1
    if flag:
        print(f"#{test_case} {cnt}")
    else:
        print(f"#{test_case} 0")
    # ///////////////////////////////////////////////////////////////////////////////////
