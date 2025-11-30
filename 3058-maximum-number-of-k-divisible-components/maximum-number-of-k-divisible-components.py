class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph  = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        cnt = 0
        def dfs(x, parent):
            nonlocal cnt
            ans = values[x]
            for child in graph[x]:
                if child!=parent:
                    ans += dfs(child , x)
            if ans%k ==0:
                cnt +=1
                return 0

            return ans
        dfs(0, -1)
        return (cnt)

