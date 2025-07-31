# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        head = prev
        curr = prev
        max_val = curr.val

        while curr.next:
            if curr.next.val < max_val:
                curr.next = curr.next.next
            else:
                max_val = max(curr.next.val, max_val)
                curr = curr.next

        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        
        return prev
        