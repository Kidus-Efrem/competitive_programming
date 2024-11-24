class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        set_nums = set(nums)
        missing_l= []
        for i in range(1, len(nums)+1):
            if i not in set_nums:
                missing_l.append(i)
        return missing_l