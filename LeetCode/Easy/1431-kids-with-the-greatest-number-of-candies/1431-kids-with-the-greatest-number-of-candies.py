class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val = max(candies)
        ans = [False] * (len(candies))
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_val:
                ans[i] = True
        return ans