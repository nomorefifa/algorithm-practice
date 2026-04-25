class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt_zero = 0
        for i in nums:
            if i == 0:
                cnt_zero += 1
        cur_idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[cur_idx] = nums[i]
                cur_idx += 1
        for i in range(cnt_zero):
            nums[cur_idx + i] = 0