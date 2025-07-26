# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def greatest_divisor(num_1, num_2):
            
            while num_2 > 0:
                num_1, num_2 = num_2, num_1 % num_2
            
            return num_1
        

        curr = head

        while curr.next:
            curr.next = ListNode(greatest_divisor(curr.val, curr.next.val), curr.next)
            curr = curr.next.next

        return head
        