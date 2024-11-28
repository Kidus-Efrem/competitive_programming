class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        newArr = []
        if len(nums1)> len( nums2):
            x= nums2
            y= nums1
        else:
            x = nums1
            y = nums2

        
        for i in x:
            if i in y:
                y.remove(i)
                newArr.append(i)
        return newArr


        