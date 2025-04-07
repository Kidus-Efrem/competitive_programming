class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c ):
            if r>= len(grid) or min(r, c)< 0 or c >=len(grid[0]) or grid[r][c]=="0":
                return
            directions = [(0, 1), (0, -1), (1, 0), (-1 ,0)]
            grid[r][c]= "0"
            # visited.add(grid[r][c])
            for dr, dc in directions:
                dfs(r+dr, c+dc)
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]== "1":
                    dfs(i, j)
                    cnt+=1
        return cnt

            