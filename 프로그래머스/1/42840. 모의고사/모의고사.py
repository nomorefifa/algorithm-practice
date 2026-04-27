def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ans = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == a[i % 5]:
            ans[0] += 1
        if answers[i] == b[i % 8]:
            ans[1] += 1
        if answers[i] == c[i % 10]:
            ans[2] += 1
    tmp = max(ans)
    t = []
    for i in range(3):
        if ans[i] == tmp:
            t.append(i + 1)
    return t