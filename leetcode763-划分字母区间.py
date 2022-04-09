#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/4/9
# project = leetcode763-划分字母区间
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        from collections import Counter, defaultdict
        s_dic = Counter(s)
        temp_dic = defaultdict(int)
        ans = []
        for ch in s:
            temp_dic[ch] += 1
            if temp_dic[ch] == s_dic[ch]:
                flag = True
                sum_ = 0
                for k in temp_dic:
                    sum_ += temp_dic[k]
                    if temp_dic[k] != s_dic[k]:
                        flag = False
                if flag:
                    ans.append(sum_)
                    temp_dic = defaultdict(int)

        return ans


solution = Solution()
print(solution.partitionLabels("ababcbacadefegdehijhklij"))
