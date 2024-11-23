class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits)-1, -1 ,-1):
            digits[i] += carry
            if digits[i] < 10:
                return digits
            digits[i] =0
        return [1]+digits
