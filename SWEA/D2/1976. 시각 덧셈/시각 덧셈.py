T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    s_h, s_m, e_h, e_m = map(int, input().split())
    m_cnt = 0 # 분 올림
    ans_m = s_m + e_m
    ans_h = s_h + e_h
    if ans_m >= 60:
        m_cnt += 1
        ans_m = ans_m % 60
    if ans_h >= 13:
        ans_h = ans_h % 13 + 1
    if ans_h + m_cnt >= 13:
        ans_h = 1
    else:
        ans_h += m_cnt
    print(f"#{test_case} {ans_h} {ans_m}")
    # ///////////////////////////////////////////////////////////////////////////////////
