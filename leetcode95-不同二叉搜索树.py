#!/usr/bin/env python
# author = 'ZZH'
# time = 2023/5/9
# project = leetcode95-不同二叉搜索树
# describe 垃圾算法，枚举再比较先序和中序能否成功建树

from typing import List,Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.flag=True

    def build(self,preorder:List,inorder:List)->Optional[TreeNode]:
        if not self.flag: return None
        if len(preorder)==0: return None

        if preorder[0] not in inorder:
            self.flag=False
            return None
        root=TreeNode(preorder[0])
        i=inorder.index(preorder[0])
        root.left=self.build(preorder=preorder[1:1+i],inorder=inorder[:i])
        root.right=self.build(preorder=preorder[1+i:],inorder=inorder[i+1:])
        return root


    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        self.ans = []
        self.preorders=[]
        def digui(i,l):
            if i==n:
                self.flag=True
                root=self.build(l,[i for i in range(1,n+1)])
                if self.flag: self.ans.append(root)
                return
            for num in range(1,n+1):
                if num in l: continue
                l.append(num)
                digui(i+1,l)
                l.pop()
        digui(0,[])
        return self.ans

solution=Solution()
print(len(solution.generateTrees(8)))
