class Solution:
    def longestPrefix(self, s: str) -> str:
        m = len(s)
        fail = [-1 ] * m
        j = -1
        for i in range(1, m):
            while j != -1 and s[i]!=s[j+1]:
                j = fail[j]
            if s[i] == s[j+1]:
                j += 1
            fail[i] = j
        return s[:fail[-1]+1]