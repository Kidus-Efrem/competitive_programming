class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dir = [(1, 0),  (0, 1), (-1, 0), (0, -1)]
        def inbound(i, j):
            return 0<=i< len(matrix) and 0<= j < len(matrix[i])

        ind = defaultdict(int)
        for i in range(n):
            for j in range(len(matrix[i])):
                for dr, dc  in dir:
                    nr , nc = dr+i, dc+j
                    if inbound(nr, nc) and matrix[nr][nc] > matrix[i][j]:
                        ind[(nr, nc)]+=1
                        
        queue = deque()
        visited = set()
        for i in range(n):
            for j in range(len(matrix[i])):
                if ind[(i, j)]==0:
                    queue.append((i, j))
                    visited.add((i, j))
        cnt = 0
        while queue:
            
            print(queue)
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr , dc in dir:
                    nr , nc = r+dr , c+dc
                    if inbound(nr, nc) and matrix[nr][nc] > matrix[r][c]:
                        ind[(nr, nc)] -= 1
                        if ind[(nr, nc)]==0 and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            queue.append((nr, nc))
            cnt +=1
        return(cnt)