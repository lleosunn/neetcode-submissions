# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur_len = 0
        prev_node = None
        cur_node = head
        while cur is not None:
            if cur_len == n:
                prev_node.next = cur.next
                cur.next = None
                return head
            prev_node = cur
            cur = cur.next
            length += 1
        
        