class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d= set()
        # ans = 0
        for num in nums:
            if num not in d:
                d.add(num)
            else:
                d.remove(num)
        return(list(d))