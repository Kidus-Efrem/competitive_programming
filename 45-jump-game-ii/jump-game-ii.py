class Solution:
    def jump(self, nums: List[int]) -> int:
        def iter():
            n = len(nums)
            
            dp = [float('inf') for i in range(n+1)]
            dp[1] = 0
            for i in range(1, len(nums)+1):
                for j in range(1, nums[i-1]+1):
                    if i +j < n+1:
                        dp[i+j] = min( dp[i]+1, dp[i+j])
            return dp[n]
        return(iter())