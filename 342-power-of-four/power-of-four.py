class Solution:
    def isPowerOfFour(self, x: int) -> bool:
        return True if x and ((x&(x-1)))==0  and x%3 ==1 else False
