# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        a = []

        def digui(root):
            if not root:
                return
            digui(root.left)
            a.append(root.val)
            digui(root.right)

        digui(root)
        a.append(val)

        def construct(l):
            if not l:
                return None
            index, max_val = -1, -1
            for i, val in enumerate(l):
                if val > max_val:
                    max_val, index = val, i
            root = TreeNode(max_val, construct(l[:index]), construct(l[index + 1:]))
            return root

        return construct(a)
