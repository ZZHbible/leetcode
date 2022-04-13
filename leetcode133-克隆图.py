#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/4/13
# project = leetcode133-克隆图
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        node_dic=set()
        node_copy_dic={}
        from queue import Queue
        q=Queue()
        q.put(node)
        node_dic.add(node.val)
        node_copy_dic[node.val]=Node(node.val)
        while not q.empty():
            n=q.get()
            for neighbor in n.neighbors:
                if neighbor.val not in node_dic:
                    q.put(neighbor)
                    node_dic.add(neighbor.val)
                    node_copy_dic[neighbor.val]=Node(neighbor.val)
                node_copy_dic[n.val].neighbors.append(node_copy_dic[neighbor.val])
        return node_copy_dic[node.val]