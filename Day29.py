# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# sort the list
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base case
        if not head or not head.next:
            return head
        
        # Step 1: Find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None  # split list
        
        # Step 2: Recursively sort
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # Step 3: Merge two sorted lists
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        # Attach remaining nodes
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return dummy.next
#linked list cycle
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next          # move 1 step
            fast = fast.next.next     # move 2 steps
            
            if slow == fast:
                return True
        
        return False

# insertion sort list
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)  # dummy head of sorted list
        curr = head
        
        while curr:
            prev = dummy
            next_node = curr.next  # store next node
            
            # Find correct position in sorted part
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            # Insert current node
            curr.next = prev.next
            prev.next = curr
            
            # Move to next node
            curr = next_node
        
        return dummy.next        