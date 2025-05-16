class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix= [0 for i in range(n+1)]
        for i in range(n):
            prefix[i+1]= arr[i]^prefix[i]
        ans = []
        for l, r  in queries:
            ans.append(prefix[l]^prefix[r+1])
        return(ans)