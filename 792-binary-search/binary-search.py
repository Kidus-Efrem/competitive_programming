class Solution(object):
    
    def search(self, nums, target):
        lo, hi = 0, len(nums) -1

        while lo <= hi:
            mid = (lo+ hi) // 2
            mid_number = nums[mid]

            if mid_number == target:
                return mid
            elif mid_number > target:
                hi = mid - 1
            elif mid_number< target:
                lo = mid+1
        return -1
