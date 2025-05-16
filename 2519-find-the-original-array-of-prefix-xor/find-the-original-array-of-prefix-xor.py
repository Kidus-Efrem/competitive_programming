class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        arr = [0 for i in range(len(pref))]
        for i in range( len(pref)):

            arr[i] = pref[i]^pref[i-1] if i>0 else pref[i]


        return arr