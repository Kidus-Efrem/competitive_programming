class Solution:
    def maxScore(self, s):
        max_score = 0
        n = len(s)
        
        for i in range(1, n):  # Splitting at index i
            left = s[:i]
            right = s[i:]
            
            # Calculate the score: zeros in left + ones in right
            score = left.count('0') + right.count('1')
            max_score = max(max_score, score)
        
        return max_score
