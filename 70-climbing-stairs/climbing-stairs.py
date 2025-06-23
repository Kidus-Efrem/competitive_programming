class Solution:
    def climbStairs(self, n: int) -> int:
        memo  = defaultdict(int)
        def helper(total):
            if total in memo:
                return memo[total]
            if total ==n:
                return 1
            if total >n:
                return 0

            result = 0
            result +=backtrack(total+1)
            result +=backtrack(total+2)
            if total not in memo:
                memo[total] = result
            return memo[total]
        def helper2():
            dp = [0 for i in range(n+1)]
            dp[0] = 1
            for i in range(n+1):
                if i+1 <len(dp):
                    dp[i+1]+=dp[i]
                if i+2 <len(dp):
                    dp[i+2]+=dp[i]
            return dp[-1]

        ans = helper2()

        return(ans)
        
            