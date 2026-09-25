def solution(schedules, timelogs, startday):
    ans = 0
    for i in range(len(schedules)):
        tmp = schedules[i] % 100
        if tmp > 49:
            target = (schedules[i] // 100 + 1) * 100 + (tmp + 10) % 60
        else:
            target = schedules[i] + 10
        flag = True
        for j in range(7):
            if (startday + j) % 7 == 6 or (startday + j) % 7 == 0:
                continue
            if timelogs[i][j] > target:
                flag = False
        if flag:
            ans += 1
    return ans