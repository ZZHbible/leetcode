#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/6/18
# project = 剑指offer029-排序循环列表
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head == None:
            head = Node(insertVal)
            head.next = head
            return head
        cur, next_node = head, head.next
        while next_node and next_node != head:
            if (cur.val <= insertVal and next_node.val >= insertVal) or (
                    cur.val > next_node.val and insertVal < next_node.val) or (
                    cur.val <= insertVal and next_node.val < cur.val):
                cur.next = Node(insertVal, next_node)
                return head

            else:
                cur = cur.next
                next_node = next_node.next
        cur.next = Node(insertVal, head)
        return head



