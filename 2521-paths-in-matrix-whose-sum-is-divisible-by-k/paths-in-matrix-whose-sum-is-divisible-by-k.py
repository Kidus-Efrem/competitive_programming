class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        def inbound(i, j):
            return 0<=i<n and 0<=j<m
        dir = [(0, 1), (1, 0)]
        dp = defaultdict(int)
        def back(i, j, x):
            # print(i, j, x)
            if (i, j, x) not in dp:
                # return dp[(i, j, x)]
                if (i, j) == (n-1, m-1):
                    # x = (x+grid[i][j])%k
                    if x == 0:
                        return 1
                    else:
                        return 0
                ans = 0
                for di, dj in dir:
                    ni, nj = i+di, j+dj
                    if inbound(ni, nj):
                        wait =back(ni, nj, (x+grid[ni][nj])%k)
                        # print("wait" ,i, j, ni, nj, wait)
                        ans+=wait
                        ans %= 10**9 + 7
                dp[(i, j, x)]  = ans
                return ans
            return dp[(i, j, x)]%(10**9 + 7)
            
        return back(0, 0, grid[0][0]%k)

            

                