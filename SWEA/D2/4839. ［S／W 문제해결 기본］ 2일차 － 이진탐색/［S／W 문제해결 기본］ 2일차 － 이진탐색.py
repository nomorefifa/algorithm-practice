T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    plist = list(map(int, input().split())) # p, pa, pb
    cnt = [0, 0, 0] # idx 1, 2 가 각각 a, b
    for i in range(1, 3):
        s = 1
        e = plist[0]
        while s <= e:
            mid = (s + e) // 2
            cnt[i] += 1
            if mid == plist[i]:
                break
            elif mid > plist[i]:
                e = mid
            else:
                s = mid
    if cnt[1] < cnt[2]:
        print(f"#{test_case} A")
    elif cnt[1] > cnt[2]:
        print(f"#{test_case} B")
    else:
        print(f"#{test_case} 0")
    # ///////////////////////////////////////////////////////////////////////////////////
