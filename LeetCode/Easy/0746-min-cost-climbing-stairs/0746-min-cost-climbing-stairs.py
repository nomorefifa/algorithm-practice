class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1) # -> 꼭대기층이 n+1 이므로
        for i in range(2, len(cost) + 1):
            one_pre = dp[i - 1] + cost[i - 1]
            two_pre = dp[i - 2] + cost[i - 2]
            dp[i] = min(one_pre, two_pre)
        return dp[len(cost)]