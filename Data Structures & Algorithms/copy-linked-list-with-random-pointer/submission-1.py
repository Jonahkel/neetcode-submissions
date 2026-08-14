"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        node_map : dict[Node, Node] = {}
        node = head
        while node is not None:
            node_copy = Node(node.val)
            node_map[node] = node_copy
            node = node.next
        node = head
        while node is not None:
            node_copy = node_map[node]
            if node.next: node_copy.next = node_map[node.next]
            if node.random: node_copy.random = node_map[node.random]
            node = node.next
        return node_map[head]