# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(head_1, head_2):

            dummy = ListNode()
            curr = dummy

            while head_1 and head_2:
                if head_1.val < head_2.val:
                    curr.next = head_1
                    head_1 = head_1.next
                else:
                    curr.next = head_2
                    head_2 = head_2.next
                
                curr = curr.next
            
            curr.next = head_1 if not head_2 else head_2
            return dummy.next
        
        while len(lists) > 1:
            head_1 = lists.pop()
            head_2 = lists.pop()

            merged_list = merge(head_1, head_2)
            lists.append(merged_list)
        
        return lists[0] if lists else None


                    

