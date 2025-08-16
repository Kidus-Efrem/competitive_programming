class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = defaultdict(int)
        def recurssion(l, r, ind):
            if ind >= len(s3) and l>= len(s1) and r >=len(s2):
                return True
            elif ind>=len(s3):
                return False
            

            # ans = Tru
            ans   = False
            x = l
            if  l< len(s1) and s1[l] == s3[ind]:
                if (l+1, r, ind) in memo:
                    ans = memo[(l, r, ind)]
                else:
                    ans =  recurssion(l+1, r, ind+1)
                    memo[(l + 1, r, ind)] = ans

                if ans:
                    return True
            # l  = x 
            if r< len(s2) and  s2[r] == s3[ind]:
                if (l, r+1 , ind) in memo:
                    ans = memo[(l, r, ind)]
                else:
                    ans = recurssion(l, r+1, ind+1)
                    memo[(l, r+1, ind)] = ans
                if ans:
                    return True
 

            if not ans:
                return False
               
        return recurssion(0, 0, 0)