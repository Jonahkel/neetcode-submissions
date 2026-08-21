# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Goal: O(n) time, O(1) space
# Brute-force
'''
Keep a stack of the first k elements. Record the kth next node. Then, set
each node p to point to node p-1, with the last one pointing to the recorded node.
Keep on repeating this process, until the list ends before filling the stack with k elements.

Complexity: O(n) time, O(k) space.

'''

# Multiple pointers?
'''
prev_group_last = node before the current k-group (or dummy at beginning).
curr_group_first = first node in group
Check if group is length k. If not, return
curr_group_last = last node in group
prev_group_last.next = curr_group_last
next_node = curr_group_first.next
for curr_node in group except the last one, starting with curr_group_first:
    temp = next_node.next
    next_node.next = curr_node
    curr_node = next_node
    next_node = temp
curr_group_first.next = next_node
prev_group_last = curr_group_first

I think this works...
Complexity: O(n) time, O(1) space

'''


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev_group_last = dummy
        while prev_group_last.next is not None:
            curr_group_first = prev_group_last.next
            curr_group_last = curr_group_first
            for _ in range(k-1):
                if curr_group_last.next is None:
                    return dummy.next
                curr_group_last = curr_group_last.next
            prev_group_last.next = curr_group_last
            curr_node = curr_group_first
            next_node = curr_group_first.next 
            for _ in range(k-1):
                temp = next_node.next
                next_node.next = curr_node
                curr_node = next_node
                next_node = temp
            curr_group_first.next = next_node
            prev_group_last = curr_group_first  
        return dummy.next  


        