class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for i in range(n+1)]
        for u, v,w in times:
            graph[u].append((v, w))
            # graph[v].append((u, w))
        # print(graph)
        dist = [math.inf for i in range(n+1)]
        dist[k] = 0
        queue = []
        heappush(queue,(0, k) )
        while queue:
            # print(queue)
            weight, node = heappop(queue)
            for child, weight in graph[node]:
                if dist[child] > dist[node]+weight:
                    dist[child] = dist[node]+weight
                    heappush(queue, (dist[child], child))
        # print(dist[1:])
        if math.inf in dist[1:]:
            return -1
        return max(dist[1:])

