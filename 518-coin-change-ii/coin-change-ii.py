class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # n = len()
        dp = [ 0 for i in range(amount+1)]
        dp[0] = 1
        for c in coins:

            for rem in range( amount+1):
                if rem+c <=amount:
                    dp[rem+c]+=dp[rem]
        return dp[amount]
