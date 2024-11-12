class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_indcies = {}
        for i in range(len(nums)):
            if nums[i] in num_indcies and i - num_indcies[nums[i]]<=k:
                return True
            num_indcies[nums[i]]=i
        return False
            