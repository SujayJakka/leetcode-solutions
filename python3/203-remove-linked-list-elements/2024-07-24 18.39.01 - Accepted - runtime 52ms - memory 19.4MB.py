# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        new_head = ListNode(-1)
        new_head.next = head

        prev = new_head
        while head:
            if head.val == val:
                prev.next = head.next
                head = prev.next
            else:
                prev = head
                head = head.next

        return new_head.next
        
    


















        