class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n-1):
            for j in range(i,n):
                if nums[i]==nums[j] and (i*j)%k == 0 and i<j:
                    count+=1
        return count