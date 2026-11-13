T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    len_list = []
    str_list = []
    for i in range(5):
        tmp = list(input())
        len_list.append(len(tmp))
        str_list.append(tmp)
    ans = ""
    max_idx = max(len_list)
    for col in range(max_idx): # 시작할 위지
        for row in range(5):
            if len_list[row] - 1 >= col:
                ans += str_list[row][col]
    print(f"#{test_case} {ans}")
    # ///////////////////////////////////////////////////////////////////////////////////
