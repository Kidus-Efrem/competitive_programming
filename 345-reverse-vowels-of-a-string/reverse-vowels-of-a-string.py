class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l, r = 0, len(s)-1
        vowels = "aeiouAEIOU"
        s_list = list(s)
        print(s_list)
        while l< r:
            while l<r and s[l] not in vowels:
                l+=1
            while r>l and s[r] not in vowels:
                r-=1
            temp = s_list[r]
            s_list[r] = s_list[l]
            s_list[l] = temp
            l, r = l+1, r-1

        return ''.join(s_list)