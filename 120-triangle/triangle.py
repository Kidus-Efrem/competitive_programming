class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[float('inf') for i in range(len(triangle))] for i in range(len(triangle)+1)]
        dp[0][0]=0
        n = len(triangle)
        for i in range(1,n+1):
            for j in range(n):
                if  j< len (triangle[i-1]):
                    dp[i][j]  = min(dp[i-1][j], dp[i-1][j-1], dp[i][j])+triangle[i-1][j]
                    # print(i, j ,dp)
                
        return(min(dp[len(triangle)]))
