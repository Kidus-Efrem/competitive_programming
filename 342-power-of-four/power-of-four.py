class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = n
        y = n
        def checker(a):
            if a <=1:
                return True if a==1 else False
            return checker(a/4)
        return (checker(x))
