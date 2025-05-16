class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = first
        arr = [-1 for i in range(len(encoded)+1)]
        for i in range(len(encoded)+1):
            arr[i] = ans
            if i < len(encoded):
                ans^=encoded[i]
        return(arr)