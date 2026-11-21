# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is in the middle
        # we want to reverse the list from slow.next to the end

        second = slow.next
        slow.next = None
        prev = None # Eventually going to be the head of the reversed second half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2