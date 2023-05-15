#!/usr/bin/env python
# author = 'ZZH'
# time = 2023/5/15
# project = leetcode300-最长递归子序列-重要！
from typing import List

# note: 二分查找做，重要！link: https://leetcode.cn/problems/longest-increasing-subsequence/solutions/24173/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans,len_=[0]*len(nums),0
        for num in nums:
            i,j=0,len_
            while i < j:
                m=i+((j-i)>>1)
                if ans[m] >= num:
                    j=m
                else:
                    i=m+1
            ans[i]=num
            if j==len_: len_+=1
        return len_