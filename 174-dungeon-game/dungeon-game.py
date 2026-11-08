class Solution:
    def calculateMinimumHP(self, lst: list[list[int]]) -> int:
        n  = len(lst)
        m  = len(lst[0])
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(n):
            dp[i][-1]= -math.inf
        for j in range(m):
            dp[-1][j] = -math.inf
        dp[-1][-2] = 0
        dp[-2][-1] =0
        def fill(i , j ):
            print(i , j , dp[i][j],min(dp[i][j], max(dp[i][j+1], dp[i+1][j])+ lst[i][j])) 

            dp[i][j] = min(dp[i][j], max(dp[i][j+1], dp[i+1][j])+ lst[i][j])
        for i in range(n-1, -1 ,-1):
            for j in range(m-1, -1, -1):
                fill(i , j)
        for d in dp:
            print(d)
        if dp[0][0] > 0:
            return dp[0][0]
        else:
            return -dp[0][0] + 1