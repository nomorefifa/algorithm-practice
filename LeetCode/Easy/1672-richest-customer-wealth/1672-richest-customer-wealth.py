class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for i in range(len(accounts)):
            tmp_sum = 0
            for j in range(len(accounts[i])):
                tmp_sum += accounts[i][j]
                if tmp_sum > max:
                    max = tmp_sum
        return max