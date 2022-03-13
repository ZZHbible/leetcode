#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/3/13
# project = leetcode393
from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = 0
        def check(data,i,num):
            for _ in range(num):
                if i>=len(data) or data[i]<128 or data[i]>191:
                    return False
                i+=1
            return True
        while (i < len(data)):
            if data[i]>=192 and data[i]<=223:
                if not check(data,i+1,1):
                    return False
                else:
                    i+=1
            elif data[i]>=224 and data[i]<=239:
                if not check(data,i+1,2):
                    return False
                else:
                    i+=2
            elif data[i]>=240 and data[i]<=247:
                if not check(data,i+1,3):
                    return False
                else:
                    i+=3
            elif data[i]<128:
                pass
            else:
                return False
            i+=1
        return True
