# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        back = head
        for i in range(n):
            back = back.next
        if back is None:
            return head.next
        front = head
        back = back.next
        while back is not None:
            front, back = front.next, back.next
        front.next = front.next.next
        return head
            