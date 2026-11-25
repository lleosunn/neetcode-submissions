# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur is not None:
            cur = cur.next
            length += 1
        
        target = length - n
        length = 0
        prev = None
        cur = head
        while cur is not None:
            if length == target:
                if prev == None:
                    return head.next
                else:
                    prev.next = cur.next
                    cur.next = None
        return head