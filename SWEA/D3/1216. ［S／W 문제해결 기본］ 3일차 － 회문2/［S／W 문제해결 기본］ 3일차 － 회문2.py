T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    tc = int(input())
    nlist = [input() for _ in range(100)]
    max_len = 0
    # 가로 회문 검사 먼저
    for i in range(100): # 행
        for j in range(100):
            for k in range(j + 1, 101):
                cur_str = nlist[i][j:k]
                flag = True
                for l in range(len(cur_str) // 2):
                    if cur_str[l] != cur_str[len(cur_str) - l -1]:
                        flag = False
                        break
                if flag:
                    if len(cur_str) > max_len:
                        max_len = len(cur_str)
    
    # 세로 회문 검사
    for i in range(100): # 열
        for j in range(100):
            for k in range(j + 1, 101):
                cur_str = ""
                for idx in range(j, k):
                    cur_str += nlist[idx][i]
                flag = True
                for l in range(len(cur_str) // 2):
                    if cur_str[l] != cur_str[len(cur_str) - l -1]:
                        flag = False
                        break
                if flag:
                    if len(cur_str) > max_len:
                        max_len = len(cur_str)
    print(f"#{tc} {max_len}")
    # ///////////////////////////////////////////////////////////////////////////////////
