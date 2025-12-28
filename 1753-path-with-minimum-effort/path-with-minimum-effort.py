class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m =len(heights) ,len(heights[0])

        dist =[[math.inf for i in range(m)] for i in range(n)]
        dist[0][0] = 0
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]    
        def inbound(i, j):
            return 0<= i < n and 0<=j < m
        heap = [(0, 0, 0)]
        while heap:
            d , i , j = heappop(heap)
            for dr, dc in dir:
                nr, nc = dr+ i, dc + j
                if not inbound(nr, nc):
                    continue
                if dist[nr][nc]> max(dist[i][j] , abs(heights[nr][nc] - heights[i][j])):
                    dist[nr][nc] = max(dist[i][j] , abs(heights[nr][nc] - heights[i][j]))
                    heappush(heap, (dist[nr][nc], nr, nc))

        return dist[n-1][m-1]