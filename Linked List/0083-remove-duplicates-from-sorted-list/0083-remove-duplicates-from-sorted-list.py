# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = back = head
        while front:
            while front.next and front.val == front.next.val:
                front = front.next
            
            front = front.next
            back.next = front
            back = front
        return head
