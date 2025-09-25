class Solution:
    def canCross(self, lst: List[int]) -> bool:
        dp = defaultdict(bool)
        def back(i, jump):
            print(i, jump)
            if i== len(lst)-1:
                return True
            if (i, jump) in dp:
                return dp[(i, jump)]
            ans = False
            for j in range(i+1, len(lst)):
                if lst[j]  - lst[i]==jump:
                    ans |= back(j, jump)
                    if ans:
                        dp[(i, jump)] = ans
                        return dp[(i, jump)]
                if lst[j]-lst[i] == jump-1:
                    ans |= back(j, jump-1)
                    if ans:
                        dp[(i, jump)] = ans
                        return dp[(i, jump)]
                if lst[j]-lst[i]==jump+1:
                    ans  |= back(j, jump+1)
                    if ans:
                        dp[(i, jump)] = ans
                        return dp[(i, jump)]
                
            dp[(i, jump)] = ans
            return dp[(i, jump)]
        if lst[1]!=1:
            return False
        if lst==[0]:
            return True
        return back(1, 1)

        
            