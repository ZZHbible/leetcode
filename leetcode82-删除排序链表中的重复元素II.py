#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/7/7
# project = leetcode82-删除排序链表中的重复元素II
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        pre = ListNode(-1, head)
        cur = head
        next_ = head.next
        ans = pre
        while next_:
            if cur.val == next_.val:
                while next_ and cur.val == next_.val:
                    cur = cur.next
                    next_ = next_.next
                cur = next_
                if next_:
                    next_ = next_.next
                pre.next = cur
            else:
                pre, cur, next_ = pre.next, cur.next, next_.next
        return ans.next

