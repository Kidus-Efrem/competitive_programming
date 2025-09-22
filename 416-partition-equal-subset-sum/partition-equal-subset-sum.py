class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        n = len(nums)
        memo = defaultdict(int)
        def back(i, a):
            if i >= n:
                if a == 0:
                    return True
                if a != 0:
                    return False
            if (i, a) in memo:
                return memo[(i, a)]
            # case = False
            # case |= back(i+1, a+nums[i])
                
            # case |= back(i+1, a-nums[i])
            case = back(i + 1, a + nums[i]) or back(i + 1, a - nums[i])

            memo[(i, a)] = case

            return memo[(i, a)]
        return back(0, 0)