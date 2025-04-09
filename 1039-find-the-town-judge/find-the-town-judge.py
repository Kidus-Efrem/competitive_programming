class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d = {i:[] for i in range(n)}
        for u, v in trust:
            d[u-1].append(v-1)
        # print('d', d)
        cnt = {i:[0,0] for i in range(n)}
        for i in range(n):
            cnt[i][0] = len(d[i])

        def dfs(vertex, visited):
            # print("cur",vertex)
            
            visited.add(vertex)
            # cnt[vertex][1]+=1
            
            for neighbour in d[vertex]:
                if neighbour not in visited:
                    cnt[neighbour][1]+=1
                    dfs(neighbour, visited )
                else:
                    cnt[neighbour][1]+=1
        visited = set()
        for i in range(n):
            if i  not in visited:
                dfs(i, visited)
        # print(cnt)
        for i in range(n):
            l, r  = cnt[i]
            if l==0 and r == n-1:
                return i+1
        return -1


        # print(cnt)