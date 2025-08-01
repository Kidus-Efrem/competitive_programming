class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s== t:
            return True
        elif t== '':
            return False
        def iter():
            dp = [0 for i in range(len(t))]
            j = 0
            for i in range(len(t)):
                if j != len(s):
                    j+=int(t[i]==s[j])
                dp[i] = j
             
            return dp[-1]
        return iter()==len(s)