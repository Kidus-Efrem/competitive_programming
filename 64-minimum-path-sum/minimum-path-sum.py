class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        def inbound(i, j):
            return 0<=i < len(grid) and 0<=j<len(grid[i])
        def iter():
            dp =grid.copy()
            # dp[0][0] = 0
            for i in range(n):
                for j in range(m):
                    temp = float("inf")
                    if inbound(i-1, j):
                       temp = min(temp, grid[i-1][j])
                    if inbound(i, j-1):
                        temp = min(temp, grid[i][j-1])
                    if temp== float("inf"):
                        temp = 0
                    dp[i][j]+=temp
                # print(dp)
            return dp[n-1][m-1]
        return iter()