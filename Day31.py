#Regular expression matching
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # dp[i][j] means s[0:i] matches p[0:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        dp[0][0] = True  # empty string matches empty pattern
        
        # Handle patterns like a*, a*b*, a*b*c*
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                # Case 1: direct match or '.'
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                
                # Case 2: '*'
                elif p[j - 1] == '*':
                    # zero occurrence
                    dp[i][j] = dp[i][j - 2]
                    
                    # one or more occurrence
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        
        return dp[m][n]

# container with most water
class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate current area
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            
            # Update max area
            max_area = max(max_area, area)
            
            # Move the pointer with smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area        