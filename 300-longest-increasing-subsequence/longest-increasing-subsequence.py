class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp =[[-1 for i in range(n)]  for j in range(n)]
        def back(i, j):
            if i >=n:
                return 0
            if  dp[i][j] != -1:
                return dp[i][j]
            ans = 0
            ans = back(i+1, j)
            if nums[i] > nums[j] or j == -1:
                ans = max(ans, back(i+1, i)+1)
            dp[i][j] = ans
            return ans
        return back(0, -1)