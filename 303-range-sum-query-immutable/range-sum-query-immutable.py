class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        for i in range(len(nums)):
            if i-1 >-1:
                nums[i]= nums[i-1] + nums[i]
            else:
                pass
        
    def sumRange(self, left: int, right: int) -> int:
        if left-1>-1:
            return self.nums[right] - self.nums[left-1]
        else:
            return self.nums[right]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)