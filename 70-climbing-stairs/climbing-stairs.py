class Solution:
    def climbStairs(self, n: int) -> int:
        def iter():
            dp = [0 for i in range(n+1)]
            dp[n] = 1
            for i in range(n, -1, -1):
                for  j in range(1, 3):
                    if i+j < n+1:
                        dp[i] +=dp[i+j]
            return dp[0]
        ans = iter()
        return(ans)