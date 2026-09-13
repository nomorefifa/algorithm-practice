def solution(signals):
    #최소공배수로 최적화o(지금생각안남)
    max_sec = 1
    for i in signals:
        max_sec *= sum(i)
    sec = 0
    ans = -1
    cyc = [sum(i) for i in signals]
    while sec <= max_sec:
        tmp = []
        for i in range(len(signals)):
            cur_color = (sec - 1) % cyc[i]
            if signals[i][0] <= cur_color <= (signals[i][0] + signals[i][1] - 1):
                tmp.append(i)
        if len(tmp) == len(signals):
            ans = sec
            break
        sec += 1
    return ans