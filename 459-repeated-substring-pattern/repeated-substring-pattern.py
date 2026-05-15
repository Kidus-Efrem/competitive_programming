class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        m = len(s)
        fail = [ - 1] * m
        j = -1
        for i in range(1, m):
            while j != -1 and s[i] != s[j+1]:
                j = fail[j]
            if s[j+1] == s[i]:
                j += 1
            fail[i] = j
        print(fail)
        patterns = len(s) - fail[-1]
        print(patterns -1 )
        return fail[-1] != -1 and len(s) %(patterns-1)== 0 