from collections import defaultdict
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)  # reverse the edges: from child → parent

        memo = {}  # node -> set of ancestors

        def dfs(node):
            if node in memo:
                return memo[node]

            ancestors = set()
            for parent in graph[node]:
                ancestors.add(parent)  # direct parent
                ancestors.update(dfs(parent))  # all ancestors of the parent

            memo[node] = ancestors
            return ancestors

        result = []
        for i in range(n):
            result.append(sorted(dfs(i)))  # sort the ancestors for each node

        return result
