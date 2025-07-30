class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n=numRows
        def iter():
            dp = []
            for i in range(1, n+1):
                dp.append([0]*i)
                dp[i-1][0],dp[i-1][-1]=1,1
            # print(dp)
            for i in range(2,n):
                for j in range(1, len(dp[i])-1):
                    dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
            return dp
        return iter()
