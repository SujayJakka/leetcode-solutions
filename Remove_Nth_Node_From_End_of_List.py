# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        pointer = head
        
        
        while pointer:
            pointer = pointer.next
            length+=1
            
        if length == 1 and n == 1:
            return None
            
        count = 1
        pointer = head
        target = length - (n - 1)
        
        if target - 1 == 0:
            return head.next
        
        while pointer:
            if(count == target - 1):
                temp = pointer.next
                temp2 = temp.next
                pointer.next = temp2
                break
            pointer = pointer.next
            count += 1
        
        return head
        
