class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        ans = 0
        for i in range(len(encoded)):
            if i%2 ==1:
                ans^= encoded[i]
        for i in range(1, len(encoded)+2):
            print("i", i)
            ans^=i
        arr = [-1 for i in range(len(encoded)+1)]
        for i in range(len(encoded)+1):
            arr[i] = ans
            if i < len(encoded):
                ans^=encoded[i]
        return(arr)