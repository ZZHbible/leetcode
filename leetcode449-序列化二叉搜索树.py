#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/5/11
# project = leetcode449-序列化二叉搜索树

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 中序先序建树
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        first_order = ""
        mid_order = ""

        def order_digui(root):
            nonlocal first_order, mid_order
            if not root:
                return
            first_order += str(root.val)+'.'
            order_digui(root.left)
            mid_order += str(root.val)+'.'
            order_digui(root.right)

        order_digui(root)
        return first_order + '|' + mid_order

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        first_order, mid_order = data.split('|')
        first_order=first_order.split('.')
        mid_order=mid_order.split('.')
        if len(first_order)!=0:
            first_order.pop()
            mid_order.pop()

        def digui(first_order, mid_order):
            if not first_order:
                return None
            root = TreeNode(first_order[0])
            i = 0
            while i < len(first_order) and mid_order[i] != first_order[0]: i += 1
            root.left = digui(first_order[1:i+1], mid_order[:i])
            root.right = digui(first_order[i + 1:], mid_order[i + 1:])
            return root

        return digui(first_order, mid_order)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
root=TreeNode(22)
root.left=TreeNode(1)
root.right=TreeNode(3)
ser = Codec()
deser = Codec()
tree = ser.serialize(root)
ans = deser.deserialize(tree)
# return ans