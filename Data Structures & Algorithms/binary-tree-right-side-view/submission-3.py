# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        top = deque([root])
        sol = [root.val]
        bottom = deque()
        while True:
            while len(top) != 0:
                node = top.popleft()
                if node.left is not None:
                    bottom.append(node.left)
                if node.right is not None:
                    bottom.append(node.right)
            if len(bottom) == 0:
                return sol
            else:
                sol.append(bottom[-1].val)
                top = bottom
                bottom = deque()
            