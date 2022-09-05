# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        tri_set = {}
        ans = set()
        idx = 0

        def digui(root: Optional[TreeNode]):
            if not root:
                return 0
            tri = (root.val, digui(root.left), digui(root.right))
            if tri in tri_set:
                (node, index) = tri_set[tri]
                ans.add(node)
                return index  # 返回树的序号
            else:
                nonlocal idx
                idx += 1  # 为每个新的子树设置唯一序号
                tri_set[tri] = (root, idx)
                return idx  # 返回树的序号

        digui(root)
        return list(ans)
