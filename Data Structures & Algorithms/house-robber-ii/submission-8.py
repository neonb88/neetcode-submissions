        



'''
class Solution:     
    def rob(self, nums: List[int]) -> int:     
        if len(nums) == 1:     
            return nums[0]     
                    
        n = len(nums)     
        dp = [(0,False)]*n     
        dp[n-1] = (nums[n-1],True)     
        dp[n-2] = (nums[n-2],False)     
        for i in range(n-3, -1, -1):     
            e = nums[i]                    
            if not dp[i+2:]:                    
                dp[i] = (e,False)                    
            else:                    
                right = dp[i+2][0] < dp[i+3][0] if i < n-3                       else False
                if right:                    
                    dp[i] = (dp[i+3][0]+e, dp[i+3][1])                    
                else:                    
                    dp[i] = (dp[i+2][0]+e, dp[i+2][1])                    
            if dp[i,1]: # we wanna dodge totals where the last element was included:     
                if i < n-3:
                    if not dp[i+2][1] or not dp[i+3][1]:
                        if not dp[i+2][1]:
                            dp[i] = (e + dp[i+2][0] ,   dp[i+2][1])   
                        else:   # if  not dp[i+3][1]:
                            dp[i] = (e + dp[i+3][0] ,   dp[i+3][1])   
                else:
                    if not dp[i+2][1]:
                        dp[i] = (e + dp[i+2][0] ,   dp[i+2][1])   
                    else:
                        dp[i] = (e, False)
        print(dp)                    
        if dp[0][1] == False:                    
            return max(dp[0][0], dp[1][0])                    
        else:                    
            return max(dp[1][0], dp[2][0])                    '''   
    
     
     
     
     
     
     
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = [[-1] * 2 for _ in range(len(nums))]

        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            if memo[i][flag] != -1:
                return memo[i][flag]
            memo[i][flag] = max(dfs(i + 1, flag),
                            nums[i] + dfs(i + 2, flag or (i == 0)))
            return memo[i][flag]     
        return max(dfs(0, True), dfs(1, False))     
     
     
     
     
     





















































































