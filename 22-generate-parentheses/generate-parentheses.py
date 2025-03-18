class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(o , c, temp, arr, pr):
            if o==0 and c==0:
                arr.append(''.join(temp))
                return 
            if o>0:
                temp.append('(')
                pr+=1
                helper(o-1, c, temp, arr, pr)
                pr-=1
                temp.pop()
            if c>0 and pr>0:
                temp.append(')')
                pr-=1
                helper(o, c-1,temp, arr, pr)
                pr+=1
                temp.pop()
            return arr
        return helper(n, n, [], [], 0)
