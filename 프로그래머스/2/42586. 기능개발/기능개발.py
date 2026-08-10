def solution(progresses, speeds):
    ans = []
    idx = 0
    while idx < len(progresses):
        tmp_ans = 1
        cnt = 0 # 현재 idx의 일수
        if (100 - progresses[idx]) % speeds[idx] == 0:
            cnt += (100 - progresses[idx]) // speeds[idx]
        else:
            cnt += (100 - progresses[idx]) // speeds[idx] + 1
        while idx < len(progresses) - 1:
            next_cnt = 0 # 다음 idx 가 걸리는 일자, 이게 cnt 보다 낮으면 계속 다음 idx 검사
            if (100 - progresses[idx + 1]) % speeds[idx + 1] == 0:
                next_cnt += (100 - progresses[idx + 1]) // speeds[idx + 1]
            else:
                next_cnt += (100 - progresses[idx + 1]) // speeds[idx + 1] + 1
            if next_cnt <= cnt:
                idx += 1
                tmp_ans += 1
            else:
                break
        ans.append(tmp_ans)
        idx += 1
    return ans