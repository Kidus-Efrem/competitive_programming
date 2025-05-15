class Solution:
    def isPowerOfThree(self, x: int) -> bool:
        if x<1:
            return False
        while x%3 == 0:
            x//=3
        return x==1