class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = n
        y = n
        def checker(a):
            if a <=1:
                return a
            return checker(a/4)
        return (True if checker(x)==1 else False)
