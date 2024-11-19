class Solution:
    def sumOddLengthSubarrays(self, arr):
        total_sum = 0
        n = len(arr)
        
        # Iterate through all subarray lengths
        for length in range(1, n + 1, 2):  # Odd lengths only
            for i in range(n - length + 1):  # Start of subarray
                subarray = arr[i:i + length]
                total_sum += sum(subarray)
        
        return total_sum
