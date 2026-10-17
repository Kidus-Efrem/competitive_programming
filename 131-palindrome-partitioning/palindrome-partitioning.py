class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        n = len(s)
        def solve(start, end , arr):
            if start  == n:
                ans.append(arr)
                return
            if end==n:
                return
    
                 
            k ,l = start, end
            case = True
            while k <=l:
                if s[k] != s[l]:
                    case = False
                    break
                k+=1 
                l-=1
            if case:
                arr.append(s[start:end+1])
                solve(end +1 , end+1 , arr[:])
                arr.pop()
            solve(start, end + 1, arr[:])
        solve(0 , 0 , [])
        return (ans)
            