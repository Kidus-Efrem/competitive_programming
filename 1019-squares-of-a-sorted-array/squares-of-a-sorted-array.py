class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return [num**2 for num in nums]
        m = len(nums)-1
        for i, n in enumerate(nums):
            if n>=0:
                m=i
                break
        A, B = nums[m:], [-1*n for n in reversed(nums[:m])]

        def merge(A,B):
            a = b = 0
            ret = []
            while a < len(A) and b< len(B):
                if A[a] < B[b]:
                    ret.append(A[a])
                    a+=1
                else:
                    ret.append(B[b])
                    b+=1
            if a< len(A):
                ret.extend(A[a:])
            else:
                ret.extend(B[b:])

            return [n**2 for n in ret]
        return(merge(A,B))
