class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1, 1] for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    if dp[j][0] +1 > dp[i][0]:
                        dp[i][0] = dp[j][0]+1
                        dp[i][1] = dp[j][1]
                    elif dp[j][0] +1 == dp[i][0]:
                        dp[i][1]+= dp[j][1]
        max_ = -math.inf
        ans = 0
        for i in range(len(dp)):
            max_ = max(max_, dp[i][0])
        for i in range(len(dp)):
            if dp[i][0] == max_:
                ans += dp[i][1]
        return(ans)