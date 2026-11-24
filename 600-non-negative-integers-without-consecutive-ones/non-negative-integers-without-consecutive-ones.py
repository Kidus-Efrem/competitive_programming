class Solution:
    def findIntegers(self, n: int) -> int:
        arr = list(map(int,  list(bin(n)[2:])))
        print(arr)
        n = len(arr)
        d = defaultdict(int)
        def fill(i, open , prev):
            print(i , open , prev)

            if (i , open , prev) in d:
                return d[(i , open , prev)]
            if i == n-1:
                if (prev != 1) and (arr[i] == 1 or open ): return 2
                return 1
            ans = 0
            if open:
                if not prev:
                    ans += fill(i +1, open , 0)
                    ans += fill(i+1, open , 1)
                else:
                    ans += fill(i+1, open , 0)
            else:
                if prev == 0:
                    if arr[i] ==1:
                        ans += fill(i +1, 1, 0)
                        ans += fill(i+1, 0 , 1)
                    else:
                        ans += fill(i +1, 0, 0)
                    
                else:
                    if arr[i] ==1:
                        ans += fill(i +1, 1, 0)
                    else:
                        ans += fill(i+1, 0 , 0)

            d[(i , open , prev)]  = ans
            return ans
        return (fill(0, 0, 0))