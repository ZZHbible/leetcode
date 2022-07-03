#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/7/3
# project = leetcode556
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums=[]
        while n:
            nums.append(n%10)
            n=n//10
        flag=False
        begin=-1
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j]>nums[i]:
                    nums[j],nums[i]=nums[i],nums[j]
                    flag=True
                    begin=i
                    break
            if flag:
                break
        if flag:
            temp=sorted(nums[:begin],reverse=True)
            nums=temp+nums[begin:]
        ans=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            ans=ans*10+nums[i]
        return ans if flag and ans <= 2147483647 else -1

solution=Solution()
print(solution.nextGreaterElement(2147483486))