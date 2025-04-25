class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        d = {i:[] for i in range(n)}
        ind = defaultdict(int)
        for u, v in edges:
            d[u].append(v)
            ind[v]+=1

        ans = [set() for i in range(n)]

        queue = deque([i for i in range(n) if ind[i]==0])

        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                for child in d[cur]:
                    ind[child]-=1
                    ans[child].add(cur)
                    ans[child].update(ans[cur])
                    if ind[child]==0:
                        queue.append(child)
        ans = [sorted(list(i)) for i in ans]
        return ans