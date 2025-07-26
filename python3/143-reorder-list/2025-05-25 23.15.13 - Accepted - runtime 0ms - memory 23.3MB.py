# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Find midpoint
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half of linked list
        second = slow.next

        prev = None
        curr = second

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Break the linked list into two
        slow.next = None
        
        # Merge Linked Lists
        first = head
        second = prev

        while second:
            temp_1, temp_2 = first.next, second.next
            first.next = second
            second.next = temp_1

            first, second = temp_1, temp_2
        
        return head

        


        

        





        


        

        