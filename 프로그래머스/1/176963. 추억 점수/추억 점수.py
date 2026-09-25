def solution(name, yearning, photo):
    ans = []
    name_dict = {}
    for i in range(len(name)):
        name_dict[name[i]] = yearning[i]
    for i in range(len(photo)):
        tmp = 0
        for j in range(len(photo[i])):
            if photo[i][j] in name_dict:
                tmp += name_dict[photo[i][j]]
        ans.append(tmp)
    return ans