# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None

        while slow:
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode

        first,last = head, prev

        while first and last:
            if first.val != last.val:
                return False
            
            first = first.next
            last = last.next
        
        return True