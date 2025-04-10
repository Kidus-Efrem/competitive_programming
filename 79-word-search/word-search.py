class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions =  [(0, 1),(1, 0) , (-1, 0), (0, -1)]
        def dfs(r, c, visited, i):
            if i ==len(word):
                return True
            if   min(r, c)< 0 or r>= len(board) or c >= (len(board[0])) or board[r][c] != word [i] or (r, c)  in visited:
                # print("invalid, ", visited, (r, c))
                return False
            # print(word[i], i, board[r][c], (r, c))
            
            
            visited.add((r, c))
            for dr, dc in directions:
                # if (r+dr, c+dc) not in visited:
                    x = dfs(r+dr, c+dc, visited, i+1)
                    if x: return True

            visited.remove((r, c))
            
            return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                # if board[i][j] == word[0]:
                    x = dfs(i, j, set(), 0)
                    if x:
                        return True
        return False