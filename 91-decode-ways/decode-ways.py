class Solution:
    def numDecodings(self, s: str) -> int:
        
        # ans = 0
        memo = defaultdict(int)
        def back(i):
            # print('i', i)
            if i >= len(s):
                return 1
            ans = 0
            if s[i] !='0':
                # print('working 1')
                cand = s[i]
                if (i, cand) in memo:
                    ans+=memo[(i, cand)]
                else:
                    x=back(i+1)
                    memo[(i, cand)] = x

                    ans+=x
            if  i+1 < len(s):
                cand = s[i]+s[i+1]
                if int(cand) > 26 or int(cand) < 1 or cand[0]=='0':
                    ans+=0


                else:
                    # print("working 2", cand[0])
                    if (i, cand) in memo:
                        ans+=memo[(i, cand)]
                    else:
                        x=back(i+2)
                        ans+=x
                        memo[(i, cand)] = x
            # print('i ans' ,i , ans)
            memo[i] = ans
            return memo[i]
        ans = back(0)
        # print(memo)

        return ans
                