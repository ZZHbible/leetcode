from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def getMidNode(left: ListNode, right: ListNode) -> Optional[ListNode]:
            if left == right:
                return None
            fast = slow = left
            while fast!=right and fast.next!=right:
                slow = slow.next
                fast = fast.next.next
            return slow

        def buildTree(left: ListNode, right: ListNode):
            if left == right:
                return None
            mid = getMidNode(left, right)
            root = TreeNode(mid.val, buildTree(left, mid), buildTree(mid.next, right))
            return root

        return buildTree(head, None)

solution=Solution()
root=solution.sortedListToBST(ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9))))))
print("hello")