class Solution:
    def fib(self, n: int) -> int:
        memo = defaultdict(int)
        def back(i):
            if  i == 0 :
                return 0
            if i ==1:
                return 1
            if  i in memo:
                return memo[i]
            memo[i] =  back(i-1)+back(i-2)
            return memo[i]
        return back(n)