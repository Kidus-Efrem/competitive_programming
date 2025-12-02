class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        table = defaultdict(int)
        mod = 10**9 + 7
        for x, y in points:
            table[y] += 1
            
        total = 0
        for k in table.keys():
            n = table[k]
            table[k] = ((n * (n - 1)) // 2)
            total = (table[k] + total) % mod
        ans = 0
        for k in table.keys():
            total -= table[k]
            ans = (ans  + (total * table[k])) % mod
        return ans

