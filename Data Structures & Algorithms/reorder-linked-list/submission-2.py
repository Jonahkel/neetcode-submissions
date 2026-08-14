# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        tail = mid = head
        while tail.next and tail.next.next:
            mid = mid.next
            tail = tail.next.next
        if tail.next:
            tail = tail.next
        
        temp = mid.next
        mid.next = None
        mid = temp
        
        prev = None
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        
        while head and tail:
            temp = head.next
            head.next = tail
            head = temp

            temp = tail.next
            tail.next = head
            tail = temp
        




        
        