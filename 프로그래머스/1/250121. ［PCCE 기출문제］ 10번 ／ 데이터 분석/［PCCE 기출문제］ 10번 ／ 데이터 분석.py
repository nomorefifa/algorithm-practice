def solution(data, ext, val_ext, sort_by):
    ans = []
    val_idx = 0
    sort_idx = 0
    if ext == "code":
        val_idx = 0
    elif ext == "date":
        val_idx = 1
    elif ext == "maximum":
        val_idx = 2
    else:
        val_idx = 3
        
    if sort_by == "code":
        sort_idx = 0
    elif sort_by == "date":
        sort_idx = 1
    elif sort_by == "maximum":
        sort_idx = 2
    else:
        sort_idx = 3
    for i in range(len(data)):
        if int(data[i][val_idx]) < int(val_ext):
            ans.append(data[i])
    ans = sorted(ans, key = lambda x: x[sort_idx])
    return ans