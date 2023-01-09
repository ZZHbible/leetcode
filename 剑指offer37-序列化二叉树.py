#!/usr/bin/env python
# author = 'ZZH'
# time = 2023/1/9
# project = 剑指offer37-序列化二叉树

# Definition for a binary tree node.
from collections import defaultdict


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '|'
        mmap = defaultdict(int)
        pre = []
        order = []

        def digui_flag(root):
            if not root:
                return
            num = root.val
            root.val = str(num) + '*' * mmap[root.val]
            mmap[num] += 1
            digui_flag(root.left)
            digui_flag(root.right)

        def digui(root):
            if not root:
                return
            pre.append(root.val)
            digui(root.left)
            order.append(root.val)
            digui(root.right)

        digui_flag(root)
        digui(root)
        return ",".join(pre) + "|" + ",".join(order)

    def deserialize(self, data) -> TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "|": return None
        pre, order = data.split('|')
        pre, order = pre.split(','), order.split(',')

        def build(pre, order):
            if not pre and not order:
                return None
            root = TreeNode(pre[0])
            i = 0
            while order[i] != root.val: i += 1
            root.left = build(pre[1:i + 1], order[:i])
            root.right = build(pre[i + 1:], order[i + 1:])
            return root

        root = build(pre, order)

        def clear(root):
            if not root: return
            root.val = root.val.rstrip('*')
            clear(root.left)
            clear(root.right)

        clear(root)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
