class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])
        def inbound(i, j):
            return 0 <= i < len(grid) and 0<=j < len(grid[i])
        # print(grid)
        def iter():
            dp = [[[-1, -1] for i in range(m) ]for j in range(n)]
            # print()
            # print()
            # dp[-1] = [j for j in range(m)]
            for j in range(m):
                if grid[-1][j] == 1:
                    # if j!=m-1:
                    dp[-1][j][1] = j
                    if j+1<m and grid[-1][j+1]==1:
                        dp[-1][j][0] = [j+1]
                else:
                    dp[-1][j][1]= j
                    if j-1 >=0 and grid[-1][j-1]==-1:
                        dp[-1][j][0] = j-1
            # print("table", dp)
            
            for i in range(n-1, -1 , -1):
                for j in range(m-1, -1, -1):

                    if grid[i][j]==1:
                        if inbound(i, j+1) and dp[i][j+1]!=-1 and grid[i][j+1]==1:
                            dp[i][j][0]= dp[i][j+1][1]
                        if inbound(i+1, j) and dp[i+1][j]!=-1 :
                            dp[i][j][1] = dp[i+1][j][0]
                    else:
                        if inbound(i+1, j) and dp[i+1][j]!=-1:
                            dp[i][j][1] = dp[i+1][j][0]
                        if inbound(i, j-1) and dp[i][j-1]!=-1 and grid[i][j-1]==-1:
                            dp[i][j][0] = dp[i][j-1][1]
                    # print("dp i j, ", i , j, dp[i][j])
                    # print()
                for j in range(m-1, -1, -1):

                    if grid[i][j]==1:
                        if inbound(i, j+1) and dp[i][j+1]!=-1 and grid[i][j+1]==1:
                            dp[i][j][0]= dp[i][j+1][1]
                        if inbound(i+1, j) and dp[i+1][j]!=-1 :
                            dp[i][j][1] = dp[i+1][j][0]
                    else:
                        if inbound(i+1, j) and dp[i+1][j]!=-1:
                            dp[i][j][1] = dp[i+1][j][0]
                        if inbound(i, j-1) and dp[i][j-1]!=-1 and grid[i][j-1]==-1:
                            dp[i][j][0] = dp[i][j-1][1]
            print(grid[n-1])
            print( dp[n-1][m-1])
                    # print()
               
            # print(dp)
            return dp[0]

        ans =  iter()
        newans = [ans[i][0]  for i in range(len(ans))]
        return newans
       
