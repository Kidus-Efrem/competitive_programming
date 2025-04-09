"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, e, id):
        # print(e.id)
        n = len(e)
        d = {i:[] for i in range(1, n+1)}
        imp = {i:None for i in range(1,n+1)}
        for i in e:
            d[i.id]= i.subordinates
            imp[i.id] = i.importance
        def dfs( vertex, visited):
            visited.add(vertex)
            val = imp[vertex]
            # print(total )
            for neighbour in d[vertex]:
                if neighbour not in visited:
                    # total+=imp[neighbour]
                    val += dfs(neighbour, visited)
            return val
        # total = imp[id]
        visited = set()
        total  = dfs( id, visited )

        return(total)