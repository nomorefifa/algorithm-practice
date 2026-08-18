def solution(sizes):
    w = []
    h = []
    for i in range(len(sizes)):
        w.append(max(sizes[i][0], sizes[i][1]))
        h.append(min(sizes[i][0], sizes[i][1]))
    return max(w) * max(h)