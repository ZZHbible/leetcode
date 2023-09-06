#!/usr/bin/env python
# author = 'ZZH'
# time = 2023/9/6
# project = leetcode1123-最深叶节点的最近公共祖先
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.node_list = []

        def digui(root, depth, list):
            if not root.left and not root.right:
                list.append(root)
                self.node_list.append(list.copy()) # 保存每个叶子节点的路径
                list.pop()
                return
            list.append(root)
            if root.left:
                digui(root.left, depth + 1, list)
            if root.right:
                digui(root.right, depth + 1, list)
            list.pop()

        digui(root, 0, [])
        if len(self.node_list) < 2: return self.node_list[0][-1]
        depth_node_list = sorted(self.node_list, key=lambda x: -len(x))

        if len(depth_node_list[0]) != len(depth_node_list[1]):
            return depth_node_list[0][-1]
        i = 1
        while i < len(depth_node_list) and len(depth_node_list[i]) == len(depth_node_list[0]): # 找深度最深的一组node_list[:i]
            i += 1
        depth_node_list = depth_node_list[:i]
        ret = depth_node_list[0][0]
        for i in range(len(depth_node_list[0])):
            node = depth_node_list[0][i]
            for l in depth_node_list:
                if node != l[i]:
                    return ret
            ret = node
        return ret
