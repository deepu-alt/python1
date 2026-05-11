# Definition for singly-linked list.
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

# integer to roman
class Solution:
    def intToRoman(self, num: int) -> str:
        # Mapping of values to Roman numerals
        val_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        
        result = ""
        
        # Convert integer to Roman
        for value, symbol in val_map:
            while num >= value:
                result += symbol
                num -= value
                
        return result

#find longest common factor
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        
        return prefix

# convert roman to integer
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        
        for i in range(len(s)):
            # If current value is less than next value → subtract
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
                
        return total

# 3sum problem
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result

# letter combinations of a phone number
class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []

        phone = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        result = []

        def backtrack(index, path):
            if index == len(digits):
                result.append(path)
                return
            
            for letter in phone[digits[index]]:
                backtrack(index + 1, path + letter)

        backtrack(0, "")
        return result

# 4 sums problem
class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 3):
            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicates for j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # Skip duplicates for left
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        # Skip duplicates for right
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result


#remove Nth node from end of list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        
        fast = dummy
        slow = dummy
        
        # Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both pointers
        while fast:
            fast = fast.next
            slow = slow.next
        
        # Remove nth node
        slow.next = slow.next.next
        
        return dummy.next        
        

# valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            if char in mapping:  # closing bracket
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:  # opening bracket
                stack.append(char)
        
        return not stack


# merge two sorted lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1)   # Dummy node to simplify logic
        current = dummy
        
        # Traverse both lists
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach remaining nodes
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        return dummy.next

#generate peranthesis
class Solution:
    def generateParenthesis(self, n: int):
        result = []
        
        def backtrack(s, open_count, close_count):
            if len(s) == 2 * n:
                result.append(s)
                return
            
            if open_count < n:
                backtrack(s + "(", open_count + 1, close_count)
            
            if close_count < open_count:
                backtrack(s + ")", open_count, close_count + 1)
        
        backtrack("", 0, 0)
        return result

#merge k sorted lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists):
        heap = []
        
        # Push initial nodes into heap
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        dummy = ListNode(0)
        current = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            
            current.next = node
            current = current.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next          


# swap nodes in pairs      
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            first = head
            second = head.next
            
            # Swapping
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move pointers forward
            prev = first
            head = first.next
        
        return dummy.next


#reverse node i n K - group
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        
        # Step 1: Check if there are at least k nodes
        count = 0
        temp = head
        while temp and count < k:
            temp = temp.next
            count += 1
        
        # If we have k nodes, reverse them
        if count == k:
            prev = None
            curr = head
            
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            # Step 3: Recursively process remaining nodes
            head.next = self.reverseKGroup(curr, k)
            
            return prev
        
        # If less than k nodes, return head as it is
        return head

# remove duplicates from sorted array
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        i = 0
        
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1


# Longest Valid Parentheses

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # base index
        max_len = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)  # reset base
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len

#divide two integres
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Edge case: overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine sign of result
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with positive values
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        
        # Bit manipulation approach
        for i in range(31, -1, -1):
            if (dividend >> i) >= divisor:
                quotient += (1 << i)
                dividend -= (divisor << i)
        
        # Apply sign
        if negative:
            quotient = -quotient
        
        # Clamp result within 32-bit range
        return max(INT_MIN, min(INT_MAX, quotient))

#substring with concatenation of all words
from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_words = len(words)
        word_map = Counter(words)
        result = []
        
        for i in range(word_len):
            left = i
            count = 0
            current_map = Counter()
            
            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]
                
                if word in word_map:
                    current_map[word] += 1
                    count += 1
                    
                    while current_map[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        current_map[left_word] -= 1
                        left += word_len
                        count -= 1
                    
                    if count == total_words:
                        result.append(left)
                
                else:
                    current_map.clear()
                    count = 0
                    left = right + word_len
        
        return result


#next permutation
class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        
        # Step 1: Find the first decreasing element
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: If found, swap with just larger element on right
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 3: Reverse the remaining part
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

#search in rotated sorted array
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1


#remove elements
class Solution:
    def removeElement(self, nums, val):
        k = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k

#search in rotated sorted array
class Solution(object):
    def searchRange(self, nums, target):
        
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            first = -1

            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    first = mid 
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return first

        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            last = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    last = mid
                    left = mid + 1
                elif nums[mid] < target:   # ✅ fixed
                    left = mid + 1
                else:
                    right = mid - 1
            
            return last

        return [findFirst(nums, target), findLast(nums, target)]

#search insert position
class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

#valid sudoku
class Solution:
    def isValidSudoko(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                box = (i // 3) * 3 + (j // 3)
                if val in rows[i] or val in cols[j] or val in boxes[box]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                boxes[box].add(val)
                return True 


#sudoko solver
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None
        Do not return anything, modify board in-place instead.
        """

        def isValid(board, row, col, num):

            # Check row
            for j in range(9):
                if board[row][j] == num:
                    return False

            # Check column
            for i in range(9):
                if board[i][col] == num:
                    return False

            # Check 3x3 box
            startRow = (row // 3) * 3
            startCol = (col // 3) * 3

            for i in range(startRow, startRow + 3):
                for j in range(startCol, startCol + 3):
                    if board[i][j] == num:
                        return False

            return True

        def solve():

            for i in range(9):
                for j in range(9):

                    # Find empty cell
                    if board[i][j] == ".":

                        # Try numbers 1 to 9
                        for num in "123456789":

                            if isValid(board, i, j, num):

                                board[i][j] = num

                                # Recursively solve
                                if solve():
                                    return True

                                # Backtrack
                                board[i][j] = "."

                        return False

            return True

        solve()

# count and say
class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"
        
        prev = self.countAndSay(n - 1)
        result = ""
        count = 1
        
        for i in range(1, len(prev)):
            if prev[i] == prev[i - 1]:
                count += 1
            else:
                result += str(count) + prev[i - 1]
                count = 1
        
        result += str(count) + prev[-1]
        
        return result

#combination sum
class Solution:
    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()
        self.backtrack(candidates, target, 0, [], result)
        return result

    def backtrack(self, candidates, target, start, path, result):
        if target == 0:
            result.append(path[:])
            return

        for i in range(start, len(candidates)):
            if candidates[i] > target:
                break
            path.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], i, path, result)
            path.pop()

    
#comibination sum 2
class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()
        self.backtrack(candidates, target, 0, [], result)
        return result

    def backtrack(self, candidates, target, start, path, result):
        if target == 0:
            result.append(path[:])
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            path.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], i + 1, path, result)
            path.pop()

# first missing positive
class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the correct position
                correct_pos = nums[i] - 1
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1