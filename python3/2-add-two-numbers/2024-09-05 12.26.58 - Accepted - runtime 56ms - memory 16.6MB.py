# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        ptr1, ptr2 = l1, l2
        digits = -1
        res = []

        while l1 is not None or l2 is not None:
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            digits += 1
        
        for i in range(digits + 1):
            if ptr1 is not None:
                num1 += (ptr1.val * (10 ** i))
                ptr1 = ptr1.next
            if ptr2 is not None:
                num2 += (ptr2.val * (10 ** i))
                ptr2 = ptr2.next
        
        sum_thing = num1 + num2
        sum_str = str(sum_thing)

        res = None
        for i in range(len(sum_str) - 1, -1, -1):
            if i == len(sum_str) - 1:
                ptr = ListNode(sum_str[len(sum_str) - 1])
                res = ptr
            else:
                ptr.next = ListNode(sum_str[i])
                ptr = ptr.next
        
        return res