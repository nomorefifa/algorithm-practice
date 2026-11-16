T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    nlist = list(input())
    n_dict = {}
    for i in range(10):
        n_dict[i] = 0
    for i in range(n):
        n_dict[int(nlist[i])] += 1
    s_list = sorted(list(n_dict.items()), key = lambda x:(-x[1], -x[0]))
    print(f"#{test_case} {s_list[0][0]} {s_list[0][1]}")
    # ///////////////////////////////////////////////////////////////////////////////////
