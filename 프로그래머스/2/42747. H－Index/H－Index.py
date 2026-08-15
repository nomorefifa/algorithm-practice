def solution(citations):
    ans = 0
    citations.sort()
    s = 0
    e = len(citations)
    while s <= e:
        mid = (s + e) // 2
        tmp_cnt = 0
        for i in range(len(citations)):
            if citations[i] >= mid:
                tmp_cnt += 1
        if tmp_cnt >= mid:
            if mid > ans:
                ans = mid
            s = mid + 1
        else:
            e = mid - 1
    return ans