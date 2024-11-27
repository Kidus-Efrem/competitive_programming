class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l, r = 0, k-1
        nums.sort()
        minDiff = float('inf')
        while r< len(nums):
            minDiff = min(minDiff, nums[r] - nums[l])
            l, r = l+1, r+1
        return minDiff