# Definition for a binary tree node.
from typing import List,Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        self.height = 0
        q = []

        def digui(root, depth):
            if not root:
                q.append('-100')
                return
            self.height = max(depth, self.height)
            q.append(str(root.val))
            digui(root.left, depth + 1)
            digui(root.right, depth + 1)

        digui(root, 0)
        n = 2 ** (self.height + 1) - 1
        ans = [[""] * n for _ in range(self.height + 1)]
        index = deque()
        index.append((0, (n - 1) // 2))
        i = 0
        while i < len(q):
            node = q[i]
            r, c = index.pop()
            if node != '-100':
                ans[r][c] = node
                index.append((r + 1, c + 2 ** (self.height - r - 1)))
                index.append((r + 1, c - 2 ** (self.height - r - 1)))

            i += 1
        return ans
