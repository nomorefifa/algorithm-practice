class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur_idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[cur_idx] = nums[i]
                cur_idx += 1
        for i in range(cur_idx, len(nums)):
            nums[i] = 0