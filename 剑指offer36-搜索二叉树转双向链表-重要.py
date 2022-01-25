#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/1/25
# project = 剑指offer36

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root):
        def digui(root):
            if not root:
                return
            digui(root.left)
            if (self.pre == None):
                self.head = root
            else:
                root.left = self.pre
                self.pre.right = root
            self.pre = root
            digui(root.right)

        if not root:
            return None
        self.head, self.pre = None, None
        digui(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head


root = Node(4, Node(2, Node(1), Node(3)), Node(5))
solution = Solution()
solution.treeToDoublyList(root)
