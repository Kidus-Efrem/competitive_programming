class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_indices = {}

        for i in range(len(nums)):
            if nums[i] in num_indices and i - num_indices[nums[i]]<=k:
                return True
            num_indices[nums[i]] = i
        return False
            