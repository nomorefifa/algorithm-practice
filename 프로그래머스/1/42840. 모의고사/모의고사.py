def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt1, cnt2, cnt3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == p1[i % len(p1)]:
            cnt1 += 1
        if answers[i] == p2[i % len(p2)]:
            cnt2 += 1
        if answers[i] == p3[i % len(p3)]:
            cnt3 += 1
    ans_num = max(cnt1, cnt2, cnt3)
    ans = []
    if cnt1 == ans_num:
        ans.append(1)
    if cnt2 == ans_num:
        ans.append(2)
    if cnt3 == ans_num:
        ans.append(3)
    return ans