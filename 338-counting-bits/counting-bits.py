class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            c = Counter(bin(i))
            ans.append(c['1'])
        return(ans)