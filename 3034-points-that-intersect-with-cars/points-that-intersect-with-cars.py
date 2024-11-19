class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        # Use a set to store unique points
        points = set()
        
        for start, end in nums:
            # Add all points in the range [start, end]
            points.update(range(start, end + 1))
        
        # The size of the set is the number of unique points
        return len(points)
