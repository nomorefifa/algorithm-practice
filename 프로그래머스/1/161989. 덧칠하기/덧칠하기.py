def solution(n, m, section):
    ans = 0
    # nlist = [i for i in range(n + 1)]
    slist = [True] * (n + 1)
    for i in section:
        slist[i] = False
    for i in range(len(section)):
        if slist[section[i]] == True:
            continue
        for j in range(section[i], section[i] + m):
            if j >= len(slist):
                continue
            if slist[j] == False:
                slist[j] = True
        ans += 1
    return ans