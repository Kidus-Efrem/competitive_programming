class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        memo = defaultdict(int)
        def recur(i, j):
            # print(i, j)
            if i ==len(a):
                return 0
            if j==len(b):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            total = 0
            if a[i] == b[j]:
                total =  recur(i+1, j+1)+1
            total = max(recur(i+1, j), recur(i, j+1), total)
            memo[(i, j)] = total
            return total

        return recur(0, 0)
