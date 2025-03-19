class Solution:
    def subsets(self, lst: List[int]) -> List[List[int]]:
        arr=[[]]
        n = len(lst)
        def helper(temp, j):
            if len(arr)==2**n:
                return
            while j <n:
                temp.append(lst[j])
                arr.append(list(temp))
                helper(temp,j+1)
                temp.pop()
                j+=1
        helper([], 0)
        return(arr)