class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        memo = {}
        def dp(left, right):

            if (left,right) not in memo:
                    
                res = 0
                mul = nums[right] * nums[left]
                for i in range(left+1,right):
                    one = dp(left,i) 
                    two = dp(i,right)
                    temp = one + two + nums[i]*mul
                    res = max(res,temp)

                memo[(left,right)] = res 

            return memo[(left,right)]

          

        return dp(0,len(nums)-1)


