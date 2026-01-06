class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # if the list is empty
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        
        merged: List[List[int]] = []
        
        for current_interval in intervals:
            # if merged is empty, or if the current start > last merged end -> no overlap
            if not merged or current_interval[0] > merged[-1][1]:
                merged.append(current_interval)
            # merge the current if there isn't an overlap
            else:
                merged[-1][1] = max(merged[-1][1], current_interval[1])
                
        return merged
        
        # [[1,3],[2,6],[8,10],[15,18]]
        #[1, 3], [3, 6]
        # current_interval = [2,6]
        # merged = [1, 6], [8, 10], [15,18]