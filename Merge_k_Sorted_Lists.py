# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        return self.mergeSort(lists)

    
    def mergeSort(self, arr):

        if len(arr) <= 1:
            if len(arr) == 0:
                return None
            return arr[0]
        
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_half = self.mergeSort(left_half)
        right_half = self.mergeSort(right_half)

        return self.merge(left_half, right_half)
        

    def merge(self, s, t):
        
        head = ListNode(0)
        temp = head

        while s and t:
            if s.val > t.val:
                temp.next = t
                t = t.next
            else:
                temp.next = s
                s = s.next
            
            temp = temp.next
        
        if s:
            temp.next = s
        else:
            temp.next = t
        
        return head.next
