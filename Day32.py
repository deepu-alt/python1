class Solution:
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                
                print(f"dp[{i}][{j}] = {dp[i][j]}")

        print("\nFinal DP Table:")        
        for i in range(m + 1):
            print(dp[i])

        return dp[m][n]


# 👇 MUST CALL FUNCTION
sol = Solution()
print("Result:", sol.isMatch("aab", "c*a*b"))

#text justification 
class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0

        while i < len(words):
            line_words = []
            line_length = 0

            # Collect words for current line
            while (i < len(words) and
                   line_length + len(words[i]) + len(line_words) <= maxWidth):
                line_words.append(words[i])
                line_length += len(words[i])
                i += 1

            # Last line or single word line
            if i == len(words) or len(line_words) == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
                res.append(line)

            else:
                total_spaces = maxWidth - line_length
                gaps = len(line_words) - 1

                even_spaces = total_spaces // gaps
                extra_spaces = total_spaces % gaps

                line = ""

                for j in range(gaps):
                    line += line_words[j]

                    spaces = even_spaces
                    if j < extra_spaces:
                        spaces += 1

                    line += " " * spaces

                line += line_words[-1]
                res.append(line)

        return res
#sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x // 2
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
#climbing  stairn 
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        first, second = 1, 2

        for i in range(3, n + 1):
            first, second = second, first + second

        return second
#simplify path
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for part in path.split('/'):
            if part == '' or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return '/' + '/'.join(stack)

#edit distance 

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases
        for i in range(m + 1):
            dp[i][0] = i

        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],     # Delete
                        dp[i][j - 1],     # Insert
                        dp[i - 1][j - 1]  # Replace
                    )

        return dp[m][n]
#set matrix zero
class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Check if first row contains 0
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Check if first column contains 0
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Use first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set cells to 0 based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Zero out first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
#search 2d matrix 
class Solution:
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])

        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2

            # Convert 1D index to 2D index
            row = mid // n
            col = mid % n

            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
