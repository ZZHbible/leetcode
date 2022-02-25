#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/2/25
# project = leetcode537

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1_shi,num1_xu=num1.split('+')
        num2_shi,num2_xu=num2.split('+')
        num1_shi,num2_shi=int(num1_shi),int(num2_shi)
        num1_xu=int(num1_xu.split('i')[0])
        num2_xu=int(num2_xu.split('i')[0])
        num_shi=num1_shi*num2_shi-num1_xu*num2_xu
        num_xu=num1_shi*num2_xu+num2_shi*num1_xu
        return str(num_shi)+'+'+str(num_xu)+'i'

solution=Solution()
print(solution.complexNumberMultiply("1+-1i", "1+-1i"))