# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        dummy = ListNode(0)
        dummy.next = list1
        i = 0
        prev = dummy

        while list1:
            if i == a:
                prev.next = list2
            elif i == b + 1:
                while list2.next:
                    list2 = list2.next
                list2.next = list1
                break

            prev = list1
            list1 = list1.next
            i += 1

        return dummy.next
            

        