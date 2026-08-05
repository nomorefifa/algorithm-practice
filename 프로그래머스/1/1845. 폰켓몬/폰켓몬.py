def solution(nums):
    max_cnt = len(nums)//2
    set_nums = set(nums)
    ans = 0
    if len(set_nums) > max_cnt:
        ans = max_cnt
    else:
        ans = len(set_nums)
    return ans
        