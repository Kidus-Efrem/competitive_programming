class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        swaps = True
        while swaps== True:
            swaps = False
            for i in range(n-1):
                if heights[i]<heights[i+1]:
                    heights[i+1], heights[i]= heights[i], heights[i+1]
                    names[i+1], names[i] = names[i],names[i+1]
                    swaps = True
        return names