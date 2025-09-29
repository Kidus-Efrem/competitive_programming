class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp= [[0 for i in range(n+1)] for _ in range(m+1)]
        dp[1][1]= 1
        for i in range(0, m+1):
            for j in range(0, n+1):
                if i-1>=0:
                    dp[i][j] += dp[i-1][j]
                if j-1>=0:
                    dp[i][j]+=dp[i][j-1]
        # print(dp)
        return dp[m][n]