def remover(nums):
    if not nums:
        return 0

    unique_index = 0  # Pointer for the position of unique elements

    for i in range(1, len(nums)):
        if nums[i] != nums[unique_index]:
            unique_index += 1
            nums[unique_index] = nums[i]

    return unique_index + 1  # Return the count of unique elements

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return remover(nums)  # Just return the count of unique elements
