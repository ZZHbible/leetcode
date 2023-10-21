#!/usr/bin/env python
# author = 'ZZH'
# time = 2023/10/22
# project = leetcode1402.做菜顺序

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        pos = []
        neg = []
        for num in satisfaction:
            if num>=0:
                pos.append(num)
            else:
                neg.append(num)
        pos.sort()
        neg.sort(key=lambda x:-x)
        ans = sum([(i+1)*pos[i] for i in range(len(pos))])
        l_num = sum(pos)
        for i in range(len(neg)):
            if neg[i]+l_num > 0:
                l_num+=neg[i]
                ans+=l_num
            else:
                break
        return ans