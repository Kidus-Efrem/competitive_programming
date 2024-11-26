class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_len = float('inf')
        l=0
        current_sum=0

        for r in range(len(nums)):
            current_sum+=nums[r]
            while current_sum >= target:
                min_len=min(min_len, r-l+1)
                current_sum-=nums[l]
                l+=1
        if min_len==float('inf'):
            return 0
        else: return min_len

        
     
            
            
         