

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0]*n     # [0 for i in range(n)]
        dp[n-1] = nums[n-1]
        dp[n-2] = nums[n-2]
        for i in range(n-3, -1, -1):
            e = nums[i]
            #fjfkfffff
            dp[i] = e if not dp[i+2:] else max(dp[i+2:]) + e
        return max(dp[0], dp[1])






























































































        