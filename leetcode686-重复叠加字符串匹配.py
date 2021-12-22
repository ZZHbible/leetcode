#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/12/22
# project = leetcode686-重复叠加字符串匹配
from collections import Counter


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        a_list,b_list=Counter(a),Counter(b)
        for key in b_list:
            if key not in a_list:
                return -1
        count=max(len(b)//len(a),len(a)//len(b))
        temp=a*count*5
        if temp.find(b)!=-1:
            return (temp.find(b)+len(b))//len(a) if (temp.find(b)+len(b))%len(a)==0 else  (temp.find(b)+len(b))//len(a) + 1
        return -1


solution=Solution()
print(solution.repeatedStringMatch("baa", "abaab"))

