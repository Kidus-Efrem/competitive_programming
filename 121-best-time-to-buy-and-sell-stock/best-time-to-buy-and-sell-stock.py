class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = float("inf")
        n = len(prices)
        ans = -float("inf")
        for i in range(n):
            min_ = min(prices[i], min_)
            ans = max(prices[i]- min_, ans)
        return(max(0, ans))
