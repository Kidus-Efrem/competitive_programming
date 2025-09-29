class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s2 = s
        n  = len(s)
        dp = [[-1 for i in range(n)] for _ in range(n)]
        # print(len(s))
        def back(i, j):
            # print(i, j)
           
            if i >j:
                return 0
            if i==j:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            
            ans = 0
            if s[i] == s[j]:
                ans = max(ans , back(i+1, j-1)+2)
                

            ans = max(ans, back(i+1, j))
            ans = max(ans, back(i, j-1), ans)
            dp[i][j] = ans
            return ans
        return back(0, len(s)-1)

