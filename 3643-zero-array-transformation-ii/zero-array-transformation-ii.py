class Solution:
    def minZeroArray(self, nums: List[int], q: List[List[int]]) -> int:
        if sum(nums)==0:
            return 0
        def helper(m):
            arr = [0]*(len(nums)+1)
            
            for i in range(m+1):
                l, r, v = q[i]
                arr[l]+=v
                arr[r+1]-=v
            arr2 = arr[:]
            for i in range(1, len(arr)):
                arr2[i]+=arr2[i-1]
            for i in range(len(nums)):
                if arr2[i]< nums[i]:
                    return False
            return True
        l, h = 0, len(q)-1
        ans = -1
        while l<=h:
            mid = (l+h)//2
  
            if helper(mid):
                h = mid-1
            else:
                l= mid+1
        n = len(q)
        return l+1 if l< n else -1