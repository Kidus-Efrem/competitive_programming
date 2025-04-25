class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
        d = {i:[] for i in range(n)}
        ind = {i:0 for i in range(n)}

        for u, v in pre:
            d[v].append(u)
            ind[u]+=1
        queue = deque( k for k, v in ind.items() if v==0)
        ans = []
        # seen = [0 for i in range(n)]
        for q in queue:
            # seen[q]=1
            ans.append(q)
        while queue:
            # for _ in range(len(queue)):
                cur = queue.popleft()
                for child in d[cur]:
                   ind[child]-=1
                   if ind[child]==0:
                    ans.append(child)
                    queue.append(child)
        return(ans if len(ans)==n else [])
