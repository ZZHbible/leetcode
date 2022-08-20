# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        index = -1
        max_val = -1
        for i, val in enumerate(nums):
            if val > max_val:
                max_val = val
                index = i
        root = TreeNode(max_val, self.constructMaximumBinaryTree(nums[:index]),
                        self.constructMaximumBinaryTree(nums[index + 1:]))
        return root
