class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        min_ = float('inf')
        cnt = 0
        for i in range(len(arr1)):
            a = arr1[i]
            flag = True
            for j in range(len(arr2)):
                b = arr2[j]
                if abs(a-b)<=d:
                    flag = False
                    break
            if flag:
                cnt+=1

        return (cnt)