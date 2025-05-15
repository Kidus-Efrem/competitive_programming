class Solution:
    def isPowerOfTwo(self, x: int) -> bool:
        return True if x&(x-1)==0 and x!=0 else False