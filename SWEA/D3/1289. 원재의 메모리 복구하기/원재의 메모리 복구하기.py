T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    m = input()
    start = ["0"] * len(m)
    cnt = 0
    for i in range(len(m)):
        if start[i] == m[i]:
            continue
        else:
            for j in range(i, len(m)):
                start[j] = m[i]
            cnt += 1
    print(f"#{test_case} {cnt}")
    # ///////////////////////////////////////////////////////////////////////////////////
