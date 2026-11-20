T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    nlist = list(map(int, input().split()))
    n = nlist[0]
    nlist = nlist[1:]
    cur_fuel = nlist[0]
    cnt = 0
    for i in range(1, n):
        cur_fuel -= 1
        if cur_fuel >= n - 1 - i: #현재 전지로 목적지 도달 가능
            break
        else: #없다면 지금 전지를 바꿀지 아니면 다음에 바꿀지 탐색
            if cur_fuel <= 0: #연로 0이하면 여기서 충전
                cur_fuel = nlist[i]
                cnt += 1
            else: #0보다 많으면 넣고갈지 다음에 넣을지 탐색
                cur_stop = i
                for j in range(i + 1, i + cur_fuel + 1):
                    if cur_stop + nlist[cur_stop] < j + nlist[j]:
                        cur_stop = j
                if cur_stop == i:
                    cur_fuel = nlist[cur_stop]
                    cnt += 1
    print(f"#{test_case} {cnt}")