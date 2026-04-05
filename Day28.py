# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# rotate a list to the right by k places
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find length
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Step 2: Make circular
        tail.next = head
        
        # Step 3: Optimize k
        k = k % length
        
        # Step 4: Find new tail
        steps_to_new_tail = length - k - 1
        new_tail = head
        
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        
        # Step 5: Break circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
    
#    partition list around a value x such that all nodes less than x come before nodes greater than or equal to x

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head, x):
        before_head = ListNode(0)
        after_head = ListNode(0)
        
        before = before_head
        after = after_head
        
        current = head
        
        while current:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            
            current = current.next
        
        # Important: end the after list
        after.next = None
        
        # Connect both lists
        before.next = after_head.next
        
        return before_head.next
    
# reorde list to be in the form L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # Step 1: Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse second half
        prev = None
        curr = slow.next
        slow.next = None  # break list
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Step 3: Merge two halves
        first = head
        second = prev
        
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2
