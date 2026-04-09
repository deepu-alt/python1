# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Reverse linked list
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  # store next node
            curr.next = prev       # reverse link
            prev = curr            # move prev forward
            curr = next_node       # move curr forward
        
        return prev
# longest substring without repeating charactres
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length    

#median of two sorted arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1
            
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if correct partition is found
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Odd length
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                # Even length
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            
            elif maxLeft1 > minRight2:
                right = partition1 - 1
            else:
                left = partition1 + 1

#longest palindromic substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, end = 0, 0
        
        def expand(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  # length of palindrome
        
        for i in range(len(s)):
            len1 = expand(i, i)       # Odd length palindrome
            len2 = expand(i, i + 1)   # Even length palindrome
            
            max_len = max(len1, len2)
            
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end + 1]       

# zigzag conversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [""] * numRows
        current_row = 0
        going_down = False
        
        for char in s:
            rows[current_row] += char
            
            # Change direction at top or bottom
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            current_row += 1 if going_down else -1
        
        return "".join(rows)


 # reverse integer
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        while x != 0:
            # Extract last digit
            digit = int(x % 10)
            
            # Handle negative numbers correctly
            if x < 0 and digit > 0:
                digit -= 10
            
            x = (x - digit) // 10
            
            # Check for overflow before multiplying
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > 7):
                return 0
            if rev < INT_MIN // 10 or (rev == INT_MIN // 10 and digit < -8):
                return 0
            
            rev = rev * 10 + digit
        
        return rev                            
    
# string to integer(atoi)
# class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        
        # Step 1: Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: Check sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # Step 3: Convert digits
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Step 4: Handle overflow before it happens
            if num > (2**31 - 1 - digit) // 10:
                return -2**31 if sign == -1 else 2**31 - 1
            
            num = num * 10 + digit
            i += 1
        
        return sign * num

# palindrome number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindrome
        if x < 0:
            return False
        
        # Numbers ending with 0 (but not 0 itself) are not palindrome
        if x % 10 == 0 and x != 0:
            return False
        
        reversed_half = 0
        
        # Reverse only half of the number
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # Check for even and odd length numbers
        return x == reversed_half or x == reversed_half // 10        