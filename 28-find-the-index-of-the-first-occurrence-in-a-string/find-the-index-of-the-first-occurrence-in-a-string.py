class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        fail = [-1] * m 
        j = -1
        for i in range( 1, m):
            while j != -1 and  needle[i]!= needle[j+1]:
                j = fail[j]
            if needle[i] == needle[j+1]:
                j+= 1
            fail[i] = j
        j = -1
        for i in range(len(haystack)):
            while j != -1 and needle[j+1] != haystack[i]:
                j = fail[j]
            if needle[j+1] == haystack[i]:
                j+=1
            if j == len(needle) -1:
                return(i - m + 1)
        return -1