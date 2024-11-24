class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        j =0
        count =0
        for i in range(1,len(points)):
            count+= max(abs(points[i][0]-points[j][0]),abs( points[i][1]-points[j][1]))
            j+=1
        return count