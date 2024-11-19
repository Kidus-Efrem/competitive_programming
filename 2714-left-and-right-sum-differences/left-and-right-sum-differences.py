class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Total sum for initializing rightSum
        total_sum = sum(nums)
        left_sum = 0
        right_sum = total_sum
        
        answer = []
        
        for num in nums:
            # Update right_sum by excluding the current element
            right_sum -= num
            # Compute the absolute difference
            answer.append(abs(left_sum - right_sum))
            # Update left_sum by including the current element
            left_sum += num
        
        return answer
