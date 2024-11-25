# class Solution(object):
#     def sortedSquares(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         left = 0
#         right = len(nums)-1
#         pos = len(nums)-1

#         while left<=right:
#             left_squared = nums[left]**2
#             right_squared = nums[right]**2

#             if (left_squared > right_squared):
#                 nums[pos] = left_squared
#                 left+=1
#             else:
#                 nums[pos] = right_squared
#                 right -= 1
#             pos -= 1
#         return nums
        
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        res= [0]*len(nums)
        pos = len(nums) - 1

        while left <= right:
            left_squared = nums[left] ** 2
            right_squared = nums[right] ** 2


            if left_squared > right_squared:
                res[pos] = left_squared
                left += 1
            else:
                res[pos] = right_squared
                right -= 1
            pos -= 1  # Move position for the next largest square

        return res
