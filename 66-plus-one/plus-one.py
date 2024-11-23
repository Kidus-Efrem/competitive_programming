class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)-1
        print(n, digits[n])

        digits[n] += 1
        print(n, digits[n])
        while n >= 0:
            if digits[n] == 10 and n ==0:
                digits.insert(0,1)
                digits[n+1]=0
                print (n, digits[n])
            elif digits[n] == 10:
                digits[n-1] += 1
                digits[n] = 0
            n-= 1
        return digits
