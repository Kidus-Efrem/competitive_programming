from collections import deque
from typing import List

class Solution:
    def shortestPath(self, mat: List[List[int]], k: int) -> int:
        
        visited = set()
        que = deque()
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def inbound(r, c):
            return 0 <= r < len(mat) and 0 <= c < len(mat[0])
        
        que.append((0, 0, k))
        visited.add((0, 0, k))
        distance = 0
        
        while que:
            size = len(que)
            for _ in range(size):
                r, c, rem_k = que.popleft()

                if (r, c) == (len(mat) - 1, len(mat[0]) - 1):
                    return distance
                
                for dr, dc in dir:
                    nr, nc = r + dr, c + dc
                    
                    if inbound(nr, nc):
                        if mat[nr][nc] == 0 and (nr, nc, rem_k) not in visited:
                            visited.add((nr, nc, rem_k))
                            que.append((nr, nc, rem_k))
                        
                        elif mat[nr][nc] == 1 and rem_k > 0 and (nr, nc, rem_k - 1) not in visited:
                            visited.add((nr, nc, rem_k - 1))
                            que.append((nr, nc, rem_k - 1))
            
            distance += 1
        
        return -1
