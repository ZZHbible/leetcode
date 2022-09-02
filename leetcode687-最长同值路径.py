# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        if not root:
            return 0

        def digui(root):
            ret, left, right, temp = 1, 0, 0, 1
            if root.left:
                left = digui(root.left)
                if root.val == root.left.val:
                    temp += left
                    ret = max(ret, left + 1)
            if root.right:
                right = digui(root.right)
                if root.val == root.right.val:
                    temp += right
                    ret = max(ret, right + 1)
            self.ans = max(self.ans, temp)
            return ret

        digui(root)
        return self.ans - 1
