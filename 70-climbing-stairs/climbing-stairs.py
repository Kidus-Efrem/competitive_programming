class Solution:
    def climbStairs(self, n: int) -> int:
        memo  = defaultdict(int)
        def backtrack(total):
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
        ans = backtrack(0)
        return(ans)
        
            