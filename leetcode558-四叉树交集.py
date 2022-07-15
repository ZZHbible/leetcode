#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/7/15
# project = leetcode558-四叉树交集
"""
# Definition for a QuadTree node.

"""


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        def digui(root1, root2):
            if root1.isLeaf == 1 and root2.isLeaf == 1:
                if root1.val == 1 or root2.val == 1:
                    root = Node(1, 1, None, None, None, None)
                else:
                    root = Node(0, 1, None, None, None, None)
            elif root1.isLeaf == 1 and root2.isLeaf == 0:
                if root1.val == 1:
                    root = Node(1, 1, None, None, None, None)
                else:
                    root = root2
            elif root1.isLeaf == 0 and root2.isLeaf == 1:
                if root2.val == 1:
                    root = Node(1, 1, None, None, None, None)
                else:
                    root = root1
            else:
                root = Node(0, 0, None, None, None, None)
                root.topLeft = digui(root1.topLeft, root2.topLeft)
                root.topRight = digui(root1.topRight, root2.topRight)
                root.bottomLeft = digui(root1.bottomLeft, root2.bottomLeft)
                root.bottomRight = digui(root1.bottomRight, root2.bottomRight)
                if root.topLeft.isLeaf == 1 and root.topRight.isLeaf == 1 and root.bottomLeft.isLeaf == 1 and root.bottomRight.isLeaf == 1 and root.topLeft.val == root.topRight.val and root.topLeft.val == root.bottomLeft.val and root.topLeft.val == root.bottomRight.val:
                    root.isLeaf, root.val = 1, root.topLeft.val
                    root.topLeft, root.topRight, root.bottomLeft, root.bottomRight = None, None, None, None
            return root

        return digui(quadTree1, quadTree2)
