# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []
        i = 0
        find_return_node = True
        return_node = None
        prev_node = None

        while head:
            i += 1
            stack.append(head)

            next_head = head.next

            if i == k:
                node = stack.pop()

                if find_return_node:
                    return_node = node
                    find_return_node = False
                else:
                    prev_node.next = node

                while stack:
                    next_node = stack.pop()
                    node.next = next_node
                    node = next_node
                
                prev_node = node
                node.next = next_head
                i = 0
        
            head = next_head
        
        return return_node
                

        