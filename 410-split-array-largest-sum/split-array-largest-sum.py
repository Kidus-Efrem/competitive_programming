class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = max(nums), 10**18
        def helper(x):
            cnt = 0
            total =0
            for i in range(n):
                if total + nums[i] <=x:
                    total+=nums[i]
                else:
                    total = nums[i]
                    cnt+=1
            if total: cnt+=1
            # print(cnt, x)
            return cnt<=k

                
        result = r
        while l<=r:
            mid = (l+r)//2
            if helper(mid):
                result = mid
                r= mid-1
            else:
                l= mid+1
        return result


