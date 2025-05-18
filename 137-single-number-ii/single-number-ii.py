class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(32):
            cnt =0

            for j in range(n):
                if nums[j]>>i & 1:
                    cnt +=1
            if cnt%3==1:
                ans |= 1<<i
        newans = 0
        if ans>>31 &1:
            ans-= 2 ** 32
        return(ans)
        