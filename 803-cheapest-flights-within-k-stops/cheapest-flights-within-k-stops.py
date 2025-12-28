class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        heap = []
        dist = [[math.inf for i in range(k+2)] for i in range(n)]
        graph = [[] for i in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))
        dist[src][k+1] = 0
        heappush(heap, ( dist[src][k+1],src,k+1 ))
        # #print(k+1, 'k+1')
        while heap:
            #print('0', heap)
            d, node, rem = heappop(heap)
            #print('1', d, node, rem)
            if node == dst:
                continue
            for child,w in graph[node]:
                #print('3', dist)
                #print('4',dist[node],dist[child])
                if dist[node][rem]+ w < dist[child][rem-1] and rem>0:
                    dist[child][rem-1] = d+w
                    heappush(heap, (dist[child][rem-1], child, rem-1))
        #print(dist[dst])
        return min( dist[dst] )if min(dist[dst])!= math.inf else -1
                