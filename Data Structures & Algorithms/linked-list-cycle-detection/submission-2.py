# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n) space...
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        marker = ListNode()
        while head is not None:
            if head.next == marker: return True
            temp = head.next
            head.next = marker
            head = temp
        return False
